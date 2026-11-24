# BUDGET CHECKER PROJECT v2


# Asking for the budget (a number)
spending_budget = float(input("What's your budget? "))

# Asking how many expenses
num_expenses = int(input("How many expenses? "))

# Loop for expenses
amount_spent = 0

for expense in range(num_expenses):
    cost = float(input("Expense amount: "))
    amount_spent += cost

# Outcomes for under/over budget and 0 diff
if spending_budget > amount_spent:
    budget_difference = spending_budget - amount_spent
    print("Under budget by $" + str(round(budget_difference, 2)))
elif spending_budget < amount_spent:
    budget_difference = amount_spent - spending_budget
    print("Over budget by $" + str(round(budget_difference, 2)))
else: 
    print("Right on budget!")

 