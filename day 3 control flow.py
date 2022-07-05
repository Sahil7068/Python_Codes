# print("Welcome to the rollercoaster ride")
# height = int(input("What is your height in cm? "))
# if height>180:
#     print("You can ride rollercoaster")
# else:
#     print("You cannot man, go home")


#ODD AND EVEN

# number = int(input("Number you want to check man "))
# if number%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

#NESTED IF/ELSE

# print("Welcome to the rollercoaster ride")
# height = int(input("What is your height in cm? "))
# if height>180:
#     print("You can ride rollercoaster")
#     age = int(input("Chacha, chaliye apna age daliye "))
#     if age>=18:
#         print("chal $7 nikal")
#     else:
#         print("$5 me ho gayega")
# else:
#     print("You cannot man, go home")


#IF/ELIF/ELSE

# print("Welcome to the rollercoaster ride")
# height = int(input("What is your height in cm? "))
# if height > 180:
#     print("You can ride rollercoaster")
#     age = int(input("Chacha, chaliye apna age daliye "))
#     if age < 12:
#         print("chal $7 nikal")
#     elif age<=18:
#         print("pay $3")
#
#     else:
#         print("$5 me ho gayega")
# else:
#     print("You cannot man, go home")

#Rough
# print("Welcome to war")
# height = int(input("Enter your height in cm "))
# if height>162:
#     print("Congratulations! You're eligible.")
#     age = int(input("Enter your age "))
#     if age<16:
#         print("Enroll yourself in NDA")
#     elif age<=20:
#         print("Congrats, you'll go into Millitary")
#     else:
#         print("Air force")
#
#
# else:
#     print("Go home man, come next year with some extra inches")


#BMI

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
#
# BMI = round(weight/height ** 2)
# print(BMI)
#
# if BMI<18.5:
#     print("Chacha is underweight")
# elif 25>=BMI>=18.5:
#     print("Chacha is normal")
# elif  30>= BMI>=25:
#     print("Chacha is overweight")
# elif 35>=BMI>=30:
#     print("Chacha is obese")
# else:
#     print("Chacha is clinacally obsese")

#LEAP YEAR

# year = int(input("Enter a year to check leap year "))
# if year % 4==0:
#     if year % 100==0:
#         if year % 400==0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

#PYTHON PIZZA TIME

# print ("Welcome to pizza deliveries!")
# size = input("What size of pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
#
# if size=="S":
#     bill +=15
# elif size=="M":
#     bill +=25
# else:
#     bill +=35
#
# if add_pepperoni=="Y":
#     if size=="S":
#         bill +=2
#     else:
#         bill +=5
#
# if extra_cheese=="Y":
#     bill +=1
#
# print(f"Your bill is ${bill}")

#Tshirts

# print("Welcome to SL world Tshirts! ")
# size = input("Choose your Tshirt size- S, M, or L ")
# add_spiderman_poster = input("Do you want spiderman graphics- Y or N ")
# add_pocket = input("Do you want a pocket- Y or N ")
# bill = 0
#
# if size=="S":
#     bill +=300
# elif size=="M":
#     bill +=320
# else:
#     bill +=350
#
# if add_spiderman_poster == "Y":
#     bill += 50
# if add_pocket == "Y":
#     bill += 25
#
# print(f"Your total bill is ${bill}")

# print("SAHIK".count("S"))

#LOVE CALCULATOR

# print("Welcome to the love calculator! ")
# name_1 = input("Enter your name \n")
# name_2 = input("Enter your crush's name \n")
#
# combined_name = name_1 + name_2
# lowercase_name = combined_name.lower()
#
# t = lowercase_name.count("t")
# r = lowercase_name.count("r")
# u = lowercase_name.count("u")
# e = lowercase_name.count("e")
# true = t + r + u + e
#
# l = lowercase_name.count("l")
# o = lowercase_name.count("o")
# v = lowercase_name.count("v")
# e = lowercase_name.count("e")
# love = l + o + v + e
#
# love_calculator = int(str(true) + str(love))
#
# if (love_calculator<10) or (love_calculator>90):
#     print(f"Your score is {love_calculator}, and you guys are not compatible for each other")
# elif (love_calculator >= 40) and (love_calculator <= 50):
#     print(f"Your score is {love_calculator}, you guys are alright together")
# else:
#     print(f"Your score is {love_calculator}, you guys are okay doke")

#TREASURE ISLAND
#
# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************''')

# print("Welcome to the treasure island. Your mission is to find the treasure")
# choice_1 = input('You are at a crossroad, where do you wanna go? Type "left" or "right". \n').lower()
#
# if choice_1 == "left":
#     choice_2 = input('You are in next level, choose your options Type "swim" or "wait" \n').lower()
#     if choice_2 == "wait":
#         final_choice = input('Congratulations! You are in the final level, you have to choose one door "RED" "YELLOW" "BLUE" \n').lower()
#         if final_choice == "red":
#             print("The roome is full of fire, GAME OVER!")
#         elif final_choice == "blue":
#             print("The room is full of water, GAME OVER!")
#         elif final_choice == "yellow":
#             print("Congratulations! You found the treasure!")
#     else:
#         print("You are attacked by a Shark, GAME OVER!")
#
# else:
#     print("You fell into the hole, GAME OVER!")

#MARIO WORLD

