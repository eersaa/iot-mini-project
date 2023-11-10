def test_should_return_one_temperature_datapoint():
    goto.dashboard()
    dashboard.open("temperatures")
    assert len(dashboard.temperatures) == 1