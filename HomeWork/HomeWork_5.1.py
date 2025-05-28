import string
import keyword



what_to_check = ["_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value",
                 "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]

for variable in what_to_check:
    is_valid = True

    if variable == "":
        is_valid = False

    if variable in keyword.kwlist:
        is_valid = False

    if "__" in variable:
        is_valid = False

    if variable[0].isdigit():
        is_valid = False

    if " " in variable:
        is_valid = False

    for symbol in string.punctuation:
        if symbol !="_" and symbol in variable:
            is_valid = False
            break

    for word in variable:
        if word.isalpha() and not word.islower():
            is_valid = False
            break

    print(f"{variable} => {is_valid}")


