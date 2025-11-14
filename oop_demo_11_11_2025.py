from abc import ABC, abstractmethod

class Shape(ABC):

    def area(self):
        pass

class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Using polymorphism
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")


class Example:
    def show(self, a):
        print(a)

    def show(self, a, b):  # this replaces the previous one
        print(a, b)


obj = Example()
# obj.show(5)
obj.show(5, 10)



from datetime import date, timedelta, time

# --- Task 1: Add 7 days to the current date ---
today = date.today()
future_date = today + timedelta(days=7)
print("Today's date:", today)
print("Date after 7 days:", future_date)

# --- Task 2: Days between today and New Year's Day next year ---
new_year = date(today.year + 1, 1, 1)
days_until_new_year = (new_year - today).days
print("Days until New Year:", days_until_new_year)

# --- Task 3: Compare two date objects (user input) ---
print("\nEnter two dates to compare:")
year1 = int(input("Enter year for first date: "))
month1 = int(input("Enter month for first date: "))
day1 = int(input("Enter day for first date: "))
date1 = date(year1, month1, day1)

year2 = int(input("Enter year for second date: "))
month2 = int(input("Enter month for second date: "))
day2 = int(input("Enter day for second date: "))
date2 = date(year2, month2, day2)

if date1 < date2:
    print("The first date is earlier.")
elif date1 > date2:
    print("The second date is earlier.")
else:
    print("Both dates are the same.")

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

# Calculate age
today = date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print("Your age is:", age)


t = time(15, 30)

# Print hour and minute
print("Hour:", t.hour)
print("Minute:", t.minute)