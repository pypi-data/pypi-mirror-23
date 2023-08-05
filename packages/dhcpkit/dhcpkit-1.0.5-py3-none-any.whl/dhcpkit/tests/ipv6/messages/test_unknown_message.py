"""
Test the UnknownMessage implementation
"""
import unittest

from dhcpkit.ipv6.messages import UnknownMessage
from dhcpkit.tests.ipv6.messages import test_message

unknown_message = UnknownMessage(255, b'ThisIsAnUnknownMessage')
unknown_packet = bytes.fromhex('ff') + b'ThisIsAnUnknownMessage'


class UnknownMessageTestCase(test_message.MessageTestCase):
    def setUp(self):
        self.packet_fixture = unknown_packet
        self.message_fixture = unknown_message
        self.parse_packet()

    def parse_packet(self):
        super().parse_packet()
        self.assertIsInstance(self.message, UnknownMessage)

    def test_validate_message_type(self):
        self.check_unsigned_integer_property('message_type', size=8)

    def test_validate_data(self):
        # This should be ok
        self.message.message_data = b''
        self.message.validate()

        # This shouldn't
        self.message.message_data = ''
        with self.assertRaisesRegex(ValueError, 'sequence of bytes'):
            self.message.validate()


if __name__ == '__main__':
    unittest.main()
