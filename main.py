def get_travel_information():
    #Acquires travel information from the user.

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

def get_expense(day, kind_of_expense):
    #Obtains daily expenses for a specific category.

    expense = input(f'Enter {kind_of_expense} expenses in $ for day {day}: ')
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

def get_cost_of_expenses(days):
    #Registers daily expenses for the entire trip.

    list_expenses = []

    for day in range(1, days + 1):
        list_expenses.append(get_expense(day, 'meal'))
        list_expenses.append(get_expense(day, 'transport'))
        list_expenses.append(get_expense(day, 'accommodation'))

    return list_expenses

def exception_handling(list_expenses):
    #Handles correction of expense entries based on user input.

    question = input('do you want to correct something? (yes or no)\n').lower()
    new_list = list_expenses.copy()
    while question == 'yes':
        print('Choose from the possible options:\n \
                        1. "delete the last day of expense";\n \
                        2. "delete all the expenses";\n \
                        3. "cancel"')
        user_choice = int(input('Enter a number:\n'))

        if user_choice == 1:
            print(f'Enter the correct expense for each category on the last day:')
            if new_list:
                for number in range(3):
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

def add_up_all_the_expenses(expenses):
    #Calculates the total expenses for the entire trip.

    total_expenses = 0
    for expense in expenses:
        total_expenses += expense
    return total_expenses

def results_display(total_meal_expenses, total_transport_expenses, total_accomodation_expenses, total_expenses):
    #Displays a summary of travel expenses.

    return '\n'\
           'Here the summary of travel expenses:\n'\
           '|    meal    |    transport    |    accomodation    |    total expenses    |\n'\
           '----------------------------------------------------------------------------\n'\
           f'|      {total_meal_expenses}    |         {total_transport_expenses}      |      {total_accomodation_expenses}            |      {total_expenses}              |\n'

def budget_check(total_budget, total_expenses):
    #Checks if the initial budget covers all expenses

    final_budget = total_budget - total_expenses

    if final_budget >= 0:
        return f"Your initial budget covered all expenses. Here's your final budget: $""{:.2f}".format(final_budget)
    else:
        return f"Your initial budget didn't cover all expenses. Here's your final budget: $""{:.2f}".format(final_budget)

def main():
    """
    Main function to run the travel expense management program.
    Calls various functions to obtain, manage, and display travel expenses.
    """

    travel_day = get_travel_information()
    list_expenses = get_cost_of_expenses(travel_day[0])
    handling_expenses = exception_handling(list_expenses)
    total_meal_expenses = sum(handling_expenses[::3])
    total_transport_expenses = sum(handling_expenses[1::3])
    total_accomodation_expenses = sum(handling_expenses[2::3])
    total_expenses = add_up_all_the_expenses(handling_expenses)
    display_expenses = results_display(total_meal_expenses, total_transport_expenses, total_accomodation_expenses, total_expenses)
    check_budget = budget_check(travel_day[1], total_expenses)

    print(display_expenses)
    print(check_budget)

if __name__ == '__main__':
    main()