from typing import List
from src.user_functions import get_expense, get_travel_information


def get_cost_of_expenses(days: int, budget: float) -> List[float]:
    """
    Registers daily expenses for the entire trip.

    param days: The number of days relating to the trip
    param budget: The user's initial budget

    return: A list containing the various expenses in the categories of meals, transport and accommodation.
    """

    list_expenses = []

    for day in range(1, days + 1):
        list_expenses.append(get_expense(day, 'meal'))
        if sum(list_expenses) > budget:
            print("Your budget won't cover your expenses!")
            list_expenses.pop()
            break
        list_expenses.append(get_expense(day, 'transport'))
        if sum(list_expenses) > budget:
            print("Your budget won't cover your expenses!")
            list_expenses.pop()
            break
        list_expenses.append(get_expense(day, 'accommodation'))
        if sum(list_expenses) > budget:
            print("Your budget won't cover your expenses!")
            list_expenses.pop()
            break

    return list_expenses


def expenses_correction(list_expenses: List[float], initial_budget: float) -> List[float]:
    """
    This function allows the user to correct expenses entered incorrectly.

    As long as the user enters "yes" as the first input, they can choose from 3 options by entering a number from 1 to 3:
        - If the user enters 1, they have the option to delete the expenses for the last day by re-entering expenses for meal, transport, and accommodation;
        - If the user enters 2, all entered expenses will be deleted, allowing the user to start over;
        - If the user enters 3 or another type of input, they will exit the loop.

    param list_expenses: A list containing the various expenses in the categories of meals, transport and accommodation.
    param initial_budget: The user's initial budget

    return: The new corrected list.
    """
    print('\nDo you want to correct something?\n')
    question = input('Type "yes" to go to expense correction, otherwise press enter to exit:\n').lower()
    new_list = list_expenses.copy()

    while question != 'yes' and question != '':
        question = input('Type "yes" to go to expense correction, otherwise press enter to exit:\n').lower()

    while question == 'yes':
        print('Choose from the possible options:\n \
                        1. "delete the last day of expense";\n \
                        2. "delete all the expenses";\n \
                        3. "cancel"')
        user_choice = input('Enter a number:\n')

        while user_choice not in ('1', '2', '3'):
            print('You must enter an integer value between 1 and 3!\n')
            print('Choose from the possible options:\n \
                                    1. "delete the last day of expense";\n \
                                    2. "delete all the expenses";\n \
                                    3. "cancel"')
            user_choice = input('Enter a number:\n')

        if user_choice == '1':
            print(f'Enter the correct expense for each category on the last day:')
            if new_list:

                # For loop allows to delete the last three expenses from the list, which correspond to the last day of the trip
                for number in range(3):
                    del new_list[-1]

                new_list.extend(get_cost_of_expenses(1, initial_budget))
            else:
                print("The expense list is already empty.")

        elif user_choice == '2':
            days, budget = get_travel_information()
            print(f'Enter the correct expense for each category:')
            new_list = []
            new_list.extend(get_cost_of_expenses(days, budget))

        elif user_choice == '3':
            return list_expenses

        print('\nDo you want to correct something?\n')
        question = input('Type "yes" to go to expense correction, otherwise press enter to exit:\n').lower()

        while question != 'yes' and question != '':
            question = input('Type "yes" to go to expense correction, otherwise press enter to exit:\n').lower()

    return new_list


def sum_expenses(expenses: List[float]) -> float:
    """
    This function adds all the expenses present in the list that contains the different expenses.

    param expenses: A list containing the various expenses in the categories of meals, transport and accommodation.

    return: The total expenses
    """

    total_expenses = 0
    for expense in expenses:
        total_expenses += expense
    return total_expenses
