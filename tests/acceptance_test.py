# This same test could work against both CoAP API and database.
def test_iot_node_should_successfully_update_measurement_to_datacollector()
    iot_node.send_update({"temperature": 25, "destination": "datacollector"})
    datacollector.confirm_update({"temperature": 25})
