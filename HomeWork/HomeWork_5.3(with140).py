import string

ONE_SYMBOL = "#"

user_string = input("Enter your expression: ") # пользователь вводит набор символов, слов и тд.

cleaned_text = ''.join(symbol for symbol in user_string if symbol not in string.punctuation) # чистка введенной фразы от символов

lst = cleaned_text.title() # поднимает для каждой фразы заглавную букву

new_lst = lst.split() #  превращаю фразы в строку с отделенными фразами

joined_words = ''.join(new_lst) # склеиваю фразы

final_result = joined_words[:140]

print(ONE_SYMBOL + final_result)  # вывод конкатенации