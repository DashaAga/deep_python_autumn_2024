import unittest
import logging
from unittest.mock import patch
logging.basicConfig(level=logging.INFO)

from retry_deco import retry_deco


class TestRetryDecorator(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)

    @patch('logging.info')
    def test_retry_successful_execution(self, mock_log):
        """Тестирует успешное выполнение функции с первой попытки."""
        @retry_deco(retries=3)
        def sample_func(x, y):
            return x + y

        result = sample_func(2, 3)
        self.assertEqual(result, 5)
        self.assertEqual(mock_log.call_count, 2)

    @patch('logging.info')
    def test_retry_fails_and_succeeds(self, mock_log):
        """Тестирует, что функция падает один раз и успешно выполняется при повторе."""
        attempts = []

        @retry_deco(retries=3)
        def sample_func(x):
            if len(attempts) < 1:
                attempts.append(1)
                raise RuntimeError("Test error")
            return x

        result = sample_func(5)
        self.assertEqual(result, 5)
        self.assertEqual(mock_log.call_count, 4)

    @patch('logging.info')
    def test_retry_exceeds_attempts(self, mock_log):
        """Тестирует, что после превышения попыток бросается исключение."""
        @retry_deco(retries=3)
        def sample_func():
            raise RuntimeError("Test error")

        with self.assertRaises(RuntimeError):
            sample_func()

        self.assertEqual(mock_log.call_count, 6)

    @patch('logging.info')
    def test_retry_with_ignored_exceptions(self, mock_log):
        """Тестирует, что игнорируемое исключение сразу бросается."""
        @retry_deco(retries=3, ignored_exceptions=(ValueError,))
        def sample_func():
            raise ValueError("Ignored exception")

        with self.assertRaises(ValueError):
            sample_func()

        self.assertEqual(mock_log.call_count, 2)

if __name__ == '__main__':
    unittest.main()
