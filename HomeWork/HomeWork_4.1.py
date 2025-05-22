original_list = [5, 0, 9, 7, 0, 3, 0, 2]
new_list = [i for i in original_list if i != 0]
zero_list = [i for i in original_list if i == 0]
sum_list = new_list + zero_list
print(sum_list)