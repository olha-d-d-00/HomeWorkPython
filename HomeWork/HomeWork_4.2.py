import random
my_list = []

for i in range(random.randint(0, 10)):
    my_list.append(random.randint(1, 10))
print(my_list)

new_list = my_list[::2]
sum_list = sum(my_list[::2])
new_list = sum_list * my_list[-1]
print(new_list)
print(sum_list)
print(new_list)