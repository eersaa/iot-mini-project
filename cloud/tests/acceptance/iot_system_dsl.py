
class IotSystemDsl():
    def __init__(self, protocol_driver, iot_node):
        self.driver = protocol_driver
        self.iot_node = iot_node
    
    def show_measurement_sample(self, **parameters):
        measurement_type = parameters["type"]
    
        return self.driver.show_measurement_sample(measurement_type)
    
class IotNodeDsl():
    def __init__(self, protocol_driver):
        self.driver = protocol_driver
    
    def send_measurement_sample(self, **parameters):
        measurement_type = parameters["type"]
        measurement_value = parameters["value"]
    
        self.driver.send_measurement_sample(measurement_type, measurement_value)