# CALCULATOR PROJECT V1

first_num = 0
second_num = 0


# Ask for first/second numbers and operator
first_num = float(input("First number: "))
operator = input("Operator: ")
second_num = float(input("Second number: "))
if operator == "+":
    result = first_num + second_num
elif operator == "-":
    result = first_num - second_num
elif operator == "*":
    result = first_num * second_num
elif operator == "/":
    result = first_num / second_num
else: 
    result = "Invalid (not an operator)."


# Print final result
print("Your answer is " + str(result))

