"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def sanitized_number(user_input: str):
    try:
        return float(user_input)
    except ValueError:
        return None

def main():
    
    print(f"===== Simple Calculator =====")
    while True:
        raw_val = input("Enter the first number: ")
        num1 = sanitized_number(raw_val) # Pass the string to the function
        if num1 is not None:
            break # Exit loop if we got a valid number
        print("Invalid input. Please enter a number.")

    # For Num 2
    while True:
        raw_val = input("Enter the second number: ")
        num2 = sanitized_number(raw_val)
        if num2 is not None:
            break
        print("Invalid input. Please enter a number.")

    # Ask the user for sample input    
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()

