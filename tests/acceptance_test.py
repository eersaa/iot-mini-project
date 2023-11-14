
def test_should_successfully_show_one_sample_to_user_sent_from_iot_node():
    iot_system.iot_node.send_measurement_sample(type="temperature", value="25.0")
    confirm_showed_sample(iot_system.show_measurement_sample(type="temperature"), value="25.0")
