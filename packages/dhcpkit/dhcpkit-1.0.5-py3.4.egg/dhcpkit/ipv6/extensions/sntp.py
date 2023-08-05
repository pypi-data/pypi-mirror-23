"""
Implementation of SNTP option as specified in :rfc:`4075`.
"""

from ipaddress import IPv6Address
from struct import pack
from typing import Iterable, Union

from dhcpkit.ipv6.messages import AdvertiseMessage, InformationRequestMessage, RebindMessage, RenewMessage, \
    ReplyMessage, RequestMessage, SolicitMessage
from dhcpkit.ipv6.options import Option

OPTION_SNTP_SERVERS = 31


class SNTPServersOption(Option):
    """
    :rfc:`4075#section-4`

    The Simple Network Time Protocol servers option provides a list of
    one or more IPv6 addresses of SNTP [3] servers available to the
    client for synchronization.  The clients use these SNTP servers to
    synchronize their system time to that of the standard time servers.
    Clients MUST treat the list of SNTP servers as an ordered list.  The
    server MAY list the SNTP servers in decreasing order of preference.

    The option defined in this document can only be used to configure
    information about SNTP servers that can be reached using IPv6.  The
    DHCP option to configure information about IPv4 SNTP servers can be
    found in :rfc:`2132` [4].  Mechanisms for configuring IPv4/IPv6 dual-
    stack applications are being considered, but are not specified in
    this document.

    The format of the Simple Network Time Protocol servers option is as
    shown below:

    .. code-block:: none

       0                   1                   2                   3
       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |      OPTION_SNTP_SERVERS       |        option-len            |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                                                               |
      |                  SNTP server (IPv6 address)                   |
      |                                                               |
      |                                                               |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                                                               |
      |                  SNTP server (IPv6 address)                   |
      |                                                               |
      |                                                               |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
      |                              ...                              |
      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    option-code
        OPTION_SNTP_SERVERS (31).

    option-len
        Length of the 'SNTP server' fields, in octets; it must be a multiple of 16.

    SNTP server
        IPv6 address of SNTP server.
    """

    option_type = OPTION_SNTP_SERVERS

    def __init__(self, sntp_servers: Iterable[IPv6Address] = None):
        self.sntp_servers = list(sntp_servers or [])
        """List of IPv6 addresses of SNTP servers"""

    def validate(self):
        """
        Validate that the contents of this object conform to protocol specs.
        """
        if not isinstance(self.sntp_servers, list):
            raise ValueError("SNTP servers must be a list")

        for address in self.sntp_servers:
            if not isinstance(address, IPv6Address) or \
                    address.is_link_local or \
                    address.is_loopback or \
                    address.is_multicast or \
                    address.is_unspecified:
                raise ValueError("SNTP servers must be a list of routable IPv6 addresses")

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
        header_offset = my_offset

        if option_len % 16 != 0:
            raise ValueError('SNTP Servers Option length must be a multiple of 16')

        # Parse the addresses
        self.sntp_servers = []
        max_offset = option_len + header_offset  # The option_len field counts bytes *after* the header fields
        while max_offset > my_offset:
            address = IPv6Address(buffer[offset + my_offset:offset + my_offset + 16])
            self.sntp_servers.append(address)
            my_offset += 16

        return my_offset

    def save(self) -> Union[bytes, bytearray]:
        """
        Save the internal state of this object as a buffer.

        :return: The buffer with the data from this element
        """
        buffer = bytearray()
        buffer.extend(pack('!HH', self.option_type, len(self.sntp_servers) * 16))
        for address in self.sntp_servers:
            buffer.extend(address.packed)

        return buffer


# Register where these options may occur
SolicitMessage.add_may_contain(SNTPServersOption)
AdvertiseMessage.add_may_contain(SNTPServersOption)
RequestMessage.add_may_contain(SNTPServersOption)
RenewMessage.add_may_contain(SNTPServersOption)
RebindMessage.add_may_contain(SNTPServersOption)
InformationRequestMessage.add_may_contain(SNTPServersOption)
ReplyMessage.add_may_contain(SNTPServersOption)
