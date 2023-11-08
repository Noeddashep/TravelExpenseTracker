import unittest
from unittest import TestCase
from src.manage_expenses import sum_expenses, get_cost_of_expenses, expenses_correction
from unittest.mock import patch


class TestGetCostExpenses(TestCase):

    # Checks if it returns the correct list even by inserting invalid inputs
    @patch('builtins.input', side_effect=['0', '5', '15.8', '-2', '2.55', '12,22', '22', '13$', '13'])
    def test_ok_get_cost_expenses(self, mock_input):
        result = get_cost_of_expenses(2, 50)
        self.assertEqual(result, [5, 15.8, 2.55, 12.22, 22, 13])


class TestExpensesCorrection(TestCase):

    # Check if it returns the correct list by eliminating the expenses entered the last day
    @patch('builtins.input', side_effect=['y', 'ye', 'ok', 'YES', '1', '20', '15', '12.5', 'no', ''])
    def test_yes_delete_last_day(self, mock_input):
        expenses = [10, 11, 12, 13, 14, 15]

        result = expenses_correction(expenses, 50)
        self.assertEqual(result, [10, 11, 12, 20, 15, 12.5])

    # Check if return the correct list by deleting all the expenses
    @patch('builtins.input', side_effect=['yes', '2', '2', '500', '10', '11', '12', '13', '14', '15', ''])
    def test_yes_delete_all_expenses(self, mock_input):
        expenses = [10, 11, 12, 20, 15, 12.5]

        result = expenses_correction(expenses, 50)
        self.assertEqual(result, [10, 11, 12, 13, 14, 15])

    # Check if return the list uncharged when you want to exit the program after "yes"
    @patch('builtins.input', side_effect=['yes', '', 'no', '0', '3'])
    def test_yes_quit_program(self, mock_input):
        expenses = [1, 2, 3, 4, 5, 6]

        result = expenses_correction(expenses, 50)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    # Check if return the list uncharged when you want to exit the program
    @patch('builtins.input', side_effect=['n', 'no', 'quit', '0', ''])
    def test_no_quit_program(self, mock_input):
        expenses = [1, 2, 3, 4, 5, 6]

        result = expenses_correction(expenses, 50)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])


class TestSumExpenses(TestCase):

    # Check if the sum of the list is correct
    def test_list(self):
        expenses = [20, 10, 15.5, 12.88, 5, 2.5]
        result = sum_expenses(expenses)
        self.assertEqual(result, 65.88)


if __name__ == '__main__':
    unittest.main()
