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

################################################################
# статичний метод (функція), поле (змінна) відносяться до класу, і до екземпляра
# статичний ел-т можна використовувати не створюючи екземпляр класу
# Найчастіше статичні класи використовують для опису конфігів та інших службових об'єктів, там де немає сенсу
# створювати екземпляри
# class Test:
#     MyStaticData = "static data"
#
#     # конструктор без параметрів (не за замовчуванням)
#     # def __init__(self):
#     #     self.text = "some text"
#
#     # конструктор класу - створює екземпляр об'єкту
#     # def __new__(cls):
#     #     pass
#
#     # для ініціалізації об'єкту
#     # якщо явно не визначити конструктор __new__ -> то __init__ він створиться автоматично
#     # def __init__(self):
#     #     pass
#
#     def __init__(self, text):
#         self.text = text
#
#     def show_info(self):
#         print(self.text)
#
#     @staticmethod
#     def show():
#         print("this is test class")
#         # print(self.text)
#
#
# my_test1 = Test("my text 1")
# my_test1.show()
# my_test1.show_info()
#
# my_test2 = Test("my text 2")
# my_test2.show()
# my_test2.show_info()
#
# # Test.show_info()
# Test.show()
# print(Test.MyStaticData)

##
# class Person:
# # __init__ Конструктор класу – дозволяє створити екземпляр класу. Можливо з параметрами та без параметрів.
# # self - посилання на контекст класу, екземпляр класу
# # контекст класу - все що є частиною класу (экземпляра) -
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_person(self):
#         print(f"Name: {self.name} age: {self.age}")
#
#
# user1 = Person("Vasya", 33)
# user2 = Person("Petya", 44)
# user1.show_person()
# user2.show_person()
# print(user1.name)
# user1.name = ""
# print(user1.name)
# user1.show_person()
# # Person.show_person(user2)

#
# інкапсуляція
# v1
# class User:
#     __name: str = "no name"  # private поле, доступне тільки всередині цього класу
#     __age: int = 0
#     __secret: int = 12345
#
#     def __init__(self, name=None, age=None):
#         # self.__name = name
#         # self.__age = age
#         # застосуємо інкапсуляцію
#         self.set_age(age)
#         self.set_name(name)
#
#     def set_name(self, name):
#         if 2 < len(name) < 50:
#             self.__name = name
#         else:
#             print("Incorrect name length!")
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, age):
#         if 18 < age < 150:
#             self.__age = age
#         else:
#             print("Incorrect age!")
#
#     def get_age(self):
#         return self.__age
#
#     def show_info(self):
#         print(f"Name: {self.__name} age: {self.__age}")
#         self.__secret_info()
#
#     def __secret_info(self):
#         print(f"Secret code: {self.__secret}")


# vasya = User("Vasya", -44)
# vasya.show_info()
# vasya.set_age(100)
# vasya.show_info()
# vasya.set_age(-100)
# vasya.show_info()
# # print(vasya.__name)
# # vasya.__secret_info()
# vasya._User__secret_info()  # так робити не треба так як це ламає інкапсуляцію

###
# vasya = User("Vasya", 33)
# # print(vasya.__name)
# # # подводный камень ниже!
# vasya.__name = "qqqq"
# print(vasya.__name)  # динамічно створилося нове поле в цьому примірнику, але це поле не має жодного відношення до
# # # приватному полю __name яке ми створили у класі
# vasya.hobby = "wwww"
# print(vasya.hobby)
# vasya.show_info()
# #
# print(vasya.__dict__)
# #
# petya = User("Petya", 55)
# petya.show_info()
# #
# print(petya.__dict__)

