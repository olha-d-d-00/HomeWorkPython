# number = int(input("Enter your number:"))
#
# while number > 9:
#     result = 1
#     while number > 0:
#         num = number % 10
#         number = number // 10
#         result = result * num
#     number = result
#     print(result)

# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729,
# Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1


###
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

# import string
#
# ALL_LETTERS = string.ascii_letters
# SEPARATOR = "-"
#
# user_input = input("Enter letters in format: 'a-c' ").strip()
#
# if len(user_input) == 3:
#     first_letter = user_input[0]
#     second_letter = user_input[2]
#     separator = user_input[1]
#
#     if first_letter.isalpha() and second_letter.isalpha() and separator == SEPARATOR:
#         start_index = ALL_LETTERS.index(first_letter)
#         end_index = ALL_LETTERS.index(second_letter)
#
#         if start_index > end_index:
#             start_index, end_index = end_index, start_index
#
#         result = ALL_LETTERS[start_index:end_index + 1]
#
#         # result = string.ascii_letters[end_index:start_index + 1][::-1]
#         print(result)

####
# Ваше завдання — написати програму, яка перемножує всі цифри,
# введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
#
# number = 999
# print(number)
#
# while number > 9:
#     temp_number = str(number)
#     number = 1
#     for char in temp_number:
#         if char.isdigit():
#             number *= int(char)
#     print(number)

# 999 -> "999" -> 9 * 9 * 9 => 729
# 729 -> 7 * 2 * 9 => 126
# 126 -> 1 * 2 * 6
# 12 -> 1 * 2
# 2 -> stop while

# ##############
# # # Множини (set) представляють ще один вид набору, який зберігає тільки унікальні елементи.
# # Дублікати значень буде видалено.
# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))
# #
# people = ["Mike", "Bill", "Ted"]
# users = set(people)
# print(users)
# # # #
# print(len(users))
# # #
# users.add("Sam")
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
# #
# user = "Tom"
# if user in users:
#     users.remove(user)  # якщо немає значення – генерується виняток
# print(users)
# # #
# users = {"Tom", "Bob", "Alice"}
# #
# users.discard("Tim")  # елемент "Tim" відсутній, і метод нічого не робить
# print(users)
# # # #
# users.clear()
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)
#
# # copy() копіювання працює так само як і в list, dict і тд
# users = {"Tom", "Bob", "Alice"}
# users_copy = users.copy()
# print(users_copy)
# print(users)
# users_copy.add("test")
# print(users_copy)
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Tom", "Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.intersection(users2)  # перетин множин (що загальне у першої множини з другим)
# # v2
# print(users & users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users.intersection_update(users2)  # те саме, тільки результат буде записаний в users
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.difference(users2)  # що є тільки першим і немає у другій множині
# print(users3)  # {"Tom", "Alice"}
# # v2
# print(users - users2)
# # #
# users.difference_update(users2)
# print(users)
# print(users2)
# #
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.symmetric_difference(users2)  # унікальні значення першої та другої множин
# print(users3)
# #
# # # v2
# users4 = users ^ users2
#
# ##
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issubset(superusers))  # True
# print(superusers.issubset(users))  # False
#
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issuperset(superusers))  # False
# print(superusers.issuperset(users))  # True
#
# #
# # # Тип frozen set є видом множин, які не можуть бути змінені (за типом tuple у list)
# users = frozenset({"Tom", "Bob", "Alice"})
# print(users)
# users = set(users)
# print(users)
# # # можна використовувати всі функції звичайного set, крім тих, що модифікують значення

####
# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

# numbers = []
#
# number_to_add = 1
#
# numbers_length = len(numbers)
# if numbers_length % 2 == 0:
#     number_to_add = 0
#
# first_part = numbers[:numbers_length // 2 + number_to_add]
# second_part = numbers[numbers_length // 2 + number_to_add:]
# result = [first_part, second_part]
# print(result)

############
# numbers = [2, 0, 5, 1, 0, 6, 2, 0, 8]
#
# temp_numbers = []
#
# for number in numbers:
#     if number != 0:
#         temp_numbers.append(number)
#
# print(temp_numbers)
#
# for _ in range(numbers.count(0)):
#     temp_numbers.append(0)
#
# print(temp_numbers)
#
# numbers = temp_numbers
# print(temp_numbers)

