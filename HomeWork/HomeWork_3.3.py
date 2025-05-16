'''Приклад 1'''
list = [1, 2, 3, 4, 5, 6]
li_1 = list[:3]
li_2 = list[3:]
new_list = [li_1, li_2]
print(new_list)

'''Приклад 2'''
list_x = li_1[0:2]
list_y = li_1[-1:] # тут допоміг ChatGPT після -1 дописати ":", оскільки виводилось число, а не список
list_alpha = [list_x, list_y]
print(list_alpha)

'''Приклад 3'''
list1 = [1, 2, 3, 4, 5]
lili_1 = list1[0:3]
lili_2 = list1[3:]
lili_both = [lili_1, lili_2]
print(lili_both)

'''Приклад 4'''
list_zero = [1]
first_list = list_zero[0:]
second_list = list_zero[:0]
line_hello = [first_list, second_list]
print(line_hello)


'''Приклад 5'''
moy_spisok = []
spisok_1 = moy_spisok
spisok_2 = moy_spisok
noviy_spisok = [spisok_1, spisok_2]
print(noviy_spisok)


