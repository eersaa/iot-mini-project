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

    def test_should_run_interface_as_server(self):
        interface = Mock()
        server = Server(interface)
        server.run()
        interface.run_as.assert_called_with("server")
        
if __name__ == '__main__':
    unittest.main()

# default /well-known/core resource could be created 
# when instantiation the interface, but it's not scope
# of server class