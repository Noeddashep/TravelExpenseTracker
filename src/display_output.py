def results_display(total_meal_expenses: float, total_transport_expenses: float, total_accommodation_expenses: float,
                    total_expenses: int) -> str:
    """
    Displays a summary of travel expenses.

    param total_meal_expenses: The total meal expenses
    param total_transport_expenses: The total transport expenses
    param total_accommodation_expenses: The total accommodation expenses

    return: A table summarizing the total expenses for different categories and the overall total expenses.
    """

    return '\n' \
           'Here the summary of travel expenses:\n' \
           '|    meal    |    transport    |    accomodation    |    total expenses    |\n' \
           '----------------------------------------------------------------------------\n' \
           f'|      {total_meal_expenses}    |         {total_transport_expenses}      |      {total_accommodation_expenses}            |      {total_expenses}              |\n'


def budget_check(total_budget: float, total_expenses: int) -> str:
    """
    Checks if the initial budget covers all expenses

    param total_budget: The user's initial budget
    param total_expenses: The total expenses

    return: A string that informs the user whether the initial budget was met or not.
    """

    final_budget = total_budget - total_expenses

    if final_budget >= 0:
        return f"Your initial budget covered all expenses. Here's your final budget: $""{:.2f}".format(final_budget)
    else:
        return f"Your initial budget didn't cover all expenses. Here's your final budget: $""{:.2f}".format(
            final_budget)