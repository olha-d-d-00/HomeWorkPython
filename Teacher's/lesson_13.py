# import codecs
# import re
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         result = []
#         for line in file:
#             current_text_list = re.findall(r">(.+)</", line)  # <title>Жарт про функції</title>
#             if len(current_text_list) > 0:
#                 result += current_text_list
#         print(f"Result: {result}")
#         if len(result) > 0:
#             with open(result_file, 'w', encoding='utf-8') as new_file:
#                 new_file.write('\n'.join(result))
#
#
# delete_html_tags("draft.html")

##############################
# Обробка винятків

# v1
# n1, n2 = 10, 0 # множинне привласнення
# print(n1 / n2)

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))

# v2
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
#
#     print(f"Result: {result}")
#
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:  # Exception -> базовий тип виключення пишемо останнім з except
#     print(f"Exception occurred: {error}")
# finally:  # Відпрацьовує завжди. Писати по потребі
#     print("End of calculation")
#
# print("some text")

####
# try:
#     name = input("Enter you name: ")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter a valid name!")  # raise -> згенерувати виняток (кинути виняток)
# except Exception as e:
#     print(f"Error: {e}")


# У Python є такі базові типи винятків:
#
# BaseException: базовий тип для всіх вбудованих винятків
#
# Exception: базовий тип, який зазвичай застосовується для створення своїх типів винятків
#
# ArithmeticError: базовий тип для винятків, пов'язаних з арифметичними операціями
# (OverflowError, ZeroDivisionError, FloatingPointError).
#
# BufferError: Виняток, який виникає при неможливості виконати операцію з буфером
#
# LookupError: базовий тип для винятків, які виникають під час звернення до колекцій
# за некоректним ключем або індексом (наприклад, IndexError, KeyError)

# https://docs.python.org/3/library/exceptions.html

# IndexError: виняток виникає, якщо індекс при зверненні до елемента колекції знаходиться поза допустимим діапазоном
#
# KeyError: виникає, якщо у словнику немає ключа, за яким відбувається звернення до елемента словника.
#
# OverflowError: виникає, якщо результат арифметичної операції не може бути представлений поточним
# Чисельним типом (зазвичай типом float).
#
# RecursionError: виникає, якщо перевищено допустиму глибину рекурсії.
#
# TypeError: якщо операція або функція застосовується до значення неприпустимого типу.
# result = float(object())
# print(result)
# ValueError: виникає, якщо операція або функція одержують об'єкт коректного типу з некоректним значенням.
#
# ZeroDivisionError: виникає при розподілі на нуль.
#
# NotImplementedError: тип виключення для вказівки, що якісь методи класу не реалізовані
#
# ModuleNotFoundError: виникає при неможливості знайти модуль при його імпорті директивою import
#
# OSError: тип винятків, які генеруються при виникненні помилок системи (наприклад, неможливо знайти файл,
# пам'ять диска заповнена і т.д.)

# from datetime import datetime
#
#
# #####
# class InvalidNameException(Exception):
#
#     def __init__(self, *args):
#         # print(self.args)
#         self.log_error_data()
#
#     def log_error_data(self):
#         with open("log.txt", "a") as file:
#             error_message = f"{str(datetime.today())}: " + f"\n".join(self.args) + "\n"
#             file.write(error_message)
#
#
# try:
#     name = input("Enter you name: ")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise InvalidNameException(f"Please enter a valid name! You entered: {name}")
# # raise -> згенерувати виняток (кинути виняток)
# except Exception as e:
#     print(f"Error: {e}")

####################
# ООП - об'єктно орієнтоване програмування
# Клас - кастомний тип даних, який описує деякий об'єкт.
# Клас - креслення майбутнього екземпляра об'єкта.

# Інкапсуляція - приховування внутрішньої реалізації та надання санкціонованого доступу
# до інтерфейсу класу. Як чорна скринька.
# Абстрагуємося від внутрішньої реалізації.

