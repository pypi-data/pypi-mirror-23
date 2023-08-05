"""
The base class :class:`ProtocolElement` provides the basic structure for each element of the DHCP protocol. This base
class provides several functions:

- Parsing:
    Each subclass can parse a stream of bytes from a protocol packet and construct an instance that contains all the
    data from the byte stream as properties.

- Identification:
    Each category of ProtocolElement can determine which subclass is the most specific implementation for the data
    being parsed. For example when letting the Message class :func:`parse <Message.parse>` a message it will look at
    the message type code in the byte steam and determine which specific subclass should parse the data (i.e.
    SolicitMessage, RequestMessage, ReplyMessage etc). Each category of ProtocolElement has its own registry that keeps
    track of which type code corresponds to which subclass.

- Saving:
    Each instance can save its contents to a stream of bytes as required by
    the protocol.

- Validation:
    Each element can validate if its contents are valid. As protocol elements
    often contain other protocol elements (a message has options, an option
    might have sub-options etc) there are standard tools for defining which
    protocol element may contain which other protocol elements and optionally
    define a minimum and maximum occurrence. Some elements may not occur more
    than once, some elements must occur at least once, etc.

- Representation:
    The default implementation provides __str__ and __repr__ methods so that
    protocol elements can be printed for debugging and represented as a
    parseable Python string.
"""
import codecs
import collections
import inspect
from collections import ChainMap, OrderedDict
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from json.encoder import JSONEncoder
from typing import Iterable, Optional, Tuple, TypeVar, Union

infinite = 2 ** 31 - 1

# Typing helpers
SomeProtocolElement = TypeVar('SomeProtocolElement', bound='ProtocolElement', covariant=True)


class AutoMayContainTree(type):
    """
    Meta-class that automatically creates a _may_contain class property that is a ChainMap that links all
    parent _may_contain class properties.
    """

    def __new__(mcs, name, bases=None, namespace=None):
        cls = super().__new__(mcs, name, bases, namespace)

        # Get all the ChainMaps from the parents
        parent_may_contains = [getattr(base, '_may_contain') for base in bases
                               if isinstance(getattr(base, '_may_contain', None), ChainMap)]

        # And create our local one with those as lookup targets
        cls._may_contain = ChainMap({}, *parent_may_contains)

        return cls


class AutoConstructorParams(AutoMayContainTree):
    """
    Meta-class that stores the list of parameters for __init__ so that we don't have to use inspect every time we want
    to know.
    """

    def __new__(mcs, name, bases=None, namespace=None):
        cls = super().__new__(mcs, name, bases, namespace)

        # Get the signature of the __init__ method to find the properties we need to compare
        # This is why the object properties and __init__ parameters need to match, besides it being good practice for
        # an object that represents a protocol element anyway...
        signature = inspect.signature(cls.__init__)

        # Store the discovered parameters
        discovered = []
        for parameter in signature.parameters.values():
            # Skip 'self'
            if parameter.name == 'self':
                continue

            # Skip any potential *args and **kwargs in the method signature
            if parameter.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
                continue

            discovered.append(parameter.name)

        cls._init_parameter_names = discovered
        return cls


