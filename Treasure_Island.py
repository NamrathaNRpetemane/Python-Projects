print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')



print("Welcome to Treasure Island Project")
print("your mission is to find the treasure")

choice = input("you are at a crossroad, where do you want to go? 'left' or 'right'.  ").lower()

if choice == "left":
    choice_2 = input('you\' have come to a lake.'
                 'there is an island in the middle of the lake.'
                 'Type "wait" to wait for a boat.'
                 'Type "swim" to swim across \n ').lower()
    
    if choice_2 == "wait":
        choice_3 = input('you\' arrive at the island unharmed.'
                     'there is house with 3 doors.'
                     'one red, one yellow, and one blue. which color do you choose?  ').lower()
        
        if choice_3 == "yellow":
            print("you found the treasure. You win!")
        elif choice_3 == "red":
            print("It's a room full of fire. Game over!")
        else:
            print("you entered a room of beasts. Game over!")
    else:
        print("You got attacked by an angry trout. Game Over")

else:
    print("You fell in to a hole. Game Over.")
