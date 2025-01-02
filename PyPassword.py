import random  # Importing the random module for random operations

# Function to generate a random password
def generate_password():
    # Defining character pools for the password
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # All uppercase and lowercase letters
    numbers = '0123456789'  # Digits 0-9
    symbols = '!#$%&()*+'  # Special characters

  
    print("Welcome to Python Password Generator!")
    
    # Getting user input for the number of each type of character
    try:
        nr_alpha = int(input("How many letters would you prefer to add in password? "))  
        nr_num = int(input("How many numbers would you prefer to add in password? "))    
        nr_symb = int(input("How many symbols would you like to add in password? "))     
    except ValueError:  # Catch invalid inputs
        print("Please enter valid numbers.")  # Display error message if input is not an integer
        return 

    # Check if any input is negative
    if nr_alpha < 0 or nr_num < 0 or nr_symb < 0:
        print("Negative values are not allowed.") 
        return 

    # Generate a list of random characters based on user inputs
    password_list = (
        random.choices(letters, k=nr_alpha) +  # Select `nr_alpha` random letters
        random.choices(numbers, k=nr_num) +   # Select `nr_num` random numbers
        random.choices(symbols, k=nr_symb)    # Select `nr_symb` random symbols
    )

    # Shuffle the list to randomize character order
    random.shuffle(password_list)

    # Combine the shuffled list into a single string
    password = ''.join(password_list)

    # Display the generated password
    print(f"Your generated password is: {password}")

# Call the function to execute the password generator
generate_password()
