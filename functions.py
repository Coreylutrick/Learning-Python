import sys
# def hello_world():
#     print("Hellow World")

# hello_world()
user_choice = input("Please enter a number\n")
user_choice2 = input("Please enter a second number\n")
new_user_choice = int(user_choice)
new_user_choice2 = int(user_choice2)

def check_if_int(num1, num2):
    if(type(num1) is not int or type(num2) is not int):
        print("Please pick a number")
        return
    else:
        print("The total of the numbers is ")
        return num1 + num2


def sum(num1, num2):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = check_if_int(new_user_choice, new_user_choice2)
# print("The total of the numbers is")
print(total)

# def multiple_items(*args):
#     print(args)
#     print(type(args))

# multiple_items("Corey", "Logan", "Silas")

# def multi_named_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# multi_named_items(first = "Corey", last = "Silas")