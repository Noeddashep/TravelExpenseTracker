from typing import List
def get_travel_information() -> tuple[int, float]:
    """
    Acquires travel information from the user.

    This function obtains travel information, including the number of travel days and the total budget.
    The user is required to input the number of days, which will be stored in the "travel_days" variable.
    The user will input the available budget as the second input, which will be stored in the "total_budget" variable.
    The function ensures that user inputs are valid, returning the travel days and total budget as integers.
    """


    travel_days = input('Enter the total number of days for the trip:\n')
    while not travel_days.isnumeric():
        print('Only numeric characters are accepted!')
        travel_days = input('Enter the total days for the trip:\n')

    total_budget = input('Enter the total budget available in $ for the trip:\n')
    total_budget = total_budget.replace(',', '.')
    while True:
        try:
            total_budget = float(total_budget)
            break
        except ValueError:
            print('Only numeric characters are accepted!')
            total_budget = input('Enter the total budget available in $ for the trip:\n')
            total_budget = total_budget.replace(',', '.')

    travel_days = int(travel_days)
    total_budget = float(total_budget)
    print(f"Great! Your trip will last {travel_days} days with an initial budget of ${total_budget:.2f}")

    return travel_days, total_budget

def get_expense(day: int, kind_of_expense: str) -> float:
    """
    This function gets an expense for a certain category and a specific day of the trip.
    It takes the number of the day relating to the expense as the first parameter and the type of expense as the second parameter.
    The user will enter the cost in numerical format which will be stored in the "expense" variable.
    The function handles the possibility of the user entering incorrect inputs and returns the expense for that specific category.
    """

    expense: str = input(f'Enter {kind_of_expense} expenses in $ for day {day}: ')
    expense = expense.replace(',', '.')
    while True:
        try:
            expense = float(expense)
            break
        except ValueError:
            print('Only numeric characters are accepted!')
            expense = input(f'Enter {kind_of_expense} expenses in $ for day {day}: ')
            expense = expense.replace(',', '.')

    return expense

def get_cost_of_expenses(days: int) -> List[float]:
    """
    Registers daily expenses for the entire trip.

    This function, which takes the number of days as its only argument, iterates for each expense category (meal, transport, accommodation)
    for each day of the trip, adding the corresponding expenses to the list_expenses list, which will be returned at the end of the function.
    """

    list_expenses = []

    for day in range(1, days + 1):
        list_expenses.append(get_expense(day, 'meal'))
        list_expenses.append(get_expense(day, 'transport'))
        list_expenses.append(get_expense(day, 'accommodation'))

    return list_expenses

def exception_handling(list_expenses: List[float]) -> List[float]:
    """
    This function allows the user to correct expenses entered incorrectly.
    As long as the user enters "yes" as the first input, they can choose from 3 options by entering a number from 1 to 3:
        - If the user enters 1, they have the option to delete the expenses for the last day by re-entering expenses for meal, transport, and accommodation.
        - If the user enters 2, all entered expenses will be deleted, allowing the user to start over.
        - If the user enters 3 or another type of input, they will exit the loop.
    Ultimately, the function returns the corrected new list.
    """

    question: str = input('do you want to correct something? (yes or no)\n').lower()
    new_list: List[float] = list_expenses.copy()
    while question == 'yes':
        print('Choose from the possible options:\n \
                        1. "delete the last day of expense";\n \
                        2. "delete all the expenses";\n \
                        3. "cancel"')
        user_choice: int = int(input('Enter a number:\n'))

        if user_choice == 1:
            print(f'Enter the correct expense for each category on the last day:')
            if new_list:
                for number in range(3): #For loop allows to delete the last three expenses from the list, which correspond to the last day of the trip
                    del new_list[-1]
            else:
                print("The expense list is already empty.")

        elif user_choice == 2:
            print(f'Enter the correct expense for each category:')
            new_list = []

        elif user_choice == 3:
            return list_expenses

        new_list.extend(get_cost_of_expenses(1))
        question = input('do you want to correct something? (yes or no)\n').lower()

    return new_list

def add_up_all_the_expenses(expenses: List[float]) -> float:
    """
    This function sums all the expenses from the list provided as its only argument.
    """

    total_expenses = 0
    for expense in expenses:
        total_expenses += expense
    return total_expenses

def results_display(total_meal_expenses: float, total_transport_expenses: float, total_accomodation_expenses: float, total_expenses: int) -> str:
    """
    Displays a summary of travel expenses.
    Returns a table summarizing the total expenses for different categories and the overall total expenses.
    """

    return '\n'\
           'Here the summary of travel expenses:\n'\
           '|    meal    |    transport    |    accomodation    |    total expenses    |\n'\
           '----------------------------------------------------------------------------\n'\
           f'|      {total_meal_expenses}    |         {total_transport_expenses}      |      {total_accomodation_expenses}            |      {total_expenses}              |\n'

def budget_check(total_budget: float, total_expenses:int) -> str:
    """
    Checks if the initial budget covers all expenses
    """
    
    final_budget: int = total_budget - total_expenses

    if final_budget >= 0:
        return f"Your initial budget covered all expenses. Here's your final budget: $""{:.2f}".format(final_budget)
    else:
        return f"Your initial budget didn't cover all expenses. Here's your final budget: $""{:.2f}".format(final_budget)


def main():
    """
    Main function to run the travel expense management program.
    Calls various functions to obtain, manage, and display travel expenses.
    """
    
    # Get trip information from user
    travel_day: tuple[int, float] = get_travel_information()

    # Record expenses for meals, transportation and accommodations for each day of the trip
    list_expenses: List[float] = get_cost_of_expenses(travel_day[0])

    # Manages any exceptions or corrections in the expenses entered
    handling_expenses: List[float] = exception_handling(list_expenses)

    # Calculate the total expenses for meals, transportation and accommodation separately
    total_meal_expenses: float = sum(handling_expenses[::3]) # This slice selects every third item in the list (which corresponds to each day's meal expenses)
    total_transport_expenses: float = sum(handling_expenses[1::3]) # This slice selects every third item starting from the second item in the list (which corresponds to each day's transportation expenses).
    total_accomodation_expenses: float = sum(handling_expenses[2::3]) # This slice selects every third item starting from the third item in the list (which corresponds to each day's accommodation expenses).

    # Calculate the total of the overall expenses
    total_expenses: float = add_up_all_the_expenses(handling_expenses)

    # View a summary of your travel expenses
    display_expenses: str = results_display(total_meal_expenses, total_transport_expenses, total_accomodation_expenses, total_expenses)

    # Checks whether the initial budget covers all expenses and returns an appropriate message
    check_budget: str = budget_check(travel_day[1], total_expenses)

    # Print the results
    print(display_expenses)
    print(check_budget)

if __name__ == '__main__':
    main()
