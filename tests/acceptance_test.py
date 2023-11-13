# This same test could work against both CoAP API and database.
def test_should_update_measurement_at_datacollector(datacollection):
    datacollection.send_updated_measurement(temperature=25.0, destination="datacollector")
    datacollection.confirm_update(temperature=25.0, source="datacollector")