def at_least_one_test_failed(test_result):
    return not test_result.wasSuccessful()

def no_tests_run(test_result):
    return test_result.testsRun == 0