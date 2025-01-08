def find_highest_bidder(bidding_record):
    highest_amount = 0
    winner = ""

    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > highest_amount:
            highest_amount = amount
            winner = bidder
    print(f"The winner is {winner} with a bidding amount of ${highest_amount}")

bid = {}

continue_bidding = True
while continue_bidding:
    name = input("what is your name? ")
    amount = int(input("how much do you bid? "))
    bid[name] = amount

    should_continue = input("if anyone else to continue? type 'yes' or type 'no' ").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bid)
    elif should_continue == 'yes':
        print("\n" * 20)


# in efficient method (another code)


import os

def find_highest_bidder(bidding_record):
    highest_amount = 0
    winner = ""

    for bidder, amount in bidding_record.items():
        if amount > highest_amount:
            highest_amount = amount
            winner = bidder
    print(f"The winner is {winner} with a bidding amount of ${highest_amount}")

def clear_console():
    # Clear the console (works for Windows and Unix-based systems)
    os.system('cls' if os.name == 'nt' else 'clear')

def start_bidding():
    bids = {}
    continue_bidding = True

    while continue_bidding:
        name = input("What is your name? ")
        try:
            amount = int(input("How much do you bid? "))
        except ValueError:
            print("Please enter a valid number for your bid.")
            continue

        bids[name] = amount

        should_continue = input("Is there anyone else who wants to bid? Type 'yes' or 'no': ").strip().lower()
        if should_continue == 'no':
            continue_bidding = False
            find_highest_bidder(bids)
        elif should_continue == 'yes':
            clear_console()
        else:
            print("Invalid input. Assuming 'yes'.")
            clear_console()

if __name__ == "__main__":
    start_bidding()




    


