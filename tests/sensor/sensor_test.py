from sensor import Sensor

def test_should_return_sensor_name_when_sensor_is_created():
    sensor = Sensor("temperature")
    assert sensor.name == "temperature"

# def test_should_throw_exception_when_sensor_is_created_without_name():
#     try:
#         Sensor()
#     except Exception as e:
#         assert str(e) == "__init__() missing 1 required positional argument: 'name'"