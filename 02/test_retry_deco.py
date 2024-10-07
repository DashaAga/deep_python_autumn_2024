import unittest
from unittest.mock import patch, call
import logging
from retry_deco import retry_deco

@retry_deco(retries=3)
def test_function(a, b):
    return a + b

@retry_deco(retries=3)
def function_with_exception():
    raise ValueError("Test error")

@retry_deco(retries=2, ignored_exceptions=[ValueError])
def function_with_ignored_exception():
    raise ValueError("Test ignored error")

class TestRetryDeco(unittest.TestCase):
    @patch('logging.info')
    def test_successful_function(self, mock_logging):
        result = test_function(4, 2)
        self.assertEqual(result, 6)

        mock_logging.assert_any_call('Run "test_function" with positional args = (4, 2), keyword kwargs = {}, attempt = 1')
        mock_logging.assert_any_call('Attempt 1 result = 6')

    @patch('logging.info')
    def test_function_with_exception_retries(self, mock_logging):
        with self.assertRaises(ValueError):
            function_with_exception()

        self.assertEqual(mock_logging.call_count, 6)
        mock_logging.assert_any_call('Run "function_with_exception" with positional args = (), keyword kwargs = {}, attempt = 1')
        mock_logging.assert_any_call('Attempt 1 exception = ValueError: Test error')

    @patch('logging.info')
    def test_function_with_ignored_exception(self, mock_logging):
        with self.assertRaises(ValueError):
            function_with_ignored_exception()

        self.assertEqual(mock_logging.call_count, 2)
        mock_logging.assert_any_call('Run "function_with_ignored_exception" with positional args = (), keyword kwargs = {}, attempt = 1')
        mock_logging.assert_any_call('Attempt 1 exception = ValueError: Test ignored error')

    @patch('logging.info')
    def test_retry_on_exception(self, mock_logging):
        @retry_deco(3)
        def fail_function():
            raise RuntimeError('Test error')

        with self.assertRaises(RuntimeError):
            fail_function()

        self.assertEqual(mock_logging.call_count, 6)
        mock_logging.assert_any_call('Run "fail_function" with positional args = (), keyword kwargs = {}, attempt = 1')
        mock_logging.assert_any_call('Attempt 1 exception = RuntimeError: Test error')

    @patch('logging.info')
    def test_success_after_retry(self, mock_logging):
        attempts = [0]

        @retry_deco(3)
        def sometimes_fail():
            if attempts[0] < 2:
                attempts[0] += 1
                raise RuntimeError('Temporary error')
            return 'Success'

        result = sometimes_fail()
        self.assertEqual(result, 'Success')

        self.assertEqual(mock_logging.call_count, 6)
        mock_logging.assert_any_call('Run "sometimes_fail" with positional args = (), keyword kwargs = {}, attempt = 1')
        mock_logging.assert_any_call('Attempt 1 exception = RuntimeError: Temporary error')
        mock_logging.assert_any_call('Attempt 3 result = Success')

    @patch('logging.info')
    def test_successful_with_kwargs(self, mock_logging):
        @retry_deco(3)
        def divide(a, b=1):
            return a / b

        result = divide(a=10, b=2)
        self.assertEqual(result, 5)

        log_calls = [call for call in mock_logging.call_args_list]

        self.assertIn('Run "divide"', log_calls[0][0][0])
        self.assertIn('attempt = 1', log_calls[0][0][0])
        self.assertIn('Attempt 1 result = 5.0', log_calls[1][0][0])

if __name__ == '__main__':
    unittest.main()