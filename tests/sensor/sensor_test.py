from sensor import Sensor

def test_should_return_sensor_name_when_sensor_is_created():
    sensor = Sensor("temperature")
    assert sensor.name == "temperature"

def test_should_return_zero_when_taken_empty_measurement():
    sensor = Sensor("temperature")
    sensor.take_measurement()
    assert sensor.measurement == 0