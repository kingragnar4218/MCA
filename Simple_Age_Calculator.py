#this variable is use for get user name
name  = input("Enter your name :")

#this variable is use for get job tital
Job_title = input("Enter Job :")

#this vriable is use to get country name
country = input("Enter country :")

#this variable is use to get birth year
birth_year = int(input("enter birth year :"))

#this variable is use to get current year
current_year = int(input("enter current year :"))

#this variable count age
age = float(current_year - birth_year)

#this variable is use to get monthly incom
monthly_income = float(input("Enter Monthly Income : "))


#this is static variable to use defoult retirement age
retirement_age = 60

print("\n ======= Smart Retirement Profile ======= \n")
print(f"Name : {name}")
print(f"job Title : {Job_title}")
print(f"Country : {country} \n")

print(f"Birth Year : {birth_year}")
print(f"Current Year : {current_year}")
print(f"Age : {age}")

#this calculate year left to retirement
year_left_to_retirement  = retirement_age - age
print(f"Retirement Age : {retirement_age}")
print(f"Years Left to Retire {year_left_to_retirement}")

#this condition  give info about retirement is eligible or not
if retirement_age <= year_left_to_retirement :
    eligible_for_retirement = True
    print(f"Eligible for Retirement : {eligible_for_retirement} \n")
else:
    eligible_for_retirement = False
    print(f"Eligible for Retirement : {eligible_for_retirement} \n ")

# this varible is find annual income
annual_income = monthly_income * 12

#here print both monthly income or annual income
print(f"Monthly Income : {monthly_income} \n Annual Income : {annual_income}")

#this condition is give info about user are tex payer or not
if annual_income > 250000 :
    is_tax_payer = True
    print(f"Is Tax Payer ? : {is_tax_payer}")
else:
    is_tax_payer = False
    print(f"Is Tax Payer ? : {is_tax_payer}")
