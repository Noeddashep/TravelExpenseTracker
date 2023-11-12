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