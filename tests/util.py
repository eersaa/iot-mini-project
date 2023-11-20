import unittest

def create_coap_uri(address="localhost", port=5683, resource_path=".well-known/core"):
    return f"coap://{address}:{port}/{resource_path}"

class CoapUriCreatorTest(unittest.TestCase):
    def test_should_default_to_localhost_and_well_known_core(self):
        self.assertEqual(create_coap_uri(), "coap://localhost:5683/.well-known/core")
        
if __name__ == '__main__':
    unittest.main()