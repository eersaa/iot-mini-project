# I think better place for this acceptance test is inside the Datacollector domain.
# This is because Grafana will most likely interface directly with database.
# Datacollector is the domain that is responsible for storing data to database.

# test for UI
# should_display_requested_data_from_database