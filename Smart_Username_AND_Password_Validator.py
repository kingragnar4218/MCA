#starting time = 1:40 endding time = 03:30
#1 hour and 50 minutes.

# here i create 3 variable and get input from the user and store it after i use split() , isalnum() and  count() method that i store i another variable and
# use if condition and OR operator and in Email where i use lover() and get substring and that store in reversed and both compare using backword index and that display output
# in password i use count() and IF ELSE condition and compare both and display and also check this '@' or '!' and display lenth of password

full_name = input("enter name : ")

email = input("enter email : ")

password = input("enter password : ")

print("----- Smart Lo-gin Validator -------")

#password.strip() → Clean up any spaces
password.strip()
#Check if password is only letters and numbers
check_pass = password.isalnum()
#  password.count('@'), password.count('!')
check_ath = password.count("@")
check_not = password.count("!")


#Add Logical + Comparison Operators:
pass_check = 0
if check_ath >= 1 or check_not >= 1:
    pass_check = True
else: pass_check = False


#Convert full name to Proper case
print(f"Name : {full_name.upper()}")
#email.lower()
print(f"E-mail : {email.lower()}")

vali_email = "@gmail.com"

# main_vali_email = email[:-11:-1]
# main_vali_email_leth = len(main_vali_email)
# if vali_email and (main_vali_email[::-1] and main_vali_email_leth == 10):
#     print("Gmail Account? : True")
# else:print("Gmail Account? : False")
print(f"Gmail Account? : {email.endswith('@gmail.com')}")


print("\n")
print(f"Password Length : {len(password)}")


print(f"Contains '@' or '!' {pass_check}")

print(f"Only Alphanumeric? : {check_pass}")

if len(password) > 8 and pass_check:
    print(f"Strong Password?  : True ")
else:print(f"Strong Password?  : False")