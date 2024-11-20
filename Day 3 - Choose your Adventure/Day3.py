# Day 3 - Choose your Adventure
#Purpose: Practicing if statements by creating a game in which you get to decide where to progress. 

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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You come across a road. Do you take the 'left' or the 'right' road?")

if direction != 'left':
    print("You slip and fall in a bottomless hole.\n Game Over.")
else:
    direction = input("The road leads to a river. You could 'swim' across it or 'wait' by the bank.")
    if direction != 'wait':
        print("As you swim across the river, a swarm of trout attacks you. You drown. Blub, blub.\n Game Over.")
    else:
        direction = input("A magical portal opens before you. You step through. There are three doors now before you. A 'red' one. A 'blue' one. And a 'yellow' one.")
        if direction == 'red':
            print("Going through the red door, you enter a room that immediately bursts into flame. You smolder to a crisp.\nGame Over.")
        elif direction == 'yellow':
            print("You step through the yellow door into a lavish treasure room filled with trinkets and gold!\nYou Win!")
        elif direction == 'blue':
            print("You push through the blue door only to be set upon by a hoard of hungry beasts! You're torn to shreds.\nGame Over.")
        else:
            print("What...? I guess you clip through the floor and walls and end up into a mysterious other dimension that looks like an office. Game Over.")
