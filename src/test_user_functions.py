import unittest
from unittest import TestCase
from unittest.mock import patch
from src.user_functions import get_travel_information, get_expense


class TestTravelInfo(TestCase):

    # Check if it returns the correct value with valid inputs
    @patch('builtins.input', side_effect=['5', '1500.8'])
    def test_valid_info(self, mock_input):
        result = get_travel_information()
        self.assertEqual(result, (5, 1500.8))


    """
        Check if it handles invalid input in the "days" parameter such as: 
        a string, a float with a decimal point, a negative value, and zero
    """
    @patch('builtins.input', side_effect=['5,2', '5 days', '0', '-2', '10', '1000.50'])
    def test_invalid_input_days(self, mock_input):
        result = get_travel_information()
        self.assertEqual(result, (10, 1000.5))


    """
        Check if it handles invalid input in the "days" parameter such as: 
        a string, a float with a decimal point, a negative value, and zero
    """
    @patch('builtins.input', side_effect=['10', '5 days', '0', '-2', '1000,50'])
    def test_invalid_input_budget(self, mock_input):
        result = get_travel_information()
        self.assertEqual(result, (10, 1000.5))


class TestGetExpense(TestCase):

    # Check if it returns the correct value with valid inputs
    def test_ok_expense(self):
        with patch('builtins.input', return_value="50.88"):
            result = get_expense(1, 'meal')
            self.assertEqual(result, 50.88)

    """
        Check if it handles invalid input in the "days" parameter such as: 
        a string, a float with a decimal point, a negative value, and zero
    """
    @patch('builtins.input', side_effect=['five', '-5', '0', '50,5'])
    def test_invalid_input_expense(self, mock_input):
        result = get_expense(1, 'meal')
        self.assertEqual(result, 50.5)


if __name__ == '__main__':
    unittest.main()


