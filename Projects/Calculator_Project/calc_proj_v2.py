# CALCULATOR PROJECT V2


quit_answer = ""

# Ask for first/second numbers and operator
while quit_answer != "q":
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
    print("Your answer is " + str(result))

    quit_answer = input("Type q to quit, or press Enter to keep going: ")



