####
# Рекурсія – коли функція викликає сама себе
# 1. продумати, яке або які параметри функції будуть змінені при рекурсивному виклику
# 2. визначити умову або умови виходу з рекурсії
# 3. запустити рекурсію (виклик цієї ж функції)

# 5! => 1 * 2 * ... * 5
# def factorial(number):
#     if number <= 1:
#         return 1
#
#     # factorial(number - 1) -> запуск рекурсії
#     return number * factorial(number - 1)
#
#
# print(factorial(5))


# factorial(5) -> 5 * factorial(4) => 120
# factorial(4) -> 4 * factorial(3) => 24
# factorial(3) -> 3 * factorial(2) => 6
# factorial(2) -> 2 * factorial(1) => 2
# factorial(1) => 1

# Написати рекурсивну функцію знаходження ступеня числа.
# def my_pow(base, exponent):
#     if exponent <= 1:
#         return base
#
#     return base * my_pow(base, exponent-1)
#
#
# result = my_pow(2, 3)
# print(result)

# my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# my_pow(2, 1) => 2

###
# f(n) = f(n-1) + f(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# def fib(number):
#     if number == 0 or number == 1:
#         return number
#
#     return fib(number - 1) + fib(number - 2)
#
#
# print(fib(3))

# for i in range(10):
#     print(fib(i), end=" ")

##############
# # Приклад: Зіпувати два списки
# names = ['Alice', 'Bob', 'Charlie', 'David']
# ages = [25, 30, 22, 55]
# zipped_data = zip(names, ages)
# print(zipped_data)
# result = list(zipped_data)
# print(result)
# Вивід: [('Alice', 25), ('Bob', 30), ('Charlie', 22)]


# # Приклад: Застосувати функцію до парних чисел
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
# final_result = list(result)
# print(final_result)  # Вивід: [4, 16, 36, 64, 100]


# Приклад: Застосування квадратного кореня до кожного елемента списку
# def my_sqrl(number):
#     return number**2
#
#
# numbers = [1, 2, 3, 4, 5]
# # squared_root = map(lambda x: x**2, numbers)
# squared_root = map(my_sqrl, numbers)
# result = list(squared_root)
# print(result)  # Вивід: [1.0, 1.414, 1.732, 2.0, 2.236]

####
# Генератори колекцій
# list comprehension

# newlist = [expression for item in iterable (if condition)]

# iterable: джерело даних, що перебирається, в якості якого може виступати список, безліч, послідовність,
# або навіть функція, яка повертає набір даних, наприклад, range()
#
# item: елемент, що витягується з джерела даних
#
# expression: вираз, який повертає певне значення. Це значення потім потрапляє в список, що генерується
#
# condition: умова, якій повинні відповідати елементи, що витягуються з джерела даних.
# Якщо елемент НЕ задовольняє умову, він не вибирається. Необов'язковий параметр.

# # v1
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive = []
# for num in numbers:
#     if num > 0:
#         numbers_positive.append(num)
#
# print(numbers_positive)
# #
# # # v2
# numbers_positive_2 = [num for num in numbers if num > 0]
# print(numbers_positive_2)
#
# # #
# nums = [n for n in range(10)]
# print(nums)
#
# #
# nums = [n for n in range(10) if n % 2 == 0]
# print(nums)
#
# #
# users = {1: 'John', 2: 'Peter', 3: 'Max'}
# names = [name for name in users.values()]
# print(names)
#
# #
# users_data = [f"{key}: {users[key]}" for key in users.keys() if key > 2]
# print(users_data)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive_2 = tuple([num * 2 for num in numbers if num > 0])
# print(numbers_positive_2)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# new_numbers = [num * 2 if num > 5 else num for num in numbers if num > 0]
# print(new_numbers)
#
# # #
# my_dict = {i: i ** 2 for i in range(10)}
# print(my_dict)
#
# #
# my_set = {i for i in range(10)}
# print(my_set)

#################
# import random
# # from random import *
# # from random import randint, choice
#
# print(random.randint(1, 100)) # від 1 до 100
# print(random.random())
# print(random.choice("qwerty"))
# print(random.randrange(10)) # від нуля до 9
# print(random.randrange(2, 10)) # від 2 до 9
# print(random.randrange(2, 10, 2)) # від 2 до 9 через один (кожен другий)
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums) # перемішуємо значення списку
# print(nums)

###
# import math
#
# print(-math.inf)
# print(math.inf)
# print(math.ceil(10.2))
# print(math.floor(10.999))
# print(math.factorial(5))
# print(math.pow(2, 3))  # 2 ** 3
# print(math.sqrt(9))

# ##
# from decimal import *
#
# number = 0.1 + 0.1 + 0.1
# print(number)
# number = Decimal("0.1")
# number = number + number + number
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.00"))
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.0000"))
# print(number)
#
# number = Decimal("12.123456789")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.5555")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.9999")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# # округлення відбувається до найближчого парного числа, якщо округлена частина дорівнює 5
# number = Decimal("12.025")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)
#
# number = Decimal("12.035")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)

###
# datetime
# import datetime as dt
#
# print(dt.date.today())
# print(dt.date(2022, 11, 10))
# print(dt.time())
# print(dt.time(10, 13, 15))
# print(dt.time(10, 13))
# # #
# print(dt.datetime.now())
# dt_now = dt.datetime.now()
# print(f"{dt_now.day}/{dt_now.month}/{dt_now.year} {dt_now.hour}:{dt_now.minute}:{dt_now.second}:{dt_now.microsecond}")
# #
# print(dt.datetime)
# #
# my_date = dt.datetime.strptime("12/03/2020", "%d/%m/%Y")
# print(my_date)

# https://www.programiz.com/python-programming/datetime/strftime
#
# from datetime import datetime, timezone, timedelta
#
# # naive
# naive = datetime.now()
# print("Naive DateTime:", naive)
#
# # UTC aware
# UTC = datetime.now(timezone.utc)
# print("UTC DateTime", UTC)
#
# # Creating a datetime with JST (Japan) TimeZone
# jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
# print("In JST::", jst_dateTime)
#
# # https://pynative.com/python-timezone/
