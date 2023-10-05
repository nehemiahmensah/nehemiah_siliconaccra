# def add_two(num):
#     result = num + 2
#     return

# user_input = ("Enter your number ")
# answer = add_two(user_input)
# print(f"Your answer is {answer}")

info = input("Enter your age ")
# # print(info)
# # print(type(info))
# # print(info.isnumeric())

# while info.isnumeric() != True and info == float():
#     print("ERROR!!! \nPlease enter a valid input")
#     info = input("Enter your age ")
# else: level = input("What is your name? ")
# while level.isalpha() != True:
#     print("ERROR!!! \n Enter a name without a number")
#     level = input("What is your name? ")
# else: print(f"Your age is {info} \n Your name is {level}")
if "." in info:
    info = info.isnumeric
    while info.isnumeric() != True :
        print("ERROR!!! \nPlease enter a valid input")
        info = input("Enter your age ")
    else: level = input("What is your name? ")
    while level.isalpha() != True:
        print("ERROR!!! \n Enter a name without a number")
        level = input("What is your name? ")
    else: print(f"Your age is {info} \n Your name is {level}")




