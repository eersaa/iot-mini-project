import unittest

from util.util import create_coap_uri

class CoapUriCreatorTest(unittest.TestCase):
    def test_should_default_to_localhost_and_well_known_core(self):
        self.assertEqual(create_coap_uri(), "coap://localhost:5683/.well-known/core")

    def test_should_use_default_address_and_port_when_resource_path_is_given(self):
        self.assertEqual(create_coap_uri(resource_path="temperature"), "coap://localhost:5683/temperature")

    def test_should_use_given_ipv6_address(self):
        self.assertEqual(create_coap_uri(address="[2001:0db8:85a3:0000:0000:8a2e:0370:7334]"), "coap://[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:5683/.well-known/core")

    def test_should_use_given_ipv4_address(self):
        self.assertEqual(create_coap_uri(address="127.0.0.1"), "coap://127.0.0.1:5683/.well-known/core")
        
if __name__ == '__main__':
    unittest.main()