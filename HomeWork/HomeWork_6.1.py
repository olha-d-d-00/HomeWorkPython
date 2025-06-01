import string

POSITIVE_ANSWER = "Yes"
POSITIVE_ANSWER1 = "Y"
NEGATIVE_ANSWER = "No"
NEGATIVE_ANSWER1 = "N"

while True:
    user_range = input("Enter the range of ASCII letters you need in the format \"a-Z\": ").strip()
    if len(user_range) != 3:
        print("Error input length! Please enter only 3 value, like: \"a-Z\"")
    else:
        firs_char = user_range[0]
        dash = user_range[1]
        last_char = user_range[2]

        letters_ascii = string.ascii_letters

        if not firs_char.isalpha():
            print("Invalid value! Please enter first value in letter format only!")
        elif dash != "-":
            print("Invalid value! Your second character must be a dash (-)")
        elif not last_char.isalpha():
            print("Invalid value! Please enter the last value in letter format only!")
        elif firs_char not in letters_ascii or last_char not in letters_ascii:
            print("Invalid value! Only Latin letters (A-Z, a-z) are allowed!")
        else:
            start_value = letters_ascii.index(firs_char)
            end_value = letters_ascii.index(last_char)

            if start_value <= end_value:
                result = letters_ascii[start_value:end_value + 1]
            else:
                result = letters_ascii[end_value:start_value + 1]


            print(result)

    question_for_user = input("Continue outputting ASCII letters? Enter Yes/No, or y/n: ").strip().lower()

    if question_for_user in [NEGATIVE_ANSWER.lower(), NEGATIVE_ANSWER1.lower()]:
        break
