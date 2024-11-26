import math

def advanced_calculator():
    print("Welcome to the Advanced Calculator!")
    print("Supported operations: +, -, *, /, %, **, sqrt, exit")
    
    while True:
        try:
            # Take user input
            operation = input("Enter an operation (or 'exit' to quit): ").strip().lower()
            
            # Exit condition
            if operation == 'exit':
                print("Goodbye!")
                break
            
            # Special case for square root
            if operation == 'sqrt':
                num = float(input("Enter a number: "))
                if num < 0:
                    raise ValueError("Cannot calculate square root of a negative number!")
                print(f"The square root of {num} is {math.sqrt(num)}")
                continue
            
            # General case
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed!")
                result = num1 / num2
            elif operation == '%':
                result = num1 % num2
            elif operation == '**':
                result = num1 ** num2
            else:
                print("Invalid operation! Please try again.")
                continue
            
            print(f"The result of {num1} {operation} {num2} is: {result}")
        
        except ValueError as ve:
            print(f"Input error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Math error: {zde}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the calculator
advanced_calculator()
