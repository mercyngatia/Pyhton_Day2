print ("Welcome to the Calculator App!")  # Corrected to use print function
print ("This app will help you perform basic arithmetic operations.  Please enter two numbers.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose an operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == '/':
    if num2 != 0:   #don't allow division by zero
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from +, -, *, or /.")
print("Thank you for using the Calculator App! Goodbye!")


