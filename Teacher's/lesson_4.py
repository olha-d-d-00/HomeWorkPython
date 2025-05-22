# Приклади:
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

# numbers = [12, 3, 4, 10, 8]
#
# if len(numbers) > 1:
#     numbers.insert(0, numbers[-1])
#     numbers.pop()
#
# print(numbers)

#####
###
# Цикли
# - while
# - for

# v1
# i = 0
#
# while i < 5:
#     print(i, end=" ")
#     i += 1  # i = i + 1
#
# print("test")

# v2
# import time
#
# i = 12
#
# while True:
#     print(i)
#     i += 2
#     time.sleep(1)

# v3
# i = 0
#
# while True:
#
#     if i == 2:
#         i += 1
#         print("continue...")
#         continue  # пропустить подальші дії циклу, але цикл не зупиниться
#
#     if i > 5:
#         print("break...")
#         break  # цикл зупиниться (повне завершення циклу)
#
#     print(i)
#     i += 1

###
# while True:
#     rating = int(input("Enter your rating from 1 to 3: (0 for exit) "))
#
#     if rating == 0:
#         print("Exit...")
#         break
#
#     if rating < 1 or rating > 3:
#         print("Invalid Rating")
#         continue
#
#     match rating:
#         case 1:
#             print("Bad rating")
#         case 2:
#             print("Normal rating")
#         case 3:
#             print("Excellent rating")


###
# for i in range(5):  # range(5) -> 0, 1, 2, 3, 4
#     # print("Hello")
#     print(i, end=" ")

# for value in 1, 4, "asrfrfg", True, 1.5, "hello":
#     print(value)

# for i in range(1, 5):  # range(1, 5) -> 1, 2, 3, 4
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(1, 10, 2):  # range(1, 10, 2) -> 1 3 5 7 9
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(10, -1, -1):
#     # print("Hello")
#     print(i, end=" ")

# print(range(10))
# print(list(range(10)))

# number = int(input("Enter your number: "))
# mylist = list(range(1, number + 1))
# print(mylist)
# mylist = tuple(range(1, number + 1))
# print(mylist)
# mylist = set(range(1, number + 1))
# print(mylist)

# for i in range(1, number + 1):
#     print(i)

# nums = [1, 2, 4, 2, 56]

# for i in range(len(nums)):  # range(5) -> 0, 1, 2, 3, 4
#     print(nums[i])

# for i in range(0, len(nums), 2):  # range(5) -> 0, 2, 4
#     print(nums[i])
#
# for number in nums:
#     print(number)
#
# print(number)

###############
# # [] -> індексатори
# # Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
# # Індекси рахуються з нуля
# print(numbers[0])
#
# numbers[1] = 11111
# print(numbers)
# print(len(numbers))
# print(numbers[-1])
#
# print(numbers[len(numbers) - 1])  # numbers[6]

####################################
# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
#
# for number in numbers:
#     print(number, end=" ")
#
# print()

# #
# values = ["one", 12, 12.4, True]
# print(values)
#
# #
# nums = [1, 3] * 5
# print(nums)
#
# #
# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers[:])
# print(numbers[1:5])
# print(numbers[1:5:2])
# print(numbers[::-1])

# Розкладання списку (декомпозиція)
# users = ["Vasya", "Petya"]
# user_1, user_2 = users
# print(user_1)
# print(user_2)
# print(users)

####
#
# import random
#
# # print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
# #
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#
# print(numbers)

# # append(item): додає елемент item до кінця списку
# #
# numbers.append(2222)
# print(numbers)
# #
# # # insert(index, item): додає елемент item до списку за індексом index
# #
# numbers.insert(1, 3333)
# print(numbers)
# #
# # # extend(items): додає набір елементів items до кінця списку
# #
# numbers.extend([2, 3, 4])
# print(numbers)
# #
# numbers += [1, 2, 3, 4]  # numbers = numbers + [1, 2, 3, 4]
# print(numbers)
# #
# # # remove(item):видаляє елемент item. Видаляється лише перше входження елемента.
# # # Якщо елемент не знайдено, генерує виняток ValueError
# #
# numbers.remove(2222)
# print(numbers)

# clear(): видалення всіх елементів зі списку

# numbers.clear()
# print(numbers)

# del numbers
# print(numbers)
#
# # index(item): повертає індекс елемента item. Якщо елемент не знайдено, генерує виняток ValueError
#
# print(numbers.index(2))
#
# # pop([index]): видаляє та повертає елемент за індексом index.
# # Якщо індекс не передано, просто видаляє останній елемент.
#
# result = numbers.pop(1)
# print(result)
# print(numbers)
# #
# print(numbers.pop())
# print(numbers)
# #
# # # count(item): повертає кількість входжень елемента item до списку
# #
# print(numbers.count(3))

# sort([key]): Сортує елементи. За умовчанням сортує за зростанням.
# Але за допомогою key ми можемо передати функцію сортування.
# sorted(list, [key]): повертає відсортований список
#
# v1
# numbers.sort()
# print(numbers)
# # v2
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)
# print(numbers)

