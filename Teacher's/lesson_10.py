# def additional_logic(func):
#     def wrapper():
#         print("Some logic 1")
#         func()
#         print("Some logic 2")
#     return wrapper
#
#
# @additional_logic
# def hello():
#     print("Hello World!")
#
#
# hello()

####
# def check_permissions(func):
#     def wrapper(role):
#         if role == 'admin':
#             print("Permissions granted!")
#             func(role)
#         else:
#             print("Permission denied!")
#     return wrapper
#
#
# @check_permissions
# def get_secret_information(user_role):
#     print(f"Hi {user_role}, this is secret information.")


# v1
# wrapper_function = check_permissions(get_secret_information)
# wrapper_function("user")

# v2
# check_permissions(get_secret_information)("admin")

# get_secret_information("user")
# get_secret_information("admin")

####
# def start(func):
#     def wrapper1(name):
#         print("Hello ", end="")
#         func(name)
#     return wrapper1
#
#
# def end(func):
#     def wrapper2(name):
#         print("Goodbye ", end="")
#         func(name)
#     return wrapper2
#
#
# @start
# @end
# def hello(name):
#     print(name)
#
#
# hello("Vasya")

##
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
#
# printer("Hello")

####################
# import time
#
#
# current_working_status = False
# current_seconds = 1
#
#
# def delay(seconds=0, is_working=True):
#     def decorator(func):
#         if not is_working:
#             return func
#         # if seconds < 0:
#         #     return func
#
#         def wrapper(*args, **kwargs):
#             print(f"Waiting for {seconds} seconds...")
#             time.sleep(seconds)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @delay(current_seconds, current_working_status)
# def hello():
#     print("Hello")
#
#
# hello()

#########################
# closure - замыкание

# 1. вложенные функции
# 2. внешняя функция возвращает адрес вложенной функции
# 3. вложенная функция должна использовать хотя бы одну переменную из внешней функции

# def outer():
#     number = 0
#     number2 = 20
#     number3 = 30
#
#     print(number2)
#
#     def inner():
#         nonlocal number
#         number += 1
#         print(number)
#         print(number3)
#         print("*" * 10)
#
#     return inner
#
#
# result_func1 = outer()
# result_func1()
# result_func1()
# #
# #
# result_func2 = outer()
# result_func2()
# result_func2()
# #
# # print("---------------")
# # result_func1()
# # result_func2()


##########
# add = lambda num1: lambda num2: num1 + num2
#
# configured_add = add(3)
#
# for i in range(1, 10):
#     print(configured_add(i))

#######################
# Генераторні функції
# Генератор - це об'єкт, який відразу при створенні не обчислює значення всіх своїх елементів
# generator = (i for i in range(3))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))  # StopIteration
# close() -> зупинка генератора
# throw() -> генератор кине виняток

# for i in generator:
#     print(i)


# def create_generator():
#     number = 1
#     while True:
#         yield number
#         number += 1
#
#
# my_gen = create_generator()
# # print(my_gen)
# # print(next(my_gen))
# # print(next(my_gen))
# # print(next(my_gen))
# # print(next(my_gen))
# # #
# try:
#     for i in my_gen:
#         print(i)
#         if i > 10:
#             my_gen.close()
#             # my_gen.throw(Exception("End!"))
# except Exception as e:
#     print(e)

#########

##################
# \d - відповідає будь-якій одній цифрі і замінює собою вираз [0-9];
# \D - виключає всі цифри та замінює [^0-9];
# \w - Замінює будь-яку цифру, букву, а також знак нижнього підкреслення;
# \W - будь-який символ крім латиниці, цифр або нижнього підкреслення;
# \s - відповідає будь-якому пробельного символу;
# \S - описує будь-який непробільний символ.
#
#
# . Один символ, крім нового рядка \n.
# ? 0 або 1 входження шаблону зліва
# + 1 і більше входжень шаблону зліва
# * 0 і більше входжень шаблону зліва
# \w Будь-яка цифра або буква (\W - все, крім букви або цифри)
# \d Будь-яка цифра [0-9] (\D - все, крім цифри)
# \s Будь-який символ пробілу (\S - будь-який символ пробілу)
# \b Кордон слова
# [..] Один із символів у дужках ([^..] — будь-який символ, крім тих, що у дужках)
# \ Екранування спеціальних символів (\. означає точку або \+ - знак "плюс")
# ^ і $ Початок і кінець рядка відповідно
# {n,m} Від n до m входжень ({,m} - від 0 до m)
# a|b Відповідає a або b
# () Групує вираз і повертає знайдений текст
# \t, \n, \r Символ табуляції, нового рядка та повернення каретки відповідно
#
# Для чого використовуються регулярні вирази
# для визначення потрібного формату, наприклад, телефонного номера або email-адреси;
# для розбивки рядків на підрядки;
# для пошуку, заміни та вилучення символів;
# для швидкого виконання нетривіальних операцій.
#
# А ось найбільш популярні методи, які надає модуль:
#
# re.match() - Цей метод шукає за заданим шаблоном на початку рядка
# re.search() - Метод схожий на match(), але шукає не лише на початку рядка
# re.findall() - Повертає список усіх знайдених збігів.
# У методу findall() немає обмежень на пошук на початку або в кінці рядка.
# re.split() - Цей метод поділяє рядок за заданим шаблоном
# re.sub() - Шукає шаблон у рядку і замінює його на вказаний підрядок.
# Якщо шаблон не знайдено, рядок залишається незмінним
# re.compile() - Ми можемо зібрати регулярне вираження в окремий об'єкт, який можна використовувати для пошуку.
# Це також позбавляє переписування одного і того ж виразу.

