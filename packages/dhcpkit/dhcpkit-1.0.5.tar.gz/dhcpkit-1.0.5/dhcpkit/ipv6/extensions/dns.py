"""
Implementation of DNS options as specified in :rfc:`3646`.
"""

from ipaddress import IPv6Address
from struct import pack
from typing import Iterable, Union

from dhcpkit.ipv6.messages import AdvertiseMessage, InformationRequestMessage, RebindMessage, RenewMessage, \
    ReplyMessage, RequestMessage, SolicitMessage
from dhcpkit.ipv6.options import Option
from dhcpkit.utils import encode_domain, encode_domain_list, parse_domain_list_bytes

OPTION_DNS_SERVERS = 23
OPTION_DOMAIN_LIST = 24


class RecursiveNameServersOption(Option):
    """
    :rfc:`3646#section-3`

    The DNS Recursive Name Server option provides a list of one or more
    IPv6 addresses of DNS recursive name servers to which a client's DNS
    resolver MAY send DNS queries [1].  The DNS servers are listed in the
    order of preference for use by the client resolver.

    The format of the DNS Recursive Name Server option is:

    .. code-block:: none

      0                   1                   2                   3
      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |      OPTION_DNS_SERVERS       |         option-len            |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                                                               |
      |            DNS-recursive-name-server (IPv6 address)           |
      |                                                               |
      |                                                               |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                                                               |
      |            DNS-recursive-name-server (IPv6 address)           |
      |                                                               |
      |                                                               |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                              ...                              |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    option-code
        OPTION_DNS_SERVERS (23).

    option-len
        Length of the list of DNS recursive name servers in octets; must be a
        multiple of 16.

    DNS-recursive-name-server
        IPv6 address of DNS recursive name server.

    :type dns_servers: list[IPv6Address]
    """

    option_type = OPTION_DNS_SERVERS

    def __init__(self, dns_servers: Iterable[IPv6Address] = None):
        self.dns_servers = list(dns_servers or [])
        """List of IPv6 addresses of resolving DNS servers"""

    def validate(self):
        """
        Validate that the contents of this object conform to protocol specs.
        """
        if not isinstance(self.dns_servers, list):
            raise ValueError("DNS servers must be a list")

        for address in self.dns_servers:
            if not isinstance(address, IPv6Address):
                raise ValueError("DNS server must be an IPv6 address")

    def load_from(self, buffer: bytes, offset: int = 0, length: int = None) -> int:
        """
        Load the internal state of this object from the given buffer. The buffer may
        contain more data after the structured element is parsed. This data is ignored.

        :param buffer: The buffer to read data from
        :param offset: The offset in the buffer where to start reading
        :param length: The amount of data we are allowed to read from the buffer
        :return: The number of bytes used from the buffer
        """
        my_offset, option_len = self.parse_option_header(buffer, offset, length)
        header_offset = my_offset

        if option_len % 16 != 0:
            raise ValueError('DNS Servers Option length must be a multiple of 16')

        # Parse the addresses
        self.dns_servers = []
        max_offset = option_len + header_offset
        while max_offset > my_offset:
            address = IPv6Address(buffer[offset + my_offset:offset + my_offset + 16])
            self.dns_servers.append(address)
            my_offset += 16

        return my_offset

    def save(self) -> Union[bytes, bytearray]:
        """
        Save the internal state of this object as a buffer.

        :return: The buffer with the data from this element
        """
        buffer = bytearray()
        buffer.extend(pack('!HH', self.option_type, len(self.dns_servers) * 16))
        for address in self.dns_servers:
            buffer.extend(address.packed)

        return buffer


class DomainSearchListOption(Option):
    """
    :rfc:`3646#section-4`

    The Domain Search List option specifies the domain search list the
    client is to use when resolving hostnames with DNS.  This option does
    not apply to other name resolution mechanisms.

    The format of the Domain Search List option is:

    .. code-block:: none

       0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |      OPTION_DOMAIN_LIST       |         option-len            |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                          searchlist                           |
      |                              ...                              |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    option-code
        OPTION_DOMAIN_LIST (24).

    option-len
        Length of the 'searchlist' field in octets.

    searchlist
        The specification of the list of domain names in the Domain Search List.

    The list of domain names in the 'searchlist' MUST be encoded as
    specified in section "Representation and use of domain names" of
    :rfc:`3315`.

    :type search_list: list[str]
    """

    option_type = OPTION_DOMAIN_LIST

    def __init__(self, search_list: Iterable[str] = None):
        self.search_list = list(search_list or [])
        """List of domain names to use as a search list"""

    def validate(self):
        """
        Validate that the contents of this object conform to protocol specs.
        """
        if not isinstance(self.search_list, list):
            raise ValueError("Search list must be a list of strings")

        for domain_name in self.search_list:
            # Just encode to validate
            encode_domain(domain_name)

    def load_from(self, buffer: bytes, offset: int = 0, length: int = None) -> int:
        """
        Load the internal state of this object from the given buffer. The buffer may contain more data after the
        structured element is parsed. This data is ignored.

        :param buffer: The buffer to read data from
        :param offset: The offset in the buffer where to start reading
        :param length: The amount of data we are allowed to read from the buffer
        :return: The number of bytes used from the buffer
        """
        my_offset, option_len = self.parse_option_header(buffer, offset, length)

        # Parse the domain labels
        parsed_len, self.search_list = parse_domain_list_bytes(buffer, offset=offset + my_offset, length=option_len)
        my_offset += parsed_len

        return my_offset

    def save(self) -> Union[bytes, bytearray]:
        """
        Save the internal state of this object as a buffer.

        :return: The buffer with the data from this element
        """
        domain_buffer = encode_domain_list(self.search_list)

        buffer = bytearray()
        buffer.extend(pack('!HH', self.option_type, len(domain_buffer)))
        buffer.extend(domain_buffer)
        return buffer


# Register where these options may occur
SolicitMessage.add_may_contain(RecursiveNameServersOption)
AdvertiseMessage.add_may_contain(RecursiveNameServersOption)
RequestMessage.add_may_contain(RecursiveNameServersOption)
RenewMessage.add_may_contain(RecursiveNameServersOption)
RebindMessage.add_may_contain(RecursiveNameServersOption)
InformationRequestMessage.add_may_contain(RecursiveNameServersOption)
ReplyMessage.add_may_contain(RecursiveNameServersOption)

SolicitMessage.add_may_contain(DomainSearchListOption)
AdvertiseMessage.add_may_contain(DomainSearchListOption)
RequestMessage.add_may_contain(DomainSearchListOption)
RenewMessage.add_may_contain(DomainSearchListOption)
RebindMessage.add_may_contain(DomainSearchListOption)
InformationRequestMessage.add_may_contain(DomainSearchListOption)
ReplyMessage.add_may_contain(DomainSearchListOption)
