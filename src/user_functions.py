def get_travel_information() -> tuple[int, float]:
    """
    Acquires travel information from the user.

    This function obtains travel information, including the number of travel days and the total budget.
    The user is required to input the number of days, which will be stored in the "travel_days" variable.
    The user will input the available budget as the second input, which will be stored in the "total_budget" variable.
    The function ensures that user inputs are valid.

    return: A tuple containing the travel days (int) and the total budget (float).
    """

    travel_days = input('Enter the total number of days for the trip:\n')
    while travel_days:
        try:
            travel_days = int(travel_days)
            if travel_days > 0:
                break
            else:
                print('You must enter a value greater than zero!')
                travel_days = input('Enter the total days for the trip:\n')
        except ValueError:
            print('Only integers are accepted!')
            travel_days = input('Enter the total days for the trip:\n')


    total_budget = input('Enter the total budget available in $ for the trip:\n').replace(',', '.')
    while total_budget:
        try:
            total_budget = float(total_budget)
            if total_budget > 0:
                break
            else:
                print('You must enter a value greater than zero!')
                total_budget = input('Enter the total days for the trip:\n').replace(',', '.')
        except ValueError:
            print('Only numeric characters are accepted!')
            total_budget = input('Enter the total budget available in $ for the trip:\n').replace(',', '.')

    print(f"Great! Your trip will last {travel_days} days with an initial budget of ${total_budget:.2f}")

    return travel_days, total_budget


def get_expense(day: int, kind_of_expense: str) -> float:
    """
    Returns an expense for a specific category and a particular day of the trip and handles
    the possibility of the user entering incorrect inputs.

    param day: The number of days relating to the expense.
    param kind_of_expense: The type of expense.

    return: The expense for the specific category and day.
    """

    expense = input(f'Enter {kind_of_expense} expenses in $ for day {day}: ').replace(',', '.')

    while expense:
        try:
            expense = float(expense)
            if expense > 0:
                break
            else:
                print('You must enter a value greater than zero!')
                expense = input(f'Enter {kind_of_expense} expenses in $ for day {day}: ').replace(',', '.')
        except ValueError:
            print("Only numeric characters are accepted!")
            expense = input(f'Enter {kind_of_expense} expenses in $ for day {day}: ').replace(',', '.')

    return expense