# Спадкування - створення нового класу на основі вже існуючого.
# Розширення базового класу – дочірніми/дочірніми класами.
# Абстрагуємось від базового класу/класів, використовуючи дочірній клас.

# Поліморфізм - один інтерфейс та багато реалізацій.
# Абстрагуємося від конкретної реалізації

######################
# успадкування
# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     pass
#
#     # self -> используется, чтоб указать что поле/метод относится к экземпляру класса
#     def __init__(self, name, age):
#         self.name = name  # self.name -> поле класса (переменная класса)
#         self.age = age
#
#     def show_info(self):  # show_info -> метод класса (функция класса)
#         print(f"Name: {self.name}, Age: {self.age}")


# v1
# class Employee(Person):  # успадковуємося від класу Person
#     def work(self):
#         print(f"{self.name} works!")
#
#
# vasya = Employee("Vasya", 33)
# vasya.show_info()
# vasya.work()


# # v2
# class Employee(Person):
#     def __init__(self, name, age, company):
#         # v1
#         super().__init__(name, age)  # виклик конструктора базового класу Person
#         # super() -> посилання на базовий клас, отримуємо доступ до елементів базового класу
#         # v2
#         # Person.__init__(self, name, age)
#         self.company = company
#
#     # перевизначення методу
#     def show_info(self):
#         super().show_info()  # виклик методу базового класу
#         print(f"Works in {self.company} company")  # розширили своєю логікою
#
#
# vasya = Employee("Vasya", 33, "Google")
# vasya.show_info()

# Створити ієрархію класів для опису академії.
#
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):  # show_info -> метод класса (функция класса)
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# class Subject(object):
#     def __init__(self, name):
#         self.name = name
#
#
# class MathTopicSubject(Subject):
#     def __init__(self, name, test):
#         super().__init__(name)
#         self.test = test
#
#
# class Teacher(Person):
#     def __init__(self, name, age, subjects: list[Subject], experience: int):
#         super().__init__(name, age)
#         self.subjects = subjects
#         self.experience = experience
#
#
# class Student(Person):
#     def __init__(self, name, age, subject: Subject):
#         super().__init__(name, age)
#         self.subject = subject
#
#
# class Academy(object):
#     def __init__(self, name, subjects: list[Subject], teachers: list[Teacher], students: list[Student]):
#         self.name = name
#         self.subjects: list[Subject] = subjects
#         self.teachers: list[Teacher] = teachers
#         self.students: list[Student] = students
#
#
# current_subjects = [Subject("math"), Subject("english"), Subject("history")]
# current_teachers = [Teacher("Vasya", 33, current_subjects, 20),
#                     Teacher("Petya", 33, current_subjects, 10)]
# current_student = [Student("Vasya", 22, current_subjects[0]), Student("Alex", 44, current_subjects[2])]
# acad = Academy("Super academy", current_subjects, current_teachers, current_student)
#
# for teacher in acad.teachers:
#     teacher.show_info()

#####################
# v3
class Person(object):
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, workplace=None):
        super().__init__(name)
        self.workplace = workplace

    def work(self):
        print(f"{self.name} works!")

    def show_information(self):
        print(f"Info from {Employee} with name {self.name}")


class Student(Person):
    def __init__(self, name, university=None):
        super().__init__(name)
        self.university = university

    def study(self):
        print(f"{self.name} studies!")

    def show_information(self):
        print(f"Info from {Student} with name {self.name}")


class WorkingStudent(Student, Employee):  # множинне спадкування
    def __init__(self, name, workplace, university):
        Student.__init__(self, name, university)
        Employee.__init__(self, name, workplace)

    def show_information(self):
        Student.show_information(self)
        Employee.show_information(self)


vasya = WorkingStudent("Vasya", "Google", "California")
vasya.work()
vasya.study()
vasya.show_information()
print(WorkingStudent.mro())

# [<class '__main__.WorkingStudent'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class 'object'>]
