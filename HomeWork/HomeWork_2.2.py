user_number = input("Введите 5-ти значное число: ")[::-1]
print(user_number)


'''Как еще можно было сделать'''

number = int(input("Введите 5-ти значное число: "))
digit1 = number % 10 #
digit2 = (number // 10) % 10
digit3 = (number // 100) % 10
digit4 = (number // 1000) % 10
digit5 = (number // 10000) % 10

# Формуємо нове число у зворотньому порядку

reversed_number = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5

print("Зворотнє число: ", reversed_number )

