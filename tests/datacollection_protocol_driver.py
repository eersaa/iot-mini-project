
class ApiDatacollectionProtocolDriver:

    def send_updated_measurement(self, type, value, destination):
        transport.send(message.create(type, value), destinations.find(destination))