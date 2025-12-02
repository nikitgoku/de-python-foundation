from loguru import logger

'''
Mini Exercise: Calculator with While Loop
---------------------------------
Write a Python function that acts as a simple calculator. The function should take two numbers and an
operator (+, -, *, /) as input and return the result of the operation. The function should continue to take
input until the user decides to get the result by entering the '=' operator.'
'''

def calculator(num1):
    # Ask the user for a operator
    operator_tuple = ('+', '-', '*', '/')
    # If at this point the user decides to get the result, we can store the result as num1
    result = num1

    operator = input("Please select the following operator: + - * / = ")

    while operator in operator_tuple:
        # Ask the user for the next number, if invalid input, ask again
        try:
            num2 = float(input("Please enter the next number: "))
        except ValueError:
            logger.error("Invalid input. Please enter a valid number.")
            continue
        
        # Perform the basic arithmetic operation using if/else/elif conditions
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '/':
                result = num1 / num2
            else:
                result = num1 * num2
        except ZeroDivisionError:       # Handle division by zero error
            logger.error("Division by zero is not allowed. Please enter a valid number.")
            continue

        operator = input("Please select the following operator: + - * / = ")
        num1 = result
    
    return result
    
while True:
    # Take the first number as input, if invalid input, ask again
    try: 
        num1 = float(input("Enter the first number: "))
        break
    except ValueError:
        logger.error("Invalid input. Please enter a valid number.")


logger.info(f"Result of the calculator is {calculator(num1)}")