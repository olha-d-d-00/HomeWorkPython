# my_module/__init__.py

# Импортируем функции из подмодулей, чтобы они были доступны при импорте пакета
from .calculations import add, subtract
from .messages import welcome_message, farewell_message

# Можно также создать переменную или функцию на уровне пакета
__all__ = ["add", "subtract", "welcome_message", "farewell_message"]