# people = ["Tom", "bob", "alice", "Sam", "Bill"]
# v1
# people.sort()  # меняет оригинал
# print(people)
# # v2
# people.sort(key=str.lower)  # str.lower -> в нижний регистр (маленькие буквы)
# print(people)
# ##
# people_sorted = sorted(people, key=str.lower)  # возвращает копию, но не модифицирует оригинал
# print(people_sorted)
# print(people)
#
# # reverse(): розставляє всі елементи у списку у зворотному порядку
#
# numbers.reverse()
# print(numbers)

# print(numbers[::-1])
#
# # copy(): копіює список
#
# nums_1 = [1, 3, 5]
# nums_copy = nums_1.copy()
# print(nums_1)
# print(nums_copy)
# nums_copy[1] = 1111
# print(nums_1)
# print(nums_copy)
#
# # Крім того, Python надає ряд вбудованих функцій для роботи зі списками:
# #
# # len(list): повертає довжину списку
#
# print(len(numbers))
#
# # min(list): повертає найменший елемент списку
#
# print(min(numbers))
#
# # max(list): повертає найбільший елемент списку
#
# print(max(numbers))
#
# users = ["Vasya", "Petya"]
# print(max(users))
# #
# letters = ["ab", "ac"]
# print(max(letters))

###############
# text = "hello world. goodbye world."
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

##
# створити список із 10 випадкових чисел
# поміняти місцями мінімальне значення з максимальним
# [3, 1, 4, 2, 5] -> [3, 5, 4, 2, 1]

# numbers = [3, 1, 4, 2, 5]
#
# print(numbers)

# v1
# min_value = min(numbers)
# max_value = max(numbers)
#
# print("min_value", min_value)
# print("max_value", max_value)
#
# min_value_index = numbers.index(min_value)
# max_value_index = numbers.index(max_value)
#
# print("min_value_index", min_value_index)
# print("max_value_index", max_value_index)
#
# numbers[min_value_index] = max_value
# numbers[max_value_index] = min_value
#
# print(numbers)

# v2
# numbers_copy = numbers.copy()
#
# # numbers_copy[вычисляем индекс минимума], numbers_copy[вычисляем индекс максимума] = максимум, минимум
# # numbers_copy[1], numbers_copy[4] = 5, 1
# numbers_copy[numbers.index(min(numbers))], numbers_copy[numbers.index(max(numbers))] = max(numbers), min(numbers)
# numbers = numbers_copy.copy()
#
# print(numbers)

###############
# values = ["Vasya", 33, ["dance", "walk"]]
# print(values)
# print(values[2])
# print(values[2][0])

##
# v1
# [[1, 3, 2], [1, 4], 1, [[1, 2], [3, 5]]]
# array = [
#     [1, 3, 2],
#     [1, 4],
#     1,
#     [
#         [1, 2],
#         [3, 5]
#     ]
# ]
# print(array)
# print(array[3][1][1])
# print(array[3][0][0])
# v2
# matrix = [
#     [24, 41, 15, 62],
#     [22, 41, 15, 62],
#     [25, 42, 11, 66],
#     [27, 46, 16, 63]
# ]

# print(matrix[0][1])
# print(matrix)
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

#
# import random
#
# matrix = []
#
# # print(matrix)
# for i in range(3):
#     matrix.append([])
#     # print(matrix)
#     for j in range(3):
#         matrix[i].append(random.randint(10, 99))
#         # print(matrix)

# print(matrix)
# #
# # # v1
# print(len(matrix))
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
# #
# print()
# # # # v2
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

##############################
# import random
# import string
#
# DATA_FOR_PASSWORD = string.digits + string.punctuation + string.ascii_letters
# MIN_PASSWORD_LEN = 8
# MAX_PASSWORD_LEN = 16
#
# # print(DATA_FOR_PASSWORD)
#
# while True:
#     new_password = []
#
#     password_length = int(input(f"Enter the password length (from {MIN_PASSWORD_LEN} to {MAX_PASSWORD_LEN}): "))
#
#     if password_length < MIN_PASSWORD_LEN or password_length > MAX_PASSWORD_LEN:
#         print(f"Password must be between {MIN_PASSWORD_LEN} and {MAX_PASSWORD_LEN} characters")
#         continue
#
#     new_password.append(random.choice(string.punctuation))
#     new_password.append(random.choice(string.digits))
#     new_password.append(random.choice(string.ascii_lowercase))
#     new_password.append(random.choice(string.ascii_uppercase))
#
#     for i in range(password_length - 4):
#         new_password.append(random.choice(DATA_FOR_PASSWORD))
#
#     random.shuffle(new_password)
#
#     result_password = "".join(new_password)
#     print(result_password)
#
#     exit_or_no = input("Enter 'q' if you want to exit: ")
#     if exit_or_no == 'q':
#         break
