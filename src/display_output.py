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

