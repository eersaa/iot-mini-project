import unittest

from aiocoap_adapter import InterfaceResource

class InterfaceResourceTests(unittest.TestCase):
    def test_should_return_resource_path_as_list(self):
        resource = InterfaceResource("resource-name")
        self.assertEqual(resource.path(), ["resource-name"])

if __name__ == '__main__':
    unittest.main()