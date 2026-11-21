# BUDGET CHECKER PROJECT


# Ask for the budget (a number)
spending_budget = float(input("What's your budget? "))

# Ask for the amount spent (a number)
amount_spent = float(input("How much have you spent? "))

# Outcomes for under/over budget and 0 diff
if spending_budget > amount_spent:
    budget_difference = spending_budget - amount_spent
    print("Under budget by $" + str(round(budget_difference, 2)))
elif spending_budget < amount_spent:
    budget_difference = amount_spent - spending_budget
    print("Over budget by $" + str(round(budget_difference, 2)))
else: 
    print("Right on budget!")

 