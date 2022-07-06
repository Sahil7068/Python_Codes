#RANDOMISATION

#import random
# random_integer = random.randint(1, 100)
# print(random_integer)

# random_float = random.random() # for decimal numbers, we have to use random.random()
# k = random_float * 5
# print(k)

#HEAD OR TAIL random

# head_or_tail = random.randint(0, 1)
# if head_or_tail == 0:
#     print("Heads")
# else:
#     print("Tails")

#LIST

# states_of_india = ["jharkhand", "bihar", "rajasthan", "kerela"]
# print(states_of_india[3])

#ROUGH

# name_string = input("Give me everybody's name, seperated with a comma ")
# names = name_string.split(", ")
# length = len(names)
# random_name = random.randint(0, length-1)
# person_who_will_pay = names[random_name]
# print(person_who_will_pay + " is going to buy the meal")

#NESTED LIST

# fruits = ["mango", "apple", "peach", "cherry"]
# vegetables = ["potato", "onion", "spinach", "lettuce"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

#TREASURE ISLAND USING NESTED LIST

# row_1 = ["☐", "☐", "☐"]
# row_2 = ["☐", "☐", "☐"]
# row_3 = ["☐", "☐", "☐"]
# map = [row_1, row_2, row_3]
# print(f"{row_1}\n{row_2}\n{row_3}\n")
# position = input("Where do you want to put the treasure? ")
# vertical = int(position[0])
# horizontal = int(position[1])
# selected_row = map[horizontal -1]
# selected_row[vertical -1] = "x"
# print(f"{row_1}\n, {row_2}\n, {row_3}\n")

#ROUGH

# row_1 = ["☐", "☐", "☐"]
# row_2 = ["☐", "☐", "☐"]
# row_3 = ["☐", "☐", "☐"]
# print(f"{row_1}\n{row_2}\n{row_3}\n")
# map = [row_1, row_2, row_3]
# position = input("Where do you want to put the treasure? ")
# vertical = int(position[0])
# horizontal = int(position[1])
# selected_row = map[horizontal -1]
# selected_row[vertical -1] = "X"
# print(f"{row_1}\n{row_2}\n{row_3}\n")

#ROCK PAPER SCISSORS

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# game_images = (rock, paper, scissors)
# user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
# if user_choice >=3 or user_choice < 0:
#     print("Your choice is invalid, You lose!")
# else:
#     print(game_images[user_choice])
#
#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])
#
#
#     if user_choice == 0 and computer_choice ==2:
#         print("You lose!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You lose!")
#     elif user_choice > computer_choice:
#      print("You win!")
#     elif computer_choice > user_choice:
#         print("You lose!")
#     elif user_choice == computer_choice:
#         print("It's a draw")
