import unittest
from unittest.mock import patch
from predict_message_mood import SomeModel, predict_message_mood

class TestPredictMessageMood(unittest.TestCase):

    @patch.object(SomeModel, 'predict')
    def test_predict_bad(self, mock_predict):
        mock_predict.return_value = 0.2
        result = predict_message_mood("Мне не нравится продукт")
        self.assertEqual(result, "неуд")

    @patch.object(SomeModel, 'predict')
    def test_predict_normal(self, mock_predict):
        mock_predict.return_value = 0.5
        result = predict_message_mood("Все прошло нормально")
        self.assertEqual(result, "норм")

    @patch.object(SomeModel, 'predict')
    def test_predict_good(self, mock_predict):
        mock_predict.return_value = 0.9
        result = predict_message_mood("Я очень рад, отличный результат")
        self.assertEqual(result, "отл")

    @patch.object(SomeModel, 'predict')
    def test_custom_thresholds_1(self, mock_predict):
        mock_predict.return_value = 0.85
        result = predict_message_mood("Сойдет", bad_thresholds=0.4, good_thresholds=0.9)
        self.assertEqual(result, "норм")
    
    @patch.object(SomeModel, 'predict')
    def test_custom_thresholds_2(self, mock_predict):
        mock_predict.return_value = 0
        result = predict_message_mood("Сойдет", bad_thresholds=0, good_thresholds=0.9)
        self.assertEqual(result, "норм")

    @patch.object(SomeModel, 'predict')
    def test_custom_thresholds_3(self, mock_predict):
        mock_predict.return_value = 1
        result = predict_message_mood("Сойдет", bad_thresholds=0, good_thresholds=1)
        self.assertEqual(result, "норм")

if __name__ == '__main__':
    unittest.main()