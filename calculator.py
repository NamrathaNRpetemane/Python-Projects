def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    # Handle division by zero
    if n2 == 0:
        return "Error! Division by zero is not allowed."
    return n1 / n2

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

def calculator():
    while True:  # Main loop to handle calculator restart
        num1 = float(input("Enter the first number: "))

        while True:  # Inner loop to handle continuation with the current result
            # Display available operations
            print("Available operations:")
            for symbol in operations:
                print(symbol)
            
            choose_input = input("Enter the operation: ")
            if choose_input not in operations:
                print("Invalid operation. Please try again.")
                continue

            num2 = float(input("Enter the second number: "))
            result = operations[choose_input](num1, num2)
            print(f"Result: {num1} {choose_input} {num2} = {result}")

            should_continue = input(f"Type 'y' to continue with {result}, or 'n' to start a new operation, or 'exit' to quit: ").lower()
            if should_continue == 'y':
                if isinstance(result, (int, float)):
                    num1 = result  # Continue with the current result
                else:
                    print("Cannot continue with an invalid result.")
                    break
            elif should_continue == 'n':
                break  # Break the inner loop and start a new calculation
            elif should_continue == 'exit':
                print("Goodbye!")
                return  # Exit the calculator
            else:
                print("Invalid input. Exiting.")
                return

calculator()









