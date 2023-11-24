import unittest
import sys
import iot_system_dsl
import coap_api_protocol_driver

class IotSystemCoapApiAcceptanceTest(unittest.TestCase):
    def setUp(self):
        self.protocol_driver = coap_api_protocol_driver.CoapApiProtocolDriver()
        self.iot_node = iot_system_dsl.IotNodeDsl(self.protocol_driver)
        self.iot_system = iot_system_dsl.IotSystemDsl(self.protocol_driver, self.iot_node)

    def test_should_successfully_show_one_sample_to_user_sent_from_iot_node(self):
        self.iot_system.iot_node.send_measurement_sample(type="temperature", value="25.0")
        self.confirm_showed_sample(self.iot_system.show_measurement_sample(type="temperature"), value="25.0")

    def confirm_showed_sample(self, sample, value):
        self.assertEqual(sample, value)

def at_least_one_test_failed(test_result):
    return not test_result.wasSuccessful()

def no_tests_run(test_result):
    return test_result.testsRun == 0

if __name__ == '__main__':
    acceptance_tests = unittest.TestLoader().discover('.', pattern='acceptance_tests*')
    test_result = unittest.TextTestRunner(verbosity=2).run(acceptance_tests)
    sys.exit(at_least_one_test_failed(test_result) or no_tests_run(test_result))