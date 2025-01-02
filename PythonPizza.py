print("Welcome to Python Pizza Deliveries!")

# input the size, pepperoni and extra cheese from user
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()


# calculate the bill by using condition statements (if elif and else) 
bill = 0
if size == 's':
    bill = 15
elif size == 'm':
    bill = 20
elif size == 'l':
    bill = 25
else:
    print("may be you entered the wrong size.")

if pepperoni == 'y':
    if size == 's':
        bill += 2
else:
        bill += 3

if extra_cheese == 'y':
     bill += 1

print(f"your total bill is {bill}")




# implement in better and simpler way

print("Welcome to Python Pizza Deliveries!")

# Input the size, pepperoni, and extra cheese from user
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = {"s" : 15, "m": 20, "l" : 25}.get(size, 0)

bill += 2 if size == "s" and pepperoni == "y" else 3 if pepperoni == "y" else 0
bill += 1 if extra_cheese == "y" else 0

print(f"your total bill ${bill}" if bill else "you may entered the wrong input")

