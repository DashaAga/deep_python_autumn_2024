import unittest
from unittest.mock import patch
from predict_message_mood import SomeModel, predict_message_mood


class TestPredictMessageMood(unittest.TestCase):

    @patch.object(SomeModel, 'predict')
    def test_predict_bad(self, mock_predict):
        mock_predict.return_value = 0.2
        message = "Мне не нравится продукт"
        result = predict_message_mood(message)
        self.assertEqual(result, "неуд")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_predict_normal(self, mock_predict):
        mock_predict.return_value = 0.5
        message = "Все прошло нормально"
        result = predict_message_mood(message)
        self.assertEqual(result, "норм")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_predict_good(self, mock_predict):
        mock_predict.return_value = 0.9
        message = "Я очень рад, отличный результат"
        result = predict_message_mood(message)
        self.assertEqual(result, "отл")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_custom_thresholds_1(self, mock_predict):
        mock_predict.return_value = 0.85
        message = "Сойдет"
        result = predict_message_mood(message,
                                      bad_thresholds=0.4, good_thresholds=0.9)
        self.assertEqual(result, "норм")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_custom_thresholds_2(self, mock_predict):
        mock_predict.return_value = 0
        message = "Сойдет"
        result = predict_message_mood(message,
                                      bad_thresholds=0, good_thresholds=0.9)
        self.assertEqual(result, "норм")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_custom_thresholds_3(self, mock_predict):
        mock_predict.return_value = 1
        message = "Сойдет"
        result = predict_message_mood(message,
                                      bad_thresholds=0, good_thresholds=1)
        self.assertEqual(result, "норм")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_predict_just_below_bad_threshold(self, mock_predict):
        mock_predict.return_value = 0.29
        message = "Текст"
        result = predict_message_mood(message, bad_thresholds=0.3)
        self.assertEqual(result, "неуд")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_predict_just_above_bad_threshold(self, mock_predict):
        mock_predict.return_value = 0.31
        message = "Текст"
        result = predict_message_mood(message, bad_thresholds=0.3)
        self.assertEqual(result, "норм")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_predict_just_below_good_threshold(self, mock_predict):
        mock_predict.return_value = 0.79
        message = "Текст"
        result = predict_message_mood(message, good_thresholds=0.8)
        self.assertEqual(result, "норм")
        mock_predict.assert_called_with(message)

    @patch.object(SomeModel, 'predict')
    def test_predict_just_above_good_threshold(self, mock_predict):
        mock_predict.return_value = 0.81
        message = "Текст"
        result = predict_message_mood(message, good_thresholds=0.8)
        self.assertEqual(result, "отл")
        mock_predict.assert_called_with(message)


if __name__ == '__main__':
    unittest.main()
