# main.py

# Импортируем пакет
import my_module

# Используем функции из пакета
print(my_module.welcome_message())

a = 10
b = 5

print("Addition:", my_module.add(a, b))
print("Subtraction:", my_module.subtract(a, b))

print(my_module.farewell_message())


# __init__.py импортирует функции из файлов calculations.py и messages.py,
# делая их доступными при импорте пакета my_module в main.py.

# В main.py импортируется весь пакет my_module,
# после чего мы можем обращаться к функциям add, subtract, welcome_message и farewell_message напрямую.

# запустить: python main.py
