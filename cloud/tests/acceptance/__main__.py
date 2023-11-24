import sys
import unittest

def at_least_one_test_failed(test_result):
    return not test_result.wasSuccessful()

def no_tests_run(test_result):
    return test_result.testsRun == 0

def main():
    acceptance_tests = unittest.TestLoader().discover('tests.acceptance', pattern='*acceptance_tests*')
    test_result = unittest.TextTestRunner(verbosity=2).run(acceptance_tests)
    sys.exit(at_least_one_test_failed(test_result) or no_tests_run(test_result))

main()