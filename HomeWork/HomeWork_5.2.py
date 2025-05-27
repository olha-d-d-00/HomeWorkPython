POSITIVE_ANSWER = "Yes"
POSITIVE_ANSWER1 = "Y"
NEGATIVE_ANSWER = "No"
NEGATIVE_ANSWER1 = "N"

while True:
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))


    print("There are such mathematical operations:\n\t1. Addition (+)\n\t2. Subtraction (-)\n\t3. Multiplication (*)\n\t4. Division (/)")
    user_select = int(input("Select the required operation: "))

    match user_select:
        case 1:
            print(number_1 + number_2)
        case 2:
            print(number_1 - number_2)
        case 3:
            print(number_1 * number_2)
        case 4:
            if number_2 == 0:
                print("You can't divide by 0!")
            else:
                print(number_1 / number_2)


    question_for_user = input("Continue calculation? Enter Yes/No, or y/n: ").strip().lower()

    if question_for_user in [NEGATIVE_ANSWER.lower(), NEGATIVE_ANSWER1.lower()]:
        break