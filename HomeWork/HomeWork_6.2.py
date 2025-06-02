MIN_VALUE = 0
MAX_VALUE = 8640000

users_time_str = input("Enter a number greater than or equal to 0 and less than 8640000: ")

if not users_time_str.isdigit():
    print("Invalid value. Enter a number!")
else:
    user_time = int(users_time_str)
    if user_time < MIN_VALUE or user_time > MAX_VALUE:
        print("Number is not in range. Please enter a valid number!")
    else:
        days, seconds = divmod(user_time, 86400) # 86400 - количество секунд в дне
        hours, seconds = divmod(seconds, 3600) # 3600 - количество секунд в часе
        minutes, seconds = divmod(seconds, 60) # 60 - количество секунд в минуте
        if days == 1:
            print(f"{days} day,", f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
        else:
            print(f"{days} days,", f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")