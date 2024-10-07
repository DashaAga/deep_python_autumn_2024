import unittest
from unittest.mock import patch
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

        mock_logging.assert_any_call(
            'Run "%s" with positional args = %s, keyword kwargs = %s, attempt = %d',
            'test_function', (4, 2), {}, 1
        )
        mock_logging.assert_any_call('Attempt %d result = %s', 1, 6)

    @patch('logging.info')
    def test_successful_with_kwargs(self, mock_logging):
        @retry_deco(3)
        def divide(a, b=1):
            return a / b

        result = divide(a=10, b=2)
        self.assertEqual(result, 5)

        log_calls = list(mock_logging.call_args_list)

        self.assertIn('Run "%s" with positional args = %s, keyword kwargs = %s, attempt = %d', log_calls[0][0])
        self.assertEqual(log_calls[0][0][1], 'divide')
        self.assertEqual(log_calls[0][0][2], (10,))
        self.assertEqual(log_calls[0][0][3], {'b': 2})
        self.assertEqual(log_calls[0][0][4], 1)
        self.assertIn('Attempt %d result = %s', log_calls[1][0])
        self.assertEqual(log_calls[1][0][1], 1)
        self.assertEqual(log_calls[1][0][2], 5.0)


if __name__ == '__main__':
    unittest.main()
