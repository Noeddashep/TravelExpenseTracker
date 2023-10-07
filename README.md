# TravelExpenseTracker
TravelExpenseTracker is a Python app for managing travel expenses. Track your daily spending in categories like meals, transportation and accommodation. You will have the opportunity to correct any errors and it will inform you if you stick to your budget.
# How does the travel expense tracker work?
Here is an explanation of the project and its functions:
- get_travel_information:
This function obtains travel information, including the number of travel days and the total budget. The user is required to input the number of days, which will be stored in the "travel_days" variable. The user will input the available budget as the second input, which will be stored in the "total_budget" variable. The function ensures that user inputs are valid, returning the travel days and total budget as integers.
- get_expense:
This function gets an expense for a specific category and a specific day of the trip. It takes the expense type as the first parameter and the day's number related to that expense as the second parameter. The user will input the cost in numeric format for that specific category, which will be stored in the "expense" variable. The function handles the possibility of the user entering incorrect input. The function returns the expense for that specific category.
- get_cost_of_expenses:
This function, which takes the number of days as its only argument, iterates for each expense category (meal, transport, accommodation) for each day of the trip, adding the corresponding expenses to the list_expenses list, which will be returned at the end of the function.
- exception_handling:
This function allows the user to correct expenses entered incorrectly. As long as the user enters "yes" as the first input, they can choose from 3 options by entering a number from 1 to 3. If the user enters 1, they have the option to delete the expenses for the last day by re-entering expenses for meal, transport, and accommodation. If the user enters 2, all entered expenses will be deleted, allowing the user to start over. If the user enters 3 or another type of input, they will exit the loop. Ultimately, the function returns the corrected new list.
- add_up_all_the_expenses:
This function sums all the expenses from the list provided as its only argument.
- results_display:
Returns a table summarizing the total expenses for different categories and the overall total expenses.
- budget_check:
Returns a string informing the user whether their budget has been respected.
- main:
Main function to run the travel expense management program. Calls various functions to obtain, manage, and display travel expenses.
