def common_elements():
    multiples_of_3 = {num for num in range(100) if num % 3 == 0}
    multiples_of_5 = {num for num in range(100) if num % 5 == 0}

    common = multiples_of_3 & multiples_of_5
    return common

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')