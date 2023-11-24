import unittest
import sys

from tests.util.unittest_helpers import at_least_one_test_failed, no_tests_run

if __name__ == '__main__':
    tests = unittest.TestLoader().discover('tests.unit', pattern='*_tests*')
    test_result = unittest.TextTestRunner().run(tests)
    sys.exit(at_least_one_test_failed(test_result) or no_tests_run(test_result))