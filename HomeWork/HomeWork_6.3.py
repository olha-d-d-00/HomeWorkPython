user_number = input("Enter your number: ")
_number = [int(i) for i in user_number]

if len(_number) == 1:
    print(_number[0])
else:
    while len(_number) > 1:
        result = 1
        for d in _number:
            result *= d
        if result <= 9:
            break

        _number = [int(i) for i in str(result)]

    print(result)
