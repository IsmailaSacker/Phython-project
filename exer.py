

# user_name = input("Please ente ur name: ")
# user_age = int(input("Please enter yr of birth: "))

# age = 2023 - user_age


# print("Your name is ", user_name, "and your age is:", age)

# try:
#     user_integer = int(user_age)
#     print("Your name is ", user_name, "and your age is:", age)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


# user_name = input("Please enter your name: ")

# try:
#     yr_of_birth = int(input("Please enter your year of birth: "))
# except ValueError:
#     print("Invalid input. Please enter a valid year of birth.")
# else:
#     current_year = 2023
#     age = current_year - yr_of_birth
#     print("Your name is", user_name, "and your age is:", age)
#     print("enjoy ur day")


# user_fname = input("Please enter firstname: ")
# user_lname = input("Please enter lastname: ")

# fullname = user_fname + " " + user_lname

# full = fullname.upper()

# print("your fullname is:", full, " And the length of your fulname is ", len(full))


# Assignments
# user_name = input("Please enter your Full Name: ")

# full = user_name.lower()

# space = user_name.replace(" ", "")

# print("\n")

# if 'a' in user_name:
#     print("Your full name is:", space,
#           " And you have letter A in your name. Congratulations!")

# else:
#     print("Your full name is:", space,
#           " And you don't have letter A in your name, Bad name")


# list = []

# numb1 = 1
# while numb1 < 5:
#     numb1 = numb1 + 1
#     user_name = input("Please enter your favorate carstuareg: ")
#     list.append(user_name)
# list.sort()
# print(list)
# list = [1, 4, 7, 8, 9, 4, 2]

# print(list[2])

while True:

    num1 = float(input("Please enter any number: "))
    num2 = float(input("Please enter the second number "))

    operator = input("enter any operator from +, -, *, / ")

    addition = num1 + num2
    substraction = num1 - num2
    division = num1 / num2
    multiplication = num1 * num2

    if num1 == 'done':
        break  # Exit the loop if the user inputs 'done'

    if operator == "+":

        print(num1, '+', num2, '=', addition)

    elif operator == '-':

        print(num1, '-', num2, '=', substraction)

    elif operator == '/':

        print(num1, '/', num2, '=', division)

    elif operator == '*':

        print(num1, '*', num2, '=', multiplication)

    else:
        print("you enter an invalid operator")


# while True:
#     num1 = input("Please enter any number (or 'done' to exit): ")

#     if num1 == 'done':
#         break

#     num2 = input("Please enter the second number: ")

#     num1 = float(num1)
#     num2 = float(num2)

#     operator = input("Enter any operator from +, -, *, /: ")

#     if operator == "+":
#         result = num1 + num2
#         print(num1, '+', num2, '=', result)
#     elif operator == '-':
#         result = num1 - num2
#         print(num1, '-', num2, '=', result)
#     elif operator == '/':
#         if num2 != 0:
#             result = num1 / num2
#             print(num1, '/', num2, '=', result)
#         else:
#             print("Division by zero is not allowed.")
#     elif operator == '*':
#         result = num1 * num2
#         print(num1, '*', num2, '=', result)
#     else:
#         print("You entered an invalid operator.")
