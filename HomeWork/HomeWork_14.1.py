class GroupLimitError(Exception):
    def __init__(self, message="Group can contain only 10 students"):
        super().__init__(message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o.'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()} | Record Book: {self.record_book}'

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))

    def __eq__(self, other):
        return (self.first_name, self.last_name, self.record_book) == \
               (other.first_name, other.last_name, other.record_book)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError(f"Cannot add student {student.first_name} {student.last_name}: group limit reached.")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(s) for s in self.group)
        return f'Number: {self.number}\n{all_students}'


gr = Group('PD1')

# добавляю 10 студентов
for i in range(10):
    student = Student('Male', 20 + i, f'Name{i}', f'LastName{i}', f'RB{i}')
    gr.add_student(student)

print(gr)

# обработка исключения при добавлении 11 студента
extra_student = Student('Female', 23, 'Extra', 'Student', 'RB999')
try:
    gr.add_student(extra_student)
except GroupLimitError as e:
    print(f'Exception caught: {e}')

assert isinstance(gr.find_student('LastName1'), Student), "Test failed: search must return a Student instance"
assert gr.find_student('NonExisting') is None, "Test failed: search for non-existent student must return None"

# проверяю удаление
gr.delete_student('LastName3')
print("\nAfter deleting LastName3:")
print(gr)

gr.delete_student('LastName3')