#####
###################################### functions

######
# def say_hello():
#     print("Hello")
#
#
# number = 10
# print(number)
# print(say_hello)
# say_hello()  # виклик функції (функція починає працювати)
# say_hello()


# def say_hello():
#     print("Hello Friends!")
#
#
# say_hello()


# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "test"
#     print(f"Hello {name}!")


# say_hello("test user")
# name = "Anton"
# say_hello(name)
# print(name)
# username = "Petya"
# say_hello(username)

#
#
# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
#

# def show_user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# user_hobby = input("Enter your hobby: ")
# show_user_info(name, age, user_hobby)
#
# show_user_info("Petya", 123, user_hobby)

########
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)

# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# та функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто
# Зупинить дії. Якщо функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів

# def add(n1, n2):
#     # print(n1 + n2)
#     return n1 + n2
#
#
# def sub(n1, n2): return n1 - n2
#
#
# def mult(n1, n2): return n1 * n2
#
#
# def division(n1, n2): return n1 / n2


# add(1, 3)

# result = add(1, 3)
# print(result)


# def calculate(first_number, second_number, math_operation: str) -> None:
#     match math_operation:
#         case "+":
#             print(f"{first_number} {math_operation} {second_number} = {add(first_number, second_number)}")
#         case "-":
#             print(f"{first_number} {math_operation} {second_number} = {sub(first_number, second_number)}")
#         case "*":
#             print(f"{first_number} {math_operation} {second_number} = {mult(first_number, second_number)}")
#         case "/":
#             if second_number == 0:
#                 print("Cannot divide by zero")
#             else:
#                 print(f"{first_number} {math_operation} {second_number} = {division(first_number, second_number)}")
#         case _:
#             print("Invalid math operation!")
#
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# math_action = input("Enter math operation + - * / ")
#
# calculate(num1, num2, math_action)


########
# def say_hi(name, age):
#     return f"Hi. My name is {name} and I'm {age} years old"
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# print(say_hi("Alex", 32))
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print(say_hi("Frank", 68))
# print('ОК')

# assert 2 == 7, "my test 1"

####################

# def user_info(name: str = "noname", age: int = 18, hobby: str = "no hobby"):
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")


# user_info("Vasya", 33, "test")
# user_info("Vasya", 33)
# user_info("Vasya")
# user_info()
#
#
# user_info("walking", "Petya", 33)
# user_info(hobby="walking", name="Petya", age=33)

#####
## Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
# print_person(name="Bob", age=41, company="Microsoft")
#
#
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(name="Bob", age=41, company="Microsoft")

# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# є позиційними і можуть отримувати значення лише за позицією

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)
#
#
# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

####
# import random
#
# words = ["Dog", "Cat", "Helicopter", "Pyton", "Turtle", "Parrot"]
# secret_word = random.choice(words)
#
# encoded_word_letters = ["-"] * len(secret_word)
# attempts_counter = 0
#
# while True:
#     print(" ".join(encoded_word_letters))
#
#     if "".join(encoded_word_letters).lower() == secret_word.lower():
#         print(f"You guessed the secret word! Word: {secret_word}\nAttempts: {attempts_counter}.")
#         break
#
#     input_text = input("Enter a letter or full word: ").strip().lower()
#
#     attempts_counter += 1
#
#     if len(input_text) == 1:
#         if input_text.isalpha() and input_text in secret_word.lower():
#             for letter_index in range(len(secret_word)):
#                 if secret_word[letter_index].lower() == input_text:
#                     encoded_word_letters[letter_index] = input_text
#
#     elif input_text == secret_word.lower():
#         print(f"You guessed the secret word! Word: {secret_word}\nAttempts: {attempts_counter}.")
#         break
#
#     else:
#         print(f"You guessed wrong. Try again.")

# Добавить уровни сложности:
# 1. Легкий: кол-во попыток => кол-во букв * 2, если попытки закончились - конец игры.
# 2. Сложный: кол-во попыток => кол-во букв * 1.5, если попытки закончились - конец игры.

# letters = ["hello", "test", "a", "b"]
#
# separator = "-"
# result = separator.join(letters)
# print(result)
