import unittest
from unittest.mock import Mock
from process_json import process_json


class TestProcessJson(unittest.TestCase):

    def test_callback_called_with_matching_tokens(self):
        json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        required_keys = ["key1", "KEY2"]
        tokens = ["WORD1", "word2"]

        callback = Mock()

        process_json(json_str, required_keys, tokens, callback)

        callback.assert_any_call("key1", "WORD1")
        callback.assert_any_call("key1", "word2")
        self.assertEqual(callback.call_count, 2) 

    def test_no_callback_when_no_matching_tokens(self):
        json_str = '{"key1": "test", "key2": "Another test"}'
        required_keys = ["key1", "key2"]
        tokens = ["word1", "word2"]

        callback = Mock()

        process_json(json_str, required_keys, tokens, callback)

        callback.assert_not_called()

    def test_no_callback_when_no_matching_keys(self):
        json_str = '{"key1": "word1", "key2": "word2"}'
        required_keys = ["key3", "key4"]
        tokens = ["word1", "word2"]

        callback = Mock()

        process_json(json_str, required_keys, tokens, callback)

        callback.assert_not_called()

    def test_case_insensitive_token_search(self):
        json_str = '{"key1": "Word1 word2"}'
        required_keys = ["key1"]
        tokens = ["WORD1", "WORD2"]

        callback = Mock()

        process_json(json_str, required_keys, tokens, callback)

        callback.assert_any_call("key1", "WORD1")
        callback.assert_any_call("key1", "WORD2")
        self.assertEqual(callback.call_count, 2)

    def test_no_keys_provided(self):
        json_str = '{"key1": "word1", "key2": "word2"}'
        tokens = ["word1", "word2"]

        callback = Mock()

        process_json(json_str, None, tokens, callback)

        callback.assert_not_called()

    def test_no_tokens_provided(self):
        json_str = '{"key1": "word1", "key2": "word2"}'
        required_keys = ["key1", "key2"]

        callback = Mock()

        process_json(json_str, required_keys, None, callback)

        callback.assert_not_called()

if __name__ == '__main__':
    unittest.main()
