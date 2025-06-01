# def hello(name, age=18, hobby="No hobby") -> None:
#     print(f"Name: {name}, Age: {age}, Hobby: {hobby}")
#
#
# hello("John", 30, "Python")
# hello("John", 30)
# hello("John")
#
# hello(hobby="Python", name="John", age=30)

#########
# def hello(): print("Hello")
#
#
# print(hello)
# message = hello  # надав посилання на функцію в іншу змінну
# print(message)
#
# hello()
# message()

##################
# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mult(a, b): return a * b
# def division(a, b): return a / b
#
#
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return add
#         case "-":
#             return sub
#         case "*":
#             return mult
#         case "/":
#             return division
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 0)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

#####
# button=lambda: print("Hello world!")
# button=add

# def test(number):
#     return number
#
#
# click=lambda: test(2)

#####
# def test(): print("Hello world!")
#
#
# message = lambda: print("Hello world!")
# message()
# message()
# print(message)
# print(lambda: print("Hello world!"))


####
# square = lambda side_1, side_2: side_1 * side_2
# print(square(2, 4))
# print((lambda side_1, side_2: side_1 * side_2)(5, 2))

# def calculate(a, b, math_operation) -> None:
#     print(math_operation)
#     print(f"Result: {math_operation(a, b)}")
#
#
# calculate(2, 5, lambda n1, n2: n1 + n2)
# calculate(2, 5, lambda n1, n2: n1 / n2)

###
# def select_math_operation(user_choice):
#     match user_choice:
#         case "+":
#             return lambda a, b: a + b  # повернення посилання на функцію
#         case "-":
#             return lambda a, b: a - b
#         case "*":
#             return lambda a, b: a * b
#         case "/":
#             return lambda a, b: a / b
#         case _:
#             raise Exception("Invalid operation!")
#
#
# try:
#     operation = input("Enter math operation: ")
#     math_operation = select_math_operation(operation)
#     result = math_operation(4, 9)
#     print(f"Result: {result}")
# except Exception as error:
#     print(error)

####
# LEGB - почитати
# https://www.bestprog.net/uk/2020/07/29/python-the-scopes-of-names-in-python-local-names-visibility-rules-for-names-legb-rule-the-global-keyword-overriding-names-in-functions-ua/

#####
# області видимості
# number = 10
# #
# #
# def test() -> None:
#     number = 11  # перекриття глобальної змінної
#
#     if 1:
#         # number = 12
#
#         if 1:
#             # number = 13
#             num = 20
#             print(number)
#     print(number)
#     print(num)
#
#
# print(number)
# test()
# print(number)
# number = 35
# print(number)

##########
# number = 10
#
#
# def test():
#     global number
#
#     number = 11  # змінюємо значення глобальної змінної
#     print(number)
#
#
# print(number)
# test()
# print(number)

#########
# def outer():
#     number = 1
#
#     def inner():
#         nonlocal number
#         number = 2
#         print(number)
#
#     inner()
#     print(number)
#
#
# outer()
#############
###

# number = 10
#
#
# def outer():
#     global number
#     number = 1
#     new_number = number
#
#     def inner():
#         global number
#         # nonlocal new_number
#         new_number = 2
#         # print(new_number)
#         my_test = 111
#         number = 2
#
#         def inner_number_2():
#             global number
#             nonlocal new_number
#             nonlocal my_test
#             new_number = 3
#             print(new_number)
#             print(my_test)
#             number = 3
#
#         inner_number_2()
#
#     inner()
#     print(new_number)
#
#
# outer()
# print(number)


# import math
#
#
# # #####
# def get_list_with_min_avg(input_data):
#     def get_avg(input_list):
#         return sum(input_list) / len(input_list)
#
#     min_avg = math.inf
#
#     for nums_list in input_data:
#         current_avg = get_avg(nums_list)
#         if min_avg > current_avg:
#             min_avg = current_avg
#
#     return min_avg
#
#
# data = [
#     [1, 2],
#     [3, 1],
#     [0, 4]
# ]
# print(get_list_with_min_avg(data))

###########
# def show_info(number, *args, text="no text"):
#     print(number)
#     print(args)
#     print(text)
#
#
# show_info(10, 2, 3, 4, 5, 6, 7, 8, 9, text="hello")


# def show_info(**kwargs):
#     print(kwargs)
#
#
# show_info(one=1, two=2, three=3, test="hello")

#
#
# def show_info(num, *args, data="test", **kwargs):
#     print(num)
#     print(args)
#     print(data)
#     print(kwargs)
#
#
# show_info(100, 2, "hello", 1234, 3456, data="my data", number=10, text="hello")

####
# def show_info(name, age, hobby):
#     print(f'Name: {name}, Age: {age}, Hobby: {hobby}')
#
#
# user_data = ["Vasya", 123, "Test"]
# # v1
# show_info(user_data[0], user_data[1], user_data[2])
# # v2 (распаковка)
# show_info(*user_data)
#
# user_data = {
#     "name": "Petya",
#     "age": 33,
#     "hobby": "My hobby"
# }
#
# # v1
# show_info(user_data.get("name"), user_data.get("age"), user_data.get("hobby"))
# # v2 (распаковка)
# show_info(**user_data)

###########
# 1. Створити список чисел.
# - Заберіть дублікати значень.
# - Вивести унікальні значення.

# import random
#
#
# def create_list_with_random_numbers(list_length=10, start_value=1, end_value=5) -> list[int]:
#     return [random.randint(start_value, end_value) for _ in range(list_length)]
#
#
# def remove_duplicates(numbers: list[int]) -> list[int]:
#     return list(set(numbers))
#
#
# def get_unique_values(numbers: list[int]) -> list[int]:
#     # v1
#     # unique_numbers = []
#     # for number in numbers:
#     #     if numbers.count(number) == 1:
#     #         unique_numbers.append(number)
#     #
#     # return unique_numbers
#
#     # v2
#     return [number for number in numbers if numbers.count(number) == 1]
#
#
# numbers_list = create_list_with_random_numbers()
# print(numbers_list)
# result = remove_duplicates(numbers_list)
# print(result)
#
# print(numbers_list)
# result = get_unique_values(numbers_list)
# print(result)

#############
# import random
#
# source_words = ["good", "interesting", "cool", "amazing", "fine"]
#
# COMMENT_LENGTH = 3
#
# result_words = [source_words[random.randint(0, len(source_words) - 1)] for i in range(COMMENT_LENGTH)]
#
# final_comment = "This film is very " + ", ".join(set(result_words)) + " ☺"
#
# print(final_comment)

