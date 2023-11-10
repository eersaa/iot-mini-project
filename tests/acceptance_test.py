def test_should_render_one_temperature_data():
    goto.dashboard()
    dashboard.open("temperature")
    dashboard.temperature.render()
    assert renderer.data.temperature[0] == 20