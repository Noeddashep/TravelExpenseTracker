from src.user_functions import get_travel_information
from src.manage_expenses import get_cost_of_expenses, exception_handling, sum_expenses
from src.display_output import results_display, budget_check
from typing import List

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
    total_meal_expenses: float = sum(handling_expenses[::3])  # This slice selects every third item in the list (which corresponds to each day's meal expenses)
    total_transport_expenses: float = sum(handling_expenses[1::3])  # This slice selects every third item starting from the second item in the list (which corresponds to each day's transportation expenses).
    total_accomodation_expenses: float = sum(handling_expenses[2::3])  # This slice selects every third item starting from the third item in the list (which corresponds to each day's accommodation expenses).

    # Calculate the total of the overall expenses
    total_expenses: float = sum_expenses(handling_expenses)

    # View a summary of your travel expenses
    display_expenses: str = results_display(total_meal_expenses, total_transport_expenses, total_accomodation_expenses,
                                            total_expenses)

    # Checks whether the initial budget covers all expenses and returns an appropriate message
    check_budget: str = budget_check(travel_day[1], total_expenses)

    # Print the results
    print(display_expenses)
    print(check_budget)


if __name__ == '__main__':
    main()
