# Title: Check if the user is an adult.
# Problem Statement:
# Write a Python program that asks the user to enter their age. The program should then check if the user is an adult.
# A person is considered an adult if their age is 18 years or older.

# age = int(input("Enter Your Age : "))
# if age > 18 :
#     print(f"age is 18 years or older : {age}")
# else:print(f"you are not adult ")

# Prompt the user to enter:
# First number
# Second number
# An operator (+, -, *, or /)
# Handle division by zero and display an appropriate error message.
# Print the final result in a clean and user-friendly format.
# Display an error if the user enters an invalid operator.

first_num = int(input("Enter Number First : "))
second_num = int(input("Enter Number Second : "))

operation = input("Enter Operation : ")

match(operation):
    case "+" :
        sum  = first_num + second_num
        print(f"Addition of Tow Number : {sum}")
    case "-" :
        sub = first_num - second_num
        print(f"Subtracation Of Tow Number : {sub} ")
    case "*" :
        mul = first_num * second_num
        print(f"Multiplication Of Tow Number : {mul} ")
    case "/" :
        if first_num == 0 or second_num == 0:
            print(f"Value Is : 0 So division Are Not Possible ")
        else:
            div = first_num / second_num
            print(f"division Of Tow Number : {div} ")
    case _:
        print(f"Enter valid Operation ")





