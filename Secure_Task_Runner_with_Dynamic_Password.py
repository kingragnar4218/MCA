#  Prompt: Secure Task Runner with Dynamic Password Attempts
#
# 📝 Problem Statement:
# Create a command-line Python program that simulates a secure system where the user can define how many attempts are allowed to enter a password. If the correct password is entered within the defined attempts, the user gains access to a secure task menu that includes various interactive utility options.
#
# 🎯 Objectives:
# Let the user define how many login attempts are allowed.
#
# Accept password input and validate it against a predefined password.
#
# If the password is correct within the allowed attempts, show a task menu.
#
# If the maximum number of attempts is reached, deny access and end the program
#
# 🧩 Features to Implement:
# 1. Dynamic Login System:
# Ask the user: "How many attempts would you like to allow?"
#
# Let the user try logging in that many times.
#
# Predefined correct password (e.g., "Teqstars Technologies").
#
# Show remaining attempts if login fails.
#
# If attempts exceed, show: 🚫 Access Denied!
#
# 2. Task Menu (on Successful Login):
# Use a dict to display a numbered menu. Example:
#
# 1. Show Today's Special
# 2. GST Calculator (5%)
# 3. Even or Odd Checker
# 4. Multiplication Table Generator
# 5. Exit
# 3. Task Logic:
# ✅ Show Today’s Special: Use a to display 3-4 fixed dishes.
#
# ✅ GST Calculator: Accept a price, calculate 5% GST, and show total.
#
# ✅ Even/Odd Checker: Ask for a number and check even or odd.
#
# ✅ Multiplication Table: Ask for a number and print table up to 10.
#
# ✅ Exit: Ends the task menu using break.

#
# def after_login():
#     while(True):
#         print(
#             f" \n 1. Show Today's Special \n 2. GST Calculator (5%) \n 3. Even or Odd Checker \n 4. Multiplication Table Generator \n 5. Exit")
#         select = input("Select Task :")
#         match(select):
#             case "1":
#
#                 list = {"dishe 1" : 500 , "dishe 2": 200 , "dishe 3" : 100 , "dishe 4" : 300}
#                 # print(f"{key}: {value}")
#                 for key, value in list.items():
#                     print(f"{key}: {value}")
#
#             case "2":
#
#                 amount = int(input("Enter Amount : "))
#                 GST = 5
#                 total_gst = amount * GST / 100
#                 print(f"Total GST is {total_gst}")
#
#             case "3":
#
#                 num = int(input("Enter Number : "))
#                 if num % 2 == 0:
#                     print(f"Number is Even :{num}")
#                 else:print(f"Number is Odd :{num}")
#
#             case "4":
#                 num = int(input("Enter Number for Multiplication : "))
#                 for i in range(1 , 11):
#                     mul = num*i
#                     print(f"{num} * {i} = {mul}")
#             case "5" :
#                 print("Exit")
#                 break


def after_login():
    while(True):
        print(
            f" \n 1. Show Today's Special \n 2. GST Calculator (5%) \n 3. Even or Odd Checker \n 4. Multiplication Table Generator \n 5. Exit")
        select = input("Select Task :")

        if select == "1":

            specials_list = {"dishe 1" : 500 , "dishe 2": 200 , "dishe 3" : 100 , "dishe 4" : 300}
            for key, value in specials_list.items():
                print(f"{key}: {value}")

        elif select == "2":

                amount = int(input("Enter Amount : "))
                GST = 5
                total_gst = amount * GST / 100
                print(f"Total GST is {total_gst}")

        elif select == "3":
                num = int(input("Enter Number : "))
                if num % 2 == 0:
                    print(f"Number is Even :{num}")
                else:
                    print(f"Number is Odd :{num}")

        elif select == "4":

                num = int(input("Enter Number for Multiplication : "))
                for i in range(1 , 11):
                    mul = num*i
                    print(f"{num} * {i} = {mul}")

        elif select == "5":
            print("Exit")
            break

        else:
            print("Invalid selection.")


#after_login()
login_attempts = int(input("How many attempts would you like to allow ? : "))
def pass_check():
    global login_attempts
    correct_password = "Teqstars Technologies"
    i = 0
    while i< login_attempts:
        password = input("Enter Password : ")
        if password == correct_password :
            print(" You Are Login")
            after_login()
            break
        else:
            login_attempts -= 1
            print("Invalid Password ")
            print(f"Remaining Attempts {login_attempts}. ")
            if login_attempts == 0:
                print("🚫 Access Denied!")
                break
            print(f"Try Again")

pass_check()
