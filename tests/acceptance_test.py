# Test setup

# This same test could work against both CoAP API and database.
def test_should_update_measurement_at_datacollector(datacollection):
    datacollection.send_updated_measurement(type="temperature", value="25.0", destination="datacollector")
    datacollection.confirm_update(type="temperature", value="25.0", destination="datacollector")