class ProtocolElement(metaclass=AutoConstructorParams):
    """
    A StructuredElement is a specific kind of class that represents a protocol message or option. Structured elements
    have the following extra requirements:

    - The constructor parameters and the internal state properties must be identical
      So if an object has a property `timeout` which is an integer then the constructor must accept a named parameter
      called `timeout` which is stored in that property. The constructor must have appropriate default values if
      possible. Empty objects, lists, dictionaries etc are represented by a default value of None.
    - The full internal state of the object must be loadable from a bytes object with the :func:`load_from` method
    - The full internal state of the object must be storable as a bytes object with the :func:`save` method
    """

    # This will be set by the meta-class
    _may_contain = None
    _init_parameter_names = None

    def validate(self):
        """
        Subclasses may overwrite this method to validate their state. Subclasses are expected to raise a ValueError
        if validation fails.
        """
        pass

    def validate_contains(self, elements: Iterable[object]):
        """
        Utility method that subclasses can use in their validate method for verifying that all sub-elements are allowed
        to be contained in this element. Will raise ValueError if validation fails.

        :param elements: The list of sub-elements
        """
        # Count occurrence
        occurrence_counters = collections.Counter()
        for element in elements:
            element_class = self.get_element_class(element)
            if element_class is None:
                raise ValueError("{} cannot contain {}".format(self.__class__.__name__, element.__class__.__name__))

            # Count its occurrence
            occurrence_counters[element_class] += 1

        # Check max occurrence
        for element_class, (min_occurrence, max_occurrence) in self._may_contain.items():
            count = occurrence_counters[element_class]
            if count > max_occurrence:
                if max_occurrence == 1:
                    raise ValueError("{} may only contain 1 {}".format(self.__class__.__name__, element_class.__name__))
                else:
                    raise ValueError("{} may only contain {} {}s".format(self.__class__.__name__, max_occurrence,
                                                                         element_class.__name__))
            elif count < min_occurrence:
                if min_occurrence == 1:
                    raise ValueError("{} must contain at least 1 {}".format(self.__class__.__name__,
                                                                            element_class.__name__))
                else:
                    raise ValueError("{} must contain at least {} {}s".format(self.__class__.__name__, max_occurrence,
                                                                              element_class.__name__))

    @classmethod
    def determine_class(cls, buffer: bytes, offset: int = 0) -> type:
        """
        Return the appropriate class to parse this element with.

        :param buffer: The buffer to read data from
        :param offset: The offset in the buffer where to start reading
        :return: The best known class for this data
        """
        return UnknownProtocolElement

    @classmethod
    def parse(cls: SomeProtocolElement, buffer: bytes,
              offset: int = 0, length: int = None) -> Tuple[int, SomeProtocolElement]:
        """
        Constructor for a new element of which the state is automatically loaded from the given buffer. Both the number
        of bytes used from the buffer and the instantiated element are returned. The class of the returned element may
        be a subclass of the current class if the parser can determine that the data in the buffer contains a subtype.

        :param buffer: The buffer to read data from
        :param offset: The offset in the buffer where to start reading
        :param length: The amount of data we are allowed to read from the buffer
        :return: The number of bytes used from the buffer and the resulting element
        """
        element_class = cls.determine_class(buffer, offset=offset)
        element = element_class()
        length = element.load_from(buffer, offset=offset, length=length)
        return length, element

    def load_from(self, buffer: bytes, offset: int = 0, length: int = None) -> int:
        """
        Load the internal state of this object from the given buffer. The buffer may contain more data after the
        structured element is parsed. This data is ignored.

        :param buffer: The buffer to read data from
        :param offset: The offset in the buffer where to start reading
        :param length: The amount of data we are allowed to read from the buffer
        :return: The number of bytes used from the buffer
        """

    def save(self) -> Union[bytes, bytearray]:
        """
        Save the internal state of this object as a buffer.

        :return: The buffer with the data from this element
        """

    def __eq__(self, other: object) -> bool:
        """
        Compare this object to another object. The result will be True if they are of the same class and if the
        properties have equal values and False otherwise.

        :param other: The other object
        :return: Whether this object is equal to the other one
        """
        # Use strict comparison, one being a subclass of the other is not good enough
        if type(self) is not type(other):
            return NotImplemented

        # Compare the discovered properties
        for parameter_name in self._init_parameter_names:
            if getattr(self, parameter_name) != getattr(other, parameter_name):
                return False

        # Amazing, all properties seem equal
        return True

    def __repr__(self):
        """
        Return a machine-readable representation of this protocol element.

        :return: Parseable representation of this protocol element
        """
        # Create a list of string with "parameter=value" for each parameter of __init__
        options_repr = ['{}={}'.format(parameter_name, repr(getattr(self, parameter_name)))
                        for parameter_name in self._init_parameter_names]

        # And construct a constructor call to show
        return '{}({})'.format(self.__class__.__name__, ', '.join(options_repr))

    def __str__(self):
        """
        Return a human-readable and indented representation of this protocol element.

        :return: Readable representation of this protocol element
        """
        if len(self._init_parameter_names) == 0:
            # No parameters: inline
            return '{}()'.format(self.__class__.__name__)
        elif len(self._init_parameter_names) == 1:
            # One parameter: inline unless the parameter has a multi-line string output
            parameter_name = self._init_parameter_names[0]
            display = getattr(self, 'display_' + parameter_name, None)
            if display:
                if callable(display):
                    attr_value = display()
                else:
                    attr_value = display
            else:
                attr_value = getattr(self, parameter_name)
            lines = str(attr_value).split('\n')

            output = '{}('.format(self.__class__.__name__, parameter_name)

            if len(lines) == 1:
                output += '{}={}'.format(parameter_name, lines[0])
            else:
                output += '\n  {}='.format(parameter_name)
                output += '{}\n'.format(lines[0])
                for line in lines[1:-1]:
                    output += '  {}\n'.format(line)
                output += '  {}\n'.format(lines[-1])

            output += ')'
            return output

        # Multiple parameters are shown one parameter per line
        output = '{}(\n'.format(self.__class__.__name__)
        for parameter_name in self._init_parameter_names:
            display = getattr(self, 'display_' + parameter_name, None)
            if display:
                if callable(display):
                    attr_value = display()
                else:
                    attr_value = display
            else:
                attr_value = getattr(self, parameter_name)

            if attr_value and isinstance(attr_value, str):
                # Show strings with repr()
                attr_value = repr(attr_value)

            if attr_value and isinstance(attr_value, list):
                # Parameters containing lists show the list content indented
                output += '  {}=[\n'.format(parameter_name)
                for element in attr_value:
                    lines = str(element).split('\n')
                    for line in lines[:-1]:
                        output += '    {}\n'.format(line)
                    output += '    {},\n'.format(lines[-1])
                output += '  ],\n'
            else:
                # Multi-line content is shown indented
                output += '  {}='.format(parameter_name)
                lines = str(attr_value).split('\n')
                if len(lines) == 1:
                    output += '{},\n'.format(lines[0])
                else:
                    output += '{}\n'.format(lines[0])
                    for line in lines[1:-1]:
                        output += '  {}\n'.format(line)
                    output += '  {},\n'.format(lines[-1])

        output += ')'

        return output

    @classmethod
    def add_may_contain(cls, klass: type, min_occurrence: int = 0, max_occurrence: int = infinite):
        """
        Add the given class to the list of permitted sub-element classes, optionally with a minimum and maximum
        occurrence count.

        :param klass: The class to add
        :param min_occurrence: Minimum occurrence for validation
        :param max_occurrence: Maximum occurrence for validation
        """
        cls._may_contain[klass] = (min_occurrence, max_occurrence)

    @classmethod
    def may_contain(cls, element: object) -> bool:
        """
        Shortcut-method to verify that objects of this class may contain element

        :param element: Sub-element to verify
        :return: Whether this class may contain element or not
        """
        return cls.get_element_class(element) is not None

    @classmethod
    def get_element_class(cls, element: object) -> Optional[type]:
        """
        Get the class this element is classified as, for occurrence counting.

        :param element: Some element
        :return: The class it classifies as
        """
        # This class has its own list of what it may contain: check it
        found_klass = None

        # NOTE: the way we loop over these classes causes one side-effect: if the element is a subclass or instance of
        # multiple classes in _may_contain, and those multiple classes are not related (so basically: element uses
        # multiple inheritance from two completely separated class trees) then this becomes non-deterministic.
        for klass in cls._may_contain:
            if inspect.isclass(element):
                if issubclass(element, klass):
                    if found_klass and issubclass(found_klass, klass):
                        # If we already found a class check whether the new class is a superclass of the previous one
                        # In that case: more specific classes can overrule less specific ones, and we don't use the
                        # superclass and keep the old one
                        continue

                    found_klass = klass

            elif isinstance(element, klass):
                if found_klass and issubclass(found_klass, klass):
                    # If we already found a class check whether the new class is a superclass of the previous one
                    # In that case: more specific classes can overrule less specific ones, and we don't use the
                    # superclass and keep the old one
                    continue

                found_klass = klass

        # Check max_occurrence
        if found_klass and cls._may_contain[found_klass][1] < 1:
            # May not contain this
            return None

        return found_klass


