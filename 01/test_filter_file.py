import unittest
from io import StringIO
from filter_file import filter_file

class TestFilterFile(unittest.TestCase):
    
    def setUp(self):

        self.file_content = (
            "Белеет парус одинокий\n"
            "В тумане моря голубом\n"
            "Что ищет он в стране далекой\n"
            "Что кинул он в краю родном\n"
            "Играют волны ветер свищет\n"
            "И мачта гнется и гнется\n"
            "Увы он счастия не ищет\n"
            "И не от счастия бежит и бежит\n"
        )
        self.file_obj = StringIO(self.file_content)
    
    def test_filter(self):

        search_words = ["гнется", "бежит"]
        stop_words = ["счастия"]

        expected_lines = [
            "И мачта гнется и гнется"
        ]
        
        result_lines = list(filter_file(self.file_obj, search_words, stop_words))
        
        self.assertEqual(result_lines, expected_lines)

    def test_stop_word(self):
        
        search_words = ["голубом"]
        stop_words = ["моря"]
        
        result_lines = list(filter_file(self.file_obj, search_words, stop_words))
        self.assertNotIn("В тумане моря голубом", result_lines)

    def test_empty(self):

        result_lines = list(filter_file(self.file_obj, [], []))
        self.assertEqual(result_lines, [])

    def test_empty_search(self):

        stop_words = ["моря"]

        result_lines = list(filter_file(self.file_obj, [], stop_words))
        self.assertEqual(result_lines, [])

    def test_empty_stop_words(self):

        search_words = ["он"]

        expected_lines = [
            "Что ищет он в стране далекой",
            "Что кинул он в краю родном",
            "Увы он счастия не ищет"
        ]
        
        result_lines = list(filter_file(self.file_obj, search_words, []))
        self.assertEqual(result_lines, expected_lines)
    
    def test_upper_case(self):

        search_words = ["КРАю"]

        expected_lines = [
            "Что кинул он в краю родном"
        ]
        
        result_lines = list(filter_file(self.file_obj, search_words, []))
        self.assertEqual(result_lines, expected_lines)

if __name__ == '__main__':
    unittest.main()