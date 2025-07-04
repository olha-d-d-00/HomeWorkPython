class GroupLimitReachedException(Exception):
    def __init__(self, error_message, group_name):
        self.error_message = error_message
        self.group_name = group_name


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.gender} {self.age}'

    def show_info(self):
        print(self.__str__())


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f' {self.record_book}'

    def show_info(self):
        print(f"Name: {self.first_name} has {self.record_book}")


class Group:

    def __init__(self, number, student_limit=3):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) == self.student_limit:
            raise GroupLimitReachedException(f"Group limit {self.student_limit} reached", self.number)
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__() + '\n'
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza1', 'Taylor1', 'AN145')
st3 = Student('Female', 25, 'Liza2', 'Taylor2', 'AN145')
st4 = Student('Female', 25, 'Liza3', 'Taylor3', 'AN145')
gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    # gr.add_student(st4)

except GroupLimitReachedException as error:
    print(error)
except Exception as error:
    print(error)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
#
gr.delete_student('Taylor')  # No error!
#
#
# # Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# # На його основі створіть клас Студент (перевизначте метод виведення інформації).
# # Створіть клас Група, екземпляр якого складається з об'єктів класу Студент.
# # Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.
# # Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
# #
# # У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
# #
# # Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
# #
# # Нижче наведені заготовки, які необхідно доповнити.

#############################
# class Counter:
#     def __init__(self, current=1, min_value=0, max_value=10):
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def set_current(self, start):
#         if start < self.min_value or start > self.max_value:
#             raise ValueError(f"Incorrect value")
#         self.current = start
#
#     def set_max(self, max_max):
#         self.max_value = max_max
#
#     def set_min(self, min_min):
#         self.min_value = min_min
#
#     def step_up(self):
#         self.set_current(self.current + 1)
#
#     def step_down(self):
#         self.set_current(self.current - 1)
#
#     def get_current(self):
#         return self.current
#
#
# counter = Counter()
# counter.set_current(7)
# counter.step_up()
# counter.step_up()
# counter.step_up()
# print(counter.get_current())
# assert counter.get_current() == 10, 'Test1'
# try:
#     counter.step_up()  # ValueError
# except ValueError as e:
#     print(e)  # Достигнут максимум
# assert counter.get_current() == 10, 'Test2'
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# print(counter.get_current())
# assert counter.get_current() == 7, 'Test3'
# try:
#     counter.step_down()  # ValueError
# except ValueError as e:
#     print(e)  # Достигнут минимум
# assert counter.get_current() == 7, 'Test4'
# print(counter.get_current())

# Створити клас цифрового лічильника. У класі реалізувати методи:
#
# встановлення максимального значення лічильника,
# встановлення мінімального значення лічильника
# встановлення початкового значення лічильника
# метод step_up збільшує лічильник на 1. Метод можна викликати до тих пір, поки значення досягне максимуму.
# При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимумуʼ
# метод step_down зменшує лічильник на 1. Метод можна викликати до тих пір, поки значення не досягне мінімуму.
# При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що досягнутий мінімум
# повернення поточного значення лічильника
# Початкове, мінімальне та максимальне значення лічильника також можуть
# бути додані в метод ініціалізації екземпляра класу.
#
# Приблизний каркас для класу та варіанти перевірки. Вам потрібно дописати необхідне замість pass

#############
###
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

##
# import math
# print(-math.inf)
# print(math.inf)
# print(math.ceil(10.2))
# print(math.floor(10.999))
# print(math.factorial(5))
# print(math.pow(2, 3)) # 2 ** 3
# print(math.sqrt(9))

##
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
# #
# print(dt.datetime.now())
# dt_now = dt.datetime.now()
# print(f"{dt_now.day}/{dt_now.month}/{dt_now.year} {dt_now.hour}:{dt_now.minute}:{dt_now.second}:{dt_now.microsecond}")
# #
# print(dt.datetime)
# #
# my_date = dt.datetime.strptime("12/03/2020", "%d/%m/%Y")
# print(my_date)

# https://www.programiz.com/python-programming/datetime/strftime

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

# https://pynative.com/python-timezone/

####
# class NotPositiveNumberException(Exception):
#     def __init__(self, error_message, input_value):
#         self.error_message = error_message
#         self.input_value = input_value
#
#
# try:
#     number = int(input("Enter positive number: "))
#     if number < 0:
#         raise NotPositiveNumberException("Provided number is negative", number)
#     print(number)
# except NotPositiveNumberException as error:
#     print(error.args[0])
#     print(error.args[1])
# except Exception as error:
#     print(error)


