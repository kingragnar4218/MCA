from datetime import datetime, date, timedelta , time


today = datetime.now()
print(f"\ntoday date :{today} , {today.date()}") # {type(today)} <class 'datetime.date'>

print("\nTask: Add 7 days to the current date and print the resulting date. ")

extra_day = int(input("Enter Day you want to add extra : "))

add_day = today + timedelta(days=extra_day)
print(f"add 7 day :{add_day}")

print("\nTask: Calculate the number of days between today and a future date (e.g., New Year's Day next year).")

find_date = (add_day - today).days
print(f"Remaining day:{find_date} ")

print("\nTask(user input): Create two date objects for different dates. Write a script to determine which date is earlier or if they are the same.")


def validate_date(date_string, date_format):
    return datetime.strptime(date_string, date_format)


check_date = input("Enter date format = YYYY-MM-DD:")
format = "%Y-%m-%d" #2026-1-1

change_check_date = datetime.strptime(check_date , format)
try:
    validate_date(check_date, format)
except ValueError:
    print("invalid Date Enterrrrrr ")

if today.date() < change_check_date.date():
    print("The first date is earlier.")
elif today.date() > change_check_date.date():
    print("The second date is earlier.")
else:
    print("Both dates are the same.")

# Hint:date objects can be compared using standard comparison operators (<, >, ==).
print("\nTask(user input): Ask the user for their birthdate (year, month, day). Calculate and print their current age in years.")
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

age = today.year - year - ((today.month, today.day) < (month, day))
print("Your age is:", age)

print("\nTask: Create a time object representing 3:30 PM. Print the hour and minute separately.")

t = time(15, 30)
print("Hour:", t.hour)
print("Minute:", t.minute)








