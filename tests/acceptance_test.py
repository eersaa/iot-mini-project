import unittest
import iot_system_dsl

class IotSystemCoapApiAcceptanceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.iot_node = iot_system_dsl.IoTNode()
        self.iot_system = iot_system_dsl.IoTSystem(self.iot_node)

    def test_should_successfully_show_one_sample_to_user_sent_from_iot_node(self):
        self.iot_system.iot_node.send_measurement_sample(type="temperature", value="25.0")
        self.confirm_showed_sample(self.iot_system.show_measurement_sample(type="temperature"), value="25.0")

    def confirm_showed_sample(self, sample, value):
        self.assertEqual(sample == value)