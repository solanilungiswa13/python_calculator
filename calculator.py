# Get user inputs 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
operation = input("Enter the operation (+, -, *, /): ") 
# Perform the operation 
if operation == "+": 
    result = num1 + num2 
elif operation == "-": 
    result = num1 - num2 
elif operation == "*": 
    result = num1 * num2 
elif operation == "/": 
    if num2 == 0: 
        result = "Division by zero is not allowed." 
    else: 
        result = num1 / num2 
else: result = "Invalid operation." 
# Print the result 
print(f"{num1} {operation} {num2} = {result}")