import re


# result = re.match(r'he', 'hello world hello')
# print(result)
# print(result.group(0))
# #
# #
# result = re.search(r'world', 'hello world hello')
# print(result.start())
# print(result.end())
# #
# #
# result = re.findall(r'he', 'hello world hello')
# print(result)
# #
# #
# result = re.split(r'l', 'hello world hello', maxsplit=1)
# print(result)
# #
# result = re.split(r'l', 'hello world hello')
# print(result)  # ['he', '', 'o wor', 'd he', '', 'o']
# #
# #
# pattern = re.compile('hello')
# result = pattern.findall('hello world hello')
# print(result)

# result = re.findall(r'.', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w*', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+$', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'^\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\b\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'@\w+.\w+', "test1@gmail.com, test2@qqq.com, test3@www.com")
# print(result)
#
# result = re.findall(r'@\w+.(\w+)', "test1@gmail.com, test2@qqq.ua, test3@www.com")
# print(result)
#
# result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-017-2004')
# print(result)

# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# - домашній номер телефону (тільки цифри та довжина номера)
#
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
#
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
#
# додатково:
#
# - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ,
# довжина пароля – від 8 до 16 символів)



# # """
# # Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# # - домашній номер телефону (тільки цифри та довжина номера)
# # - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# # - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# # - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
# # додатково:
# # - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра,
# # один символ, довжина пароля – від 8 до 16 символів)
# # """
# #
import re
import random
import string

MIN_SIZE_PASSWORD = 8
MAX_SIZE_PASSWORD = 16


def generate_password(length: int = MIN_SIZE_PASSWORD) -> str:
    """
    Генерує пароль, який відповідає наступним вимогам:
    - мінімум одна велика літера
    - мінімум одна маленька літера
    - мінімум одна цифра
    - мінімум один символ
    - загальна довжина пароля - від 8 до 16 символів (за замовчуванням 8)
    """
    if not (MIN_SIZE_PASSWORD <= length <= MAX_SIZE_PASSWORD):
        print(f"Довжина пароля повинна бути від {MIN_SIZE_PASSWORD} до {MAX_SIZE_PASSWORD} символів")
        return
        # raise ValueError(f"Довжина пароля повинна бути від {MIN_SIZE_PASSWORD} до {MAX_SIZE_PASSWORD} символів")

    # Визначаємо набори символів
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "@$!%*?&"

    # Гарантуємо наявність хоча б одного символу з кожного набору
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Додаємо випадкові символи для досягнення бажаної довжини пароля
    all_chars = lower + upper + digits + symbols
    password += [random.choice(all_chars) for _ in range(length - 4)]

    # Перемішуємо символи, щоб уникнути передбачуваності
    random.shuffle(password)

    # Повертаємо пароль як рядок
    return ''.join(password)


def validation(pattern: str, expression: str) -> bool:
    return bool(re.match(pattern, expression))
    # Повертає True, якщо вираз відповідає шаблону, інакше - False

