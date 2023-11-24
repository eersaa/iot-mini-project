import sys
import unittest

from tests.util.unittest_helpers import at_least_one_test_failed, no_tests_run

def main():
    acceptance_tests = unittest.TestLoader().discover('tests.acceptance', pattern='*_tests*')
    test_result = unittest.TextTestRunner(verbosity=2).run(acceptance_tests)
    sys.exit(at_least_one_test_failed(test_result) or no_tests_run(test_result))

main()