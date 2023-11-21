class InterfaceResource:
    def __init__(self, resource_name):
        self.resource_name = resource_name

    def path(self):
        return [self.resource_name]

class InterfaceAdapter:
    pass

    def add_resource(self, resource):
        pass

    def run_as(self, role):
        pass