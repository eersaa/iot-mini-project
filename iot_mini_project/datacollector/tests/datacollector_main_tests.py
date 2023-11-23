import unittest
import sys

def at_least_one_test_failed(test_result):
    return not test_result.wasSuccessful()

def no_tests_run(test_result):
    return test_result.testsRun == 0

if __name__ == '__main__':
    tests = unittest.TestLoader().discover('.', pattern='*_tests*')
    test_result = unittest.TextTestRunner().run(tests)
    sys.exit(at_least_one_test_failed(test_result) or no_tests_run(test_result))