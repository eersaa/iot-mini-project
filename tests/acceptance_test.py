def test_should_return_one_temperature_measurement_when_sent_one_measurement():
    temperature_sensor = Sensor("temperature")
    iot_node = IotNode.add(temperature_sensor)
    public_api_service = PublicAPI().create()
    public_api_service.start()
    dashboard = Dashboard().create()

    iot_node.temperature_sensor.take_measurement()
    iot_node.send_message(public_api_service.address)

    dashboard.show("temperatures")
    assert len(dashboard.export("temperatures").list()) == 1