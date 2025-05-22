###
# message = "hello world"
# # # [] -> індексатори
# # # Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
# # # Індекси рахуються з нуля
# print(message[0])
# print(len(message))  # кількість символів у рядку
# # print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])
#
# ###
# # # string - immutable тип даних, рядок змінити не можна
# name = "Petya"
# print(name)
# # name[1] = "r"  # TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

# # # v1
# sentence = "Hello, world"
# for letter in sentence:
#     print(letter, end=" ")
#
# print()
# #
# # # v2
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")

# # slices (срезы)
# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])

#
# name = "Vasya"
# surname = "Petrov"
# age = 33
#
# fullname = name + " " + surname + " " + str(age)  # конкатенація (додавання рядків)
# print(fullname)
#
#
# text = "Hello, world" * 3
# print(text)
#
# print("---" * 10)
#
# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# print(ord("A"))
# print(chr(65))
# print(chr(99))

####
# text = "helLo woRlD"
#
# # isalpha(): повертає True, якщо рядок складається лише з алфавітних символів
#
# print(text.isalpha())
#
# # islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі
#
# print(text.islower())
#
# # isupper(): повертає True, якщо всі символи рядка у верхньому регістрі
#
# print(text.isupper())
#
# # isdigit(): повертає True, якщо всі символи рядка - цифри
#
# print(text.isdigit())
#
# # isnumeric(): повертає True, якщо рядок є числом
#
# print(text.isnumeric())
#
# # startswith(str): повертає True, якщо рядок починається з підрядка str
#
# print(text.startswith("helLo"))
#
# # endswith(str): повертає True, якщо рядок закінчується на підрядок str
#
# print(text.endswith("D"))
#
# # lower(): перекладає рядок у нижній регістр
#
# print(text.lower())
#
# # upper(): перекладає рядок у верхній регістр
#
# print(text.upper())
#
# # title(): початкові символи всіх слів у рядку перекладаються у верхній регістр
#
# print(text.title())
# #
# # # capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка
# #
# print(text.capitalize())
# #
# fio = input("Enter fio: ").title()
# print(fio)

#
# lstrip(): видаляє початкові пробіли з рядка
# text = "        helLo woRlD         "
# print(text)
# print(text.lstrip())
#
# # rstrip(): видаляє кінцеві пробіли з рядка
# print(text)
# print(text.rstrip())
#
# # strip(): видаляє початкові та кінцеві пробіли з рядка
# print(text)
# print(text.strip())
#
# # ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по лівому краю
# text = "hello world"
# print(text)
# print(text.ljust(20))
#
# # rjust(width): якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється праворуч
# text = "hello world"
# print(text)
# print(text.rjust(20))
#
# # center(width): якщо довжина рядка менша за параметр width,
# # то ліворуч і праворуч від рядка рівномірно додаються пробіли,
# # щоб доповнити значення width, а сам рядок вирівнюється по центру
# text = "hello world"
# print(text)
# print(text.center(20))
#
# # find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, повертається число -1
# text = "hello world"
# print(text.find("hello"))  # 0
# print(text.find("l"))  # 2
# print(text.rfind("l"))  # 9
# #
# first_found_index = text.find("l")
# print(text.find("l", first_found_index + 1))
# #
# print(text.find("p"))  # -1
# #
# # v1
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)
#
# # # v2
# index = 0
#
# for letter in text:
#     if letter == "l":
#         print(index)
#     index += 1

#

# # # replace(old, new[, num]): замінює в рядку один підрядок на інший
# text = "hello world hello"
# print(text)
#
# text = text.replace("hello", "goodbye", 1)
# print(text)

###############
# text = "hello world. goodbye world. hello world."
# search_item = ". "
#
# sentences = text.split(search_item)
# print(sentences)
#
# result = []
#
# for sentence in sentences:
#     result.append(sentence.capitalize())
#
# print(result)
#
# result_sentence = search_item.join(result)
# print(result_sentence)

###################################
# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
#
# вивести на екран
#
# - вивести суму чисел головної діагоналі матриці
#
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
#
# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
#
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# (аналогічно зробити з рядком)

#################################
# import random
#
# matrix = []
#
# # print(matrix)
# for i in range(5):
#     matrix.append([])
#     for j in range(5):
#         matrix[i].append(random.randint(10, 99))
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

# - вивести суму чисел головної діагоналі матриці

# general_diagonal_sum = 0
#
# for i in range(len(matrix)):
#     general_diagonal_sum += matrix[i][i]
#     print(matrix[i][i])
#
# print(f"General diagonal sum: {general_diagonal_sum}")

# - вивести мінімальне та максимальне значення побічної діагоналі матриці

# numbers = []
#
# for i in range(len(matrix)):
#     numbers.append(matrix[i][len(matrix[i]) - 1 - i])
#
# print(numbers)
# print(f"Min value: {min(numbers)}")
# print(f"Max value: {max(numbers)}")

# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)

# ROWS = 5
#
# direction = int(input("Enter direction:\n1. Vertical\n2. Horizontal: "))
#
# match direction:
#     case 1:
#         number = int(input(f"Enter column number from 1 to {len(matrix)}: "))
#         if 1 <= number <= len(matrix):
#             for i in range(len(matrix)):
#                 print(matrix[i][number - 1], end=" ")
#         else:
#             print("column number out of range!")
#     case 2:
#         number = int(input(f"Enter row number from 1 to {len(matrix)}: "))
#         if 1 <= number <= len(matrix):
#             for num in matrix[number - 1]:
#                 print(num, end=" ")
#         else:
#             print("row number out of range!")
#     case _:
#         print("Incorrect matrix direction!")

# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# (аналогічно зробити з рядком)

# ROWS = 5
#
# direction = int(input("Enter direction:\n1. Vertical\n2. Horizontal: "))
#
# match direction:
#     case 1:
#         first_column = int(input(f"Enter column number from 1 to {len(matrix)}: "))
#         second_column = int(input(f"Enter column number from 1 to {len(matrix)}: "))
#         if 1 <= first_column <= len(matrix) and 1 <= second_column <= len(matrix) and first_column != second_column:
#             for i in range(len(matrix)):
#                 # matrix[0][1 - 1], matrix[0, 3 - 1] = matrix[0][3 - 1], matrix[0][1 - 1]
#                 # 84, 42 = 42, 84
#                 matrix[i][first_column - 1], matrix[i][second_column - 1] =  \
#                     matrix[i][second_column - 1], matrix[i][first_column - 1]
#
#             for row in matrix:
#                 for number in row:
#                     print(number, end=" ")
#                 print()
#         else:
#             print("Incorrect column number!")
#     case 2:
#         first_row = int(input(f"Enter row number from 1 to {len(matrix)}: "))
#         second_row = int(input(f"Enter row number from 1 to {len(matrix)}: "))
#         if 1 <= first_row <= len(matrix) and 1 <= second_row <= len(matrix) and first_row != second_row:
#             # matrix[3 - 1], matrix[5 - 1] = matrix[5 - 1], matrix[3 - 1]
#             # [80 61 52 43 39], [38 48 74 58 51] = [38 48 74 58 51], [80 61 52 43 39]
#             # swap
#             # first_value = [80 61 52 43 39]
#             # matrix[3 - 1] = matrix[5 - 1]
#             # matrix[5 - 1] = first_value
#             matrix[first_row - 1], matrix[second_row - 1] = matrix[second_row - 1], matrix[first_row - 1]
#
#             for row in matrix:
#                 for number in row:
#                     print(number, end=" ")
#                 print()
#         else:
#             print("Incorrect column number!")
#     case _:
#         print("Incorrect matrix direction!")

##########################
# import random
# import string
#
# MIN_PASSWORD_LENGTH = 8
# MAX_PASSWORD_LENGTH = 16
#
# data_for_password = string.ascii_letters + string.punctuation + string.digits
#
# while True:
#     user_password_len = input(f"Enter your password length (from {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH}): ")
#
#     if not user_password_len.isnumeric():
#         print("Enter a valid number!")
#         continue
#
#     user_password_len = int(user_password_len)
#
#     if user_password_len < MIN_PASSWORD_LENGTH or user_password_len > MAX_PASSWORD_LENGTH:
#         print("Incorrect password length!")
#         continue
#
#     password_raw = []
#
#     for _ in range(user_password_len):
#         password_raw.append(random.choice(data_for_password))
#
#     random.shuffle(password_raw)
#     password = "".join(password_raw)
#
#     print(f"Your new password is: {password}")
#
#     user_input = input("Enter '-' to exit the program or any key to continue: ")
#     if user_input == "-":
#         print("Exit from program...")
#         break

####
# for _ in range(3):
#     print("Hello")

# _ = "Hello"
# print(_)

###
# import os
#
# text_to_copy = "My text test"
# command = f'echo {text_to_copy.strip()}| clip'
# os.system(command)

####
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

#######
# cats, dogs = 3, 5
# text = "Cats: {}, Dogs: {}".format(cats, dogs)
# print(text)
# text = "Cats: {1}, Dogs: {0}".format(cats, dogs)
# print(text)
# text = "Cats: {1}, Dogs: {1}".format(cats, dogs)
# print(text)
# text = f"Cats: {cats}, Dogs: {dogs}"
# print(text)

#
# import keyword
#
# test_data = ["_", "__", "___", "import"]
#
# for test_variable_name in test_data:
#     if test_variable_name in keyword.kwlist:
#         print(f"Incorrect naming convention for potential variable: {test_variable_name}")
#         continue
#
#     print(f"Correct naming convention for potential variable: {test_variable_name}")

############
# import random
#
# numbers = []
#
#
# for i in range(5):
#     numbers.append(random.randint(10, 99))
#
# print(numbers)
#
# numbers2 = [random.randint(10, 99) for i in range(5)]
# print(numbers2)
#
# numbers3 = [number for number in range(20) if number % 2 == 0]
# print(numbers3)

##########################
# game_field_size = 3
# game_field = []
#
# for i in range(game_field_size):
#     game_field.append([])
#     for j in range(game_field_size):
#         game_field[i].append(" ")
#
# # print(game_field)
#
# first_player = "x"
# second_player = "0"
#
# current_tern = first_player
#
# while True:
#     for row in game_field:
#         print(row)
#
#     print(f"{current_tern} tern!")
#     coord_x = int(input("Enter x coord: "))
#     coord_y = int(input("Enter y coord: "))
#
#     if (coord_x < 0 or coord_y < 0 or coord_x >= game_field_size or coord_y >= game_field_size or
#             game_field[coord_x][coord_y] != " "):
#         print("Invalid coordinate")
#         continue
#
#     if current_tern == first_player:
#         game_field[coord_x][coord_y] = first_player
#         current_tern = second_player
#     else:
#         game_field[coord_x][coord_y] = second_player
#         current_tern = first_player




