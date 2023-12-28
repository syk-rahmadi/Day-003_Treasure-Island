print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to treasure island \n" "Your ojective if to find a hidden treasure\n" "Try to survive the game until the end. ")

txt1 = input("You are in cross road, choose 'left' or 'right' ").lower()

if txt1 == "right":
    txt2 = input("Congratulation you have arrived in lake of joy. Choose if you want to swim or take a boat ").lower()
    if txt2 == "swim":
        txt3 = input("You made to edge of the lake. Arrived in hut with the color door. Choose your door, red, green and yellow ").lower()
        if txt3 == "red":
            print("You met with redhair chichk")
        elif txt3 == "green":
            print("You find a truck of cabbage")
        elif txt3 == "yellow":
            print("You find a stack of gold digger. Congratulation, now you get hot girl")
    else:
        print("You take the boat which full of snake and you are dead.")

else:
    print("Sadly, you fall to black hole.")