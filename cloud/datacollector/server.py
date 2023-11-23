
class Server:
    def __init__(self, interface):
        self.interface = interface

    def add_resource_to_interface(self, resource):
        self.interface.add_resource(resource)

    async def run(self):
        return await self.interface.run_as("server")