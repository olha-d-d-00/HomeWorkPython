# успадкування
# v1
# class Person:
#     __name = "noname"
#     __age = 18
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__secret = 12345  # (private) -> доступ тільки всередині класу
#         self._hobby = "no info"  # (protected) -> доступ усередині класу та в класах спадкоємців
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if len(name) > 2:
#             self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age > 18:
#             self.__age = age
#
#     @property
#     def hobby(self):
#         return self._hobby
#
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# v1
# class Employee(Person):  # успадковуємося від класу Person
#     def work(self):
#         print(f"{self.name} works!")
#         # print(self.__secret)  # AttributeError: 'Employee' object has no attribute '_Employee__secret'
#         print(self._hobby)  # є доступ так як у базовому класі це поле protected
#
#
# vasya = Employee("Vasya", 33)
# vasya.show_info()
# vasya.work()
# #
# # print(vasya._hobby)  # до protected полів не варто звертатися безпосередньо, краще використовувати геттер
# print(vasya.hobby)
# # print(vasya.__dict__)


# v2
# class Employee(Person):
#     def __init__(self, name, age, company):
#         # v1
#         super().__init__(name, age)  # виклик конструктора базового класу Person
#         # super() -> посилання на базовий клас, отримуємо доступ до елементів базового класу
#         # v2
#         # Person.__init__(self, name, age)
#         self.company = company
#
#     # def work(self):
#     #     print(f"{self.name} works in {self.company} company")
#     #     # print(self.__secret)  # AttributeError: 'Employee' object has no attribute '_Employee__secret'
#     #     # print(self._hobby)  # є доступ так як у базовому класі це поле protected
#     #     # print(super().show_info())
#     #     # print(super().name)
#
#     # перевизначення методу
#     def show_info(self):
#         super().show_info()  # виклик методу базового класу
#         print(f"Works in {self.company} company")  # розширили своєю логікою
#
#
# vasya = Employee("Vasya", 33, "Google")
# vasya.show_info()
# # vasya.work()

######
###
# v3
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def work(self):
#         print(f"{self.name} works!")
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print(f"{self.name} studies!")
#
#
# class WorkingStudent(Student, Employee):  # множинне спадкування
#     pass
#
#
# vasya = WorkingStudent("Vasya")
# vasya.work()
# vasya.study()
# print(WorkingStudent.mro())

# [<class '__main__.WorkingStudent'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class 'object'>]

# v4 приклад ромбоподібного наслідування
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"Name: {self.name}\nAge: {self.age}")
#
#
# class Employee(Person):
#     def __init__(self, name, age, company=None):
#         super().__init__(name, age)
#         self.company = company
#
#     def show_info(self):
#         super().show_info()
#         print(f"Company: {self.company}")
#
#
# class Student(Person):
#     def __init__(self, name, age, university=None):
#         super().__init__(name, age)
#         self.university = university
#
#     def show_info(self):
#         super().show_info()
#         print(f"University: {self.university}")
#
#
# class WorkingStudent(Student, Employee):
#     def __init__(self, name, age, company, university):
#         Student.__init__(self, name, age, university)
#         Employee.__init__(self, name, age, company)
#
#     def show_info(self):
#         super().show_info()
#         # Student.show_info(self)
#         # Employee.show_info(self)
#
#
# vasya = WorkingStudent("Vasya", 33, "Google", "Tech")
# vasya.show_info()
# # print(vasya.company)
# # print(vasya.university)
# print(WorkingStudent.mro())

##################
##
# https://makina-corpus.com/python/python-tutorial-understanding-python-mro-class-search-path
# http://www.srikanthtechnologies.com/blog/python/mro.aspx

#####
# доп задание: добавить инкапсуляцию
# class Transport:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def show_info(self):
#         print(f"Name: {self.name}\nYear: {self.year}")
#
#
# class BaseAuto(Transport):
#     def __init__(self, name, year, wheels_count=0):
#         super().__init__(name, year)
#         self.wheels_count = wheels_count
#
#     # перекрытие метода базового класса
#     def show_info(self):
#         print(f"Wheels count: {self.wheels_count}")
#
#
# class WaterTransport(Transport):
#     def __init__(self, name, year, displacement=0.):
#         super().__init__(name, year)
#         self.displacement = displacement
#
#     # перекрытие метода базового класса
#     def show_info(self):
#         print(f"Displacement: {self.displacement}")
#
#
# class Car(BaseAuto):
#     def __init__(self, name, year, wheels_count, doors_count=0):
#         super().__init__(name, year, wheels_count)
#         self.doors_count = doors_count
#
#     # перекрытие метода базового класса
#     def show_info(self):
#         print(f"Doors count: {self.doors_count}")
#
#
# class Amphibian(WaterTransport, BaseAuto):
#     def __init__(self, name, year, wheels_count, displacement):
#         WaterTransport.__init__(self, name, year, displacement)
#         BaseAuto.__init__(self, name, year, wheels_count)
#
#     # перекрытие метода базового класса
#     def show_info(self):
#         Transport.show_info(self)
#         WaterTransport.show_info(self)
#         BaseAuto.show_info(self)
#
#
# test_car = Amphibian("BMW", 2024, 4, 123.2)
# test_car.show_info()
# print(Amphibian.mro())

##################
# поліморфізм
# https://maxdrive.kyiv.ua/dokumentacija/pochta/chto-takoe-polimorfizm-v-python

# print(len("hello"))
# print(len([1, 3, 2, 5]))
# print(len({2, 5, 1, 6}))
# print(len({1: "one", 2: "two"}))

####
# class Parrot:
#     __name = "Kesha"
#
#     def fly(self):
#         print(f"Parrot {self.__name} can fly")
#
#     def swim(self):
#         print(f"Parrot {self.__name} can't swim")
#
#
# class Penguin:
#     __name = "Bobik"
#
#     def fly(self):
#         print(f"Penguin {self.__name} can't fly")
#
#     def swim(self):
#         print(f"Penguin {self.__name} can swim")
#
#
# class Zoo:
#     def __init__(self, animals: list):
#         self.animals = animals
#
#     def show_zoo_animals(self):
#         for animal in self.animals:
#             animal.fly()
#             animal.swim()
#             print()
#
#
# my_animals = [Parrot(), Penguin()]
# my_zoo = Zoo(my_animals)
# my_zoo.show_zoo_animals()

####
class Triangle(object):
    __name = "Triangle"

    def show_info(self):
        print(f"This is {self.__name}")


class Circle(object):
    __name = "Circle"

    def show_info(self):
        print(f"This is {self.__name}")


class Rectangle(object):
    __name = "Rectangle"

    def show_info(self):
        print(f"This is {self.__name}")


def get_geometry_figures_info(geom_figures):
    for geom in geom_figures:
        geom.show_info()


get_geometry_figures_info([Rectangle(), Circle(), Rectangle(), Triangle()])