##
# v2 реалізація інкапсуляції використовуючи анотації властивостей
class User:
    __name: str = "no name"  # private поле, доступне тільки всередині цього класу
    __age: int = 0
    __secret: int = 12345

    def __init__(self, name=None, age=None):
        # self.__name = name
        # self.__age = age
        # застосуємо інкапсуляцію
        self.name = name  # setter
        self.age = age  # setter

        print(self.name)  # getter

    # getter - для отримання значення приватного поля
    @property
    def name(self):
        return self.__name

    # setter - для санкціонованого доступу до приватної змінної (поля)
    @name.setter
    def name(self, name):
        if 2 < len(name) < 50:
            self.__name = name
        else:
            print("Incorrect name length!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 < age < 150:
            self.__age = age
        else:
            print("Incorrect age!")

    # public method - публічна (доступна зовні) функція
    def show_info(self):
        print(f"Name: {self.__name} age: {self.__age}")
        # self.__secret_info()

    # private method - приватна (недоступна зовні) функція
    def __secret_info(self):
        print(f"Secret code: {self.__secret}")


anton = User("Anton", -34)
anton.show_info()
anton.age = 40
anton.show_info()
anton.age = 400
anton.show_info()
print(anton.name)

##
# class MyConverter:
#     __money_sum = 0
#     __uah_rate = 41.3
#     __converter_direction = 1
#
#     def __init__(self, input_money, convert_dir):
#         self.money_sum = input_money
#         self.converter_direction = convert_dir
#
#     @property
#     def converter_direction(self):
#         return self.__converter_direction
#
#     @converter_direction.setter
#     def converter_direction(self, convert_dir):
#         if convert_dir == 1 or convert_dir == 2:
#             self.__converter_direction = convert_dir
#         else:
#             raise Exception("Provide correct converter direction!")
#
#     @property
#     def money_sum(self):
#         return self.__money_sum
#
#     @money_sum.setter
#     def money_sum(self, input_sum):
#         if 0 < input_sum < 1000000000:
#             self.__money_sum = input_sum
#         else:
#             raise Exception("Provide valid money sum!")
#
#     # readonly property
#     @property
#     def uah_rate(self):
#         return self.__uah_rate
#
#     def show_uah_rate(self):
#         print(f"Current UAH rate: {self.__uah_rate}")
#
#     def show_result(self):
#         print(self.__getMoneyResult())
#
#     def __getMoneyResult(self):
#         match self.__converter_direction:
#             case 1:
#                 return f"{self.__money_sum} UAH = {self.__get_usd_sum()} USD"
#             case 2:
#                 return f"{self.__money_sum} USD = {self.__get_uah_sum()} UAH"
#             case _:
#                 raise Exception("Incorrect converter direction!")
#
#     def __get_usd_sum(self):
#         return self.__money_sum / self.__uah_rate
#
#     def __get_uah_sum(self):
#         return self.__money_sum * self.__uah_rate
#
#
# try:
#     converter = MyConverter(5000, convert_dir=2)
#     converter.show_result()
# except Exception as error:
#     print(error)
#
#
# ######################
# class Person:
#     __name = "no name"
#     __age = 18
#
#     def __init__(self, name, age, hobby="no hobby"):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, username):
#         if 2 < len(username) < 30:
#             self.__name = username
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, user_age):
#         if 18 <= user_age < 150:
#             self.__age = user_age
#
#     def show_info(self):
#         print(f"Name: {self.__name} age: {self.__age}")
#
#
# class Company:
#     __name = "demo name"
#
#     def __init__(self, company_name: str, users: list[Person] = None):
#         self.__name = company_name
#         self.users: list[Person] = users
#
#     def show_users(self):
#         print(f"Found {len(self.users)} users")
#         for user in self.users:
#             user.show_info()
#
#     def add_user(self, new_user: Person):
#         if isinstance(new_user, Person):
#             self.users.append(new_user)
#             return
#         raise Exception(f"Provided value with incorrect type: {type(new_user)}!")
#
#
# try:
#     users: list = [Person("Vasya", 33), Person("Petya", 44), Person("Anton", 55)]
#     google = Company("Google", users)
#     google.show_users()
#     google.add_user(Person("Anton111", 66))
#     google.show_users()
#     google.add_user("test")
# except Exception as error:
#     print(error)

#
# ################
# text = "To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer." \
#                      " The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles," \
#                      " And by opposing end them? To die: to sleep; No more; and by a sleep to say we end." \
#                      " The heart-ache and the thousand natural shocks That flesh is heir to," \
#                      " 'tis a consummation Devoutly to be wish'd. To die, to sleep"
#
#
# word_to_replace = "die"
# stars = "*" * len(word_to_replace)
# words_count = text.count(word_to_replace)
# updated_text = text.replace(word_to_replace, stars)
#
# print(f"Words {word_to_replace} count: {words_count}")
# print("Updated text: ")
# print(updated_text)
