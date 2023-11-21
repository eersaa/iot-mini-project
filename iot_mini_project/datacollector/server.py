
class Server:
    def __init__(self, interface):
        self.interface = interface

    def add_resource_to_interface(self, resource):
        self.interface.add_resource(resource)

    def run(self):
        self.interface.run_as("server")