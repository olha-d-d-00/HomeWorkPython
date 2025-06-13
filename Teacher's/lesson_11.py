###
import random


def generate_random_list(list_len, start_value=1, end_value=100):
    # v1
    # nums = []
    # for i in range(list_len):
    #     nums.append(random.randint(start_value, end_value))
    #
    # return nums

    # v2
    return [random.randint(start_value, end_value) for _ in range(list_len)]


def bubble_sort(nums):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # зберігаємо посилання на індекс попереднього значення
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # вставка елемента
        nums[j + 1] = item_to_insert


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # порівнюємо перші елементи на початку кожного списку
            # якщо перший елемент лівого підписку менший - додаємо його
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                # інакше додамо з правого підписку
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # якщо досягнуто кінця лівого списку - елементи правого списку додамо до кінця sorted_list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    middle_index = len(nums) // 2

    left_list = merge_sort(nums[:middle_index])
    right_list = merge_sort(nums[middle_index:])

    return merge(left_list, right_list)


def partition(nums, low_index, high_index):
    # вибираємо середній елемент як опорний
    # так само можливий вибір першого, останнього або довільного ел-тов як опорного
    pivot = nums[(low_index + high_index) // 2]
    i = low_index - 1
    j = high_index + 1

    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Якщо елемент з індексом i (ліворуч від опорного) більше ніж елемент з індексом j (праворуч від опорного) -
        # то міняємо їх місцями
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # допоміжна функція
    def _quick_sort(items, low_index, high_index):
        if low_index < high_index:
            split_index = partition(items, low_index, high_index)
            _quick_sort(items, low_index, split_index)
            _quick_sort(items, split_index + 1, high_index)

    _quick_sort(nums, 0, len(nums) - 1)


def linear_search_from_start(nums, search_item) -> int:
    for i in range(len(nums)):
        if nums[i] == search_item:
            return i
    return -1


def linear_search_from_end(nums, search_item) -> int:
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == search_item:
            return i
    return -1


# бінарний пошук працює ТІЛЬКИ на відсортованому масиві
def binary_search(nums, search_item) -> int:
    first_index = 0
    last_index = len(nums) - 1

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        if nums[middle_index] == search_item:
            return middle_index
        else:
            if search_item < nums[middle_index]:
                last_index = middle_index - 1
            else:
                first_index = middle_index + 1

    return -1  # -1 означає, що значення не знайдено


# my_list = generate_random_list(5)
# print(my_list)
# # bubble_sort(my_list)
# # selection_sort(my_list)
# # insertion_sort(my_list)
# # my_list = merge_sort(my_list)
# quick_sort(my_list)
# print(my_list)
#
# numbers = [1, 4, 10, 5, 2, 10, 4, 10, 3]
# numbers.sort()
# numbers = list(set(numbers))
# print(numbers)
# value = 10
# # result = linear_search_from_start(numbers, value)
# # result = linear_search_from_end(numbers, value)
# result = binary_search(numbers, value)
#
# if result != -1:
#     print(f"{value} found on index: {result}")
# else:
#     print(f"{value} not found!")

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
pattern = r"^\+?\d{1,3}\s?\d{1,5}\s?\d{5,8}$"
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
# pattern = r"^[a-zA-Z]+[._]?[a-zA-Z0-9]+[@][a-zA-Z]+[.][a-zA-Z]{2,}$"
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
# expression = ""
# pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"
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
