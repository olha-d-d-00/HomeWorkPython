import random
my_list = []

for i in range(random.randint(3, 10)):
    my_list.append(random.randint(1, 10))
print(my_list)

num1 = my_list[0]
num2 = my_list[2]
num3 = my_list[-2]

new_list = [num1, num2, num3]
print(new_list)