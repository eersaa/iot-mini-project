from datacollection_protocol_driver import ApiDatacollectionProtocolDriver

class DatacollectionDsl(ApiDatacollectionProtocolDriver):
    def __init__(self, protocol_driver):
        self.driver = protocol_driver
    
    def send_updated_measurement(self, **parameters):
        temperature = parameters["temperature"]
        destination = parameters["destination"]
    
        self.driver.send_updated_measurement(temperature, destination)
    