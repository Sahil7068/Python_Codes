#LOOP

# fruits = ["apple", "pear", "mango"]
# for fruit in fruits:
#     print(fruit)

#EXAMPLE

# student_height = input("Input a list of student's height ").split()
# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])
# print(student_height)
#
# total_height = 0
# for height in student_height:
#     total_height += height
# print(total_height)
#
# number_of_student = 0
# for n in student_height:
#     number_of_student += 1
# print(number_of_student)
#
# avg = round((total_height / number_of_student))
# print(avg)

#EXAMPLE

# student_scores = input("Input a list of student's scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # print(max(student_scores))
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score is {highest_score}")

#RANGE
# add = 0
# for number in range(1, 101):
#     add = add + number
# print(add)

# add = 0
# for number in range(1, 11, 2):
#     print(number)
#     add = add + number
# print(add)

#BUZZFIZZ

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 ==0:
#         print("FIZZ BUZZ")
#     elif number % 5 == 0:
#         print("BUZZ")
#     elif number % 3 == 0:
#         print("FIZZ")
#     else:
#         print(number)


#U

# for number in range(1, 41):
#     if number % 4 == 0:
#         print("LOOK")
#     elif number % 6 == 0:
#         print("BACK")
#     else:
#         print(number)

#PASSWORD GENERATOR

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(1, nr_letters + 1):
    password = password + random.choice(letters)

for char in range(1, nr_symbols + 5):
    password = password + random.choice(symbols)

for char in range(1, nr_numbers + 3):
    password = password + random.choice(numbers)

print(password)