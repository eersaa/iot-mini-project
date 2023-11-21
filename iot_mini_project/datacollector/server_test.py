import unittest
from unittest.mock import Mock

from server import Server

class FakeResource:
    def __init__(self, name):
        self.name = name

class ServerTests(unittest.TestCase):
    def test_should_add_resource_to_interface(self):
        interface = Mock()
        fake_resource = FakeResource("new-resource")
        server = Server(interface)
        server.add_resource_to_interface(fake_resource)
        interface.add_resource.assert_called_with(fake_resource)


if __name__ == '__main__':
    unittest.main()

# default /well-known/core resource could be created 
# when instantiation the interface, but it's not scope
# of server class