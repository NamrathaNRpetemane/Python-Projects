print("Welcome to tip Calculator")

# input the amount, tip and persons from user
bill = float(input("what was the total bill?  "))
tip = int(input("How much tip would you like to give? 10, 12, or 15?  "))
split = int(input("How many people to split the  bill?  "))

# calculate the bill for each person to pay
total_tip = tip / 100
total_bill = (bill * total_tip) + bill
each_person_bill = total_bill / split


print(f"each person should pay: {each_person_bill}")


