
# import random
#
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
# game_graphics = [rock, paper, scissors]
# user_choice = int(input("Welcome to the game! Type 0 for rock, 1 for paper, 2 for scissors \n"))
#
# if user_choice >=3 or user_choice < 0:
#     print("The number is invalid, You lose!")
# else:
#     print(game_graphics[user_choice])
#
#     computer_choice = random.randint(0, 2)
#     print(f"Computer choice: {computer_choice}")
#     print(game_graphics[computer_choice])
#
#     if computer_choice == 0 and user_choice ==2:
#         print("Computer Wins")
#     elif user_choice == 0 and computer_choice == 2:
#         print("You Win!")
#     if computer_choice > user_choice:
#         print("Computer Wins")
#     elif user_choice > computer_choice:
#         print("You Win!")
#     elif user_choice == computer_choice:
#         print("Game Draw")