print('''────────────────────────────────────────
──────────────────────▒████▒────────────
───────────────────░█████▓███░──────────
─────────────────░███▒░░░░░░██──────────
────────────────▒██▒░░░▒▓▓▓▒░██─────────
───────────────▓██░░░▒▓█▒▒▒▓▒▓█─────────
──────────────▓█▓─░▒▒▓█─────▓▓█░────────
─────────────▓█▒░▒▒▒▒█──▓▓▒▒─▓█▒────────
────────────▒█▒░▒▒▒▒▓▒─▒▓▒▓▓─▒█░────────
────────────█▓░▒▒▒▒▒▓░─▓▒──░░▒█░────────
───────────██░▒▒▒▒▒▒█──▓──░▓████████────
──────────░█▒▒▒▒▒▒▒▒▓░─█▓███▓▓▓▓██─█▓───
────────▒▓█▓▒▒▒▒▒▒▒▒▓███▓▓████▓▓██──█───
──────░███▓▒▒▒▒▓▒▒▒████▒▒░░──████░──██░─
──────██▒▒▒▒▒▒▒▒▒▓██▒────────▒██▓────▓█─
─────▓█▒▒▒▒▒▒▒▒▓█▓─────▓───▒░░▓──▓────▓█
─────██▒▓▒▒▒▒▒█▓──────▒█▓──▓█░▒──▒░────█
─────██▒▒▓▓▓▒█▓▓───░──▓██──▓█▓▓▓█▓─────█
─────▓█▒██▓▓█▒▒▓█─────░█▓──▒░───░█▓────█
─────░██▓───▓▓▒▒▓▓─────░─────────▒▒─░─░█
──────▓█──▒░─█▒▓█▓──▒───────░─░───█▒──█▒
───────█──░█░░█▓▒──▓██▒░─░─░─░─░░░█▒███─
───────█▒──▒▒──────▓██████▓─░░░░─▒██▓░──
───────▓█──────────░██▓▓▓██▒─░──░█▒─────
────────██▒─────░───░██▓▓▓██▓▒▒▓█▒──────
─────────░████▒──░───▒█▓▓▓▓▓████▓───────
────────▒▓██▓██▒──░───▓█████▓███────────
──────▒██▓░░░░▓█▓░────░█▒█▒─▒▓█▓────────
─────▓█▒░░▒▒▒▒▒▓███▓░──▓█▒─▒▓▓█─────────
────░█▒░▒████▓██▓▓▓██▒───░▓█▓█░─────────
────▓█▒▒█░─▒───▓█▓▓▓▓▓▓▒▒▓█▓█▓──────────
────▓█▒█░───────██▓▓▓▓▓█▓▓█▓██──────────
────▒█▓▓────────░██▓██▓▓▓▓▓▓▓▓█─────────
─────██░────▓▓────█░─█▓▓▓▓▓▓▓─▒█████────
─────██░───░──────▓░─▓▓▓▓▓▓▓█─▒█▒░▒██───
────▓█░▓░──▓▓────▒█░─█▓▓▓▓▓▓▓█▒─░░░▒██──
────█─▒██─░──────████▓▓▓▓▓▓▓█▓─░▒▒█▓▓█░─
───▓█─▓▒▓▒░░────▓█▓▓▓▓▓▓▓▓▓▓█░░▒▓█░──▒█─
───▒█░█▒▒█▒───░▓█▓▓▓▓▓▓▓▓▓▓█▓░▒▓▓──▓█▓█─
───█▓▒▓▒▒▓██████▓▓▓▓▓▓▓▓▓▓▓█▒▒▓▓─░█▓▒▒█░
───█░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▒▓─▒█▒▒▒▒█─
──▒█─█▒▒▒▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓─▒█▒▒▒▒██─
──▓█─█▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒▓▒░█▒▒▒░▓█──
──▓█─█▒▓▒▒▓█▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒▓░▓░░░░▒█░──
──▒█─▓▓▓▓▒▓█▓▓▓▓▓▓▓▓█████▓▓▓▓▒▓░░─▒█▒───
───█▒▓▓▓▓▓▒▓██████████░░██▓█─▒█▓▒▓█░────
───▓█▒█▓▓▓▓▒▓██░─░▒░─────██▒░▓▓▓▒██─────
────████▓▓▓██░───────────▓█░▓▒░░▓█░─────
──────░█████░─────────────██▓─▒██░──────
───────────────────────────▓███▒────────''')

print("Welcome to the Mario World")
print("Princess is abducted, we need your help Mario! please save our queen")
print("Mario - I'll save her, don't worry")
print("Adventure Begins!")

choice_1 = input('To save the queen, you need to make choice - Choose "bridge" or "sea" \n').lower()
if choice_1 == "sea":
    choice_2 = input('You have chosen the waterways, choose your ride - "boat" or "turtle" \n').lower()
    if choice_2 == "turtle":
        choice_3 = input('You have chosen the right ride, where you want to land - "island" or "cloud" \n').lower()
        if choice_3 == "island":
            choice_4 = input('You have made the right choice, you are close to your queen. Choose the right castle - "black" "green" "yellow" \n').lower()
            if choice_4 == "green":
                print("The castle is full of crocodile, GAME OVER!")
            elif choice_4 == "black":
                print("Congratulations Mario! You have saved your queen")
            elif choice_4 == "yellow":
                print("The castle is full of anacondas, GAME OVER!")
        else:
            print("Sorry! Clouds could not able to bear your weight Mario, GAME OVER!")
    else:
        print("Boat drowns, GAME OVER!")
else:
    print("Bridge falls, GAME OVER!")


