class UnknownProtocolElement(ProtocolElement):
    """
    Representation of a protocol element about which nothing is known.
    """

    def __init__(self, data: bytes = b''):
        self.data = data

    def load_from(self, buffer: bytes, offset: int = 0, length: int = None) -> int:
        """
        Load the internal state of this object from the given buffer. The buffer may contain more data after the
        structured element is parsed. This data is ignored.

        :param buffer: The buffer to read data from
        :param offset: The offset in the buffer where to start reading
        :param length: The amount of data we are allowed to read from the buffer
        :return: The number of bytes used from the buffer
        """
        max_length = length or (len(buffer) - offset)
        self.data = buffer[offset:offset + max_length]
        return max_length

    def save(self) -> Union[bytes, bytearray]:
        """
        Save the internal state of this object as a buffer.

        :return: The buffer with the data from this element
        """
        return self.data


class JSONProtocolElementEncoder(JSONEncoder):
    """
    A JSONEncoder that can handle ProtocolElements
    """

    def default(self, o):
        """
        Return a data structure that JSON can handle

        :param o: The object to convert
        :return: A serializable data structure
        """
        if isinstance(o, bytes):
            # Many protocol elements contain bytes, so handle them
            try:
                string = o.decode('ascii')
                if string.isprintable():
                    return string
            except UnicodeDecodeError:
                pass

            # If not possible return it hex-encoded
            return 'hex:' + codecs.encode(o, 'hex').decode('ascii')

        if isinstance(o, (IPv4Address, IPv4Network, IPv6Address, IPv6Network)):
            # Many protocol elements contain IP addresses and prefixes, so handle them
            return str(o)

        if isinstance(o, ProtocolElement):
            # Create an ordered dictionary for the parameter of __init__
            options_repr = OrderedDict()

            # noinspection PyProtectedMember
            for parameter_name in o._init_parameter_names:
                options_repr[parameter_name] = getattr(o, parameter_name)

            # And construct a constructor call to show
            return {o.__class__.__name__: options_repr}

        # Let the base class default method raise the TypeError
        return super().default(o)


class ElementDataRepresentation:
    """
    Class that represents data in a nicer way when printing it with :class:`ProtocolElement.__str__`.
    """

    def __init__(self, element_representation: str):
        self.element_representation = element_representation

    def __str__(self):
        return self.element_representation

    __repr__ = __str__