#
# 1.
# expression = ""
# pattern = r"^\d{5,7}$"
# print("1. Home phone number can be from 5 to 7 digits long.")
# while not validation(pattern, expression):
#     expression = input("Enter your home phone number to verify: ")
#     if not validation(pattern, expression):
#         print("Validation Error. Please try again.")
#     else:
#         print(f"Validation OK. Number {expression} is valid. It looks like your home phone.")
# print()
#
# # 2.
# pattern = r"^\+?\d{1,3}\s?\d{1,5}\s?\d{5,8}$"
# # """
# # Код країни в міжнародних номерах зазвичай складається з 1 до 3 цифр. Довжина коду країни залежить від конкретної
# # країни і може змінюватись.
# # Код оператора мобільного зв'язку або міста у телефонних номерах може складатися з різної кількості цифр, залежно
# # від країни та конкретної телефонної системи. Загалом, для мобільних операторів та міських телефонних систем кількість
# # цифр у коді може змінюватись від 1 до 5.
# # Локальний номер телефону без урахування коду країни та коду оператора або міста зазвичай складається з 5 до 8 цифр,
# # залежно від країни та конкретної телефонної системи.
# # """
# print("2. Mobile phone number can be from 10 to 12 digits long and may optionally contain + at the beginning"
#       " or spaces after the country code and operator code.")
# expression = ""
# while not validation(pattern, expression):
#     expression = input("Enter your mobile phone number to verify: ")
#     if not validation(pattern, expression):
#         print("Validation Error. Please try again.")
#     else:
#         print(f"Validation OK. Number {expression} is valid. It looks like your mobile phone.")
# print()
#
# # 3.
# expression = ""
# pattern = r"^[a-zA-Z0-9]+[._]?[a-zA-Z0-9]+[@][a-zA-Z]+[.][a-zA-Z]{2,}$"
# # ^[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}$
# # Цей патерн розбивається на такі частини:
# # ^[a-zA-Z0-9._%+-]+ - початок рядка повинен містити один або більше символів, які можуть бути літерами (a-z, A-Z),
# # цифрами (0-9), точками (.), підкресленнями ( _), відсотками (%), плюсами (+) чи мінусами (-).
# # @ - символ собаки, що розділяє ім'я користувача та домен поштового сервісу.
# # [a-zA-Z0-9.-]+ - доменне ім'я, що складається з літер, цифр, точок або дефісів.
# # \. - точка, що відокремлює доменне ім'я від доменного суфікса.
# # """[a-zA-Z]{2,} - доменний суфікс, що складається з двох або більше букв (наприклад, "com", "org", "net").
# # Це базовий патерн і він підходить для більшості звичайних адрес електронної пошти, проте варто зауважити, що існують
# # специфічні випадки адрес, які можуть не задовольняти цей вираз через особливі символи або нові доменні зони.
# print("3. Example for e-mail address : press@google.com")
# while not validation(pattern, expression):
#     expression = input("Enter your e-mail adress to verify: ")
#     if not validation(pattern, expression):
#         print("Validation Error. Please try again.")
#     else:
#         print(f"Validation OK. Expression {expression} is valid. It looks like e-mail adress.")
# print()
#
# # 4.
# expression = ""
# pattern = r"^([A-Za-zА-Яа-яҐЄІЇґєії]{2,20}\s){2}[A-Za-zА-Яа-яҐЄІЇґєії]{2,20}$"
# print("4. Last name, first name and patronymic of the client (3 words, minimum 2 char, maximum 20 char).")
# while not validation(pattern, expression):
#     expression = input("Enter last name, first name and patronymic of the client to verify: ")
#     if not validation(pattern, expression):
#         print("Validation Error. Please try again.")
#     else:
#         print(
#             f"Validation OK. Expression {expression} is valid. It looks like last name, first name and patronymic of the client.")
# print()

# # 5.
expression = ""
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"
# # Розшифровка компонентів цього виразу:
# # ^ і $ - позначають початок і кінець рядка відповідно, що гарантує перевірку всього рядка.
# # (?=.*[a-z]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї маленької літери.
# # (?=.*[A-Z]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї великої літери.
# # (?=.*\d) - позитивна попередня перевірка, щоб забезпечити наявність хоча б однієї цифри.
# # (?=.*[@$!%*?&]) - позитивна попередня перевірка, щоб забезпечити наявність хоча б одного символу з вказаного набору.
# # [A-Za-z\d@$!%*?&]{8,16} - вказує на те, що дозволені літери (великі та маленькі), цифри та символи з вказаного набору,
# # а довжина рядка має бути від 8 до 16 символів.
# # Цей регулярний вираз гарантує, що пароль буде відповідати всім вказаним вимогам: міститиме велику та маленьку літери,
# # цифру, спеціальний символ і матиме довжину від 8 до 16 символів.
# print(f"5. Password (minimum: one capital letter, one small letter, one number, one symbol, password length -"
#       f" from {MIN_SIZE_PASSWORD} to {MAX_SIZE_PASSWORD} characters). Example for password:"
#       f" {generate_password()}")
# while not validation(pattern, expression):
#     expression = input("Enter your home password to verify: ")
#     if MIN_SIZE_PASSWORD <= len(expression) <= MAX_SIZE_PASSWORD:
#         if not validation(pattern, expression):
#             print("Validation Error. Please try again.")
#         else:
#             print(f"Validation OK. Expression {expression} is valid. It looks like your password.")
#     else:
#         print("Validation Error. Please try again.")
# print()

