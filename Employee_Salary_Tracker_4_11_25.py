#stating = 4:50 ending = 5:55 2 hours and 5 minutes.
from pickle import FALSE

# in this task i create list of tuple and where i add 4 employee details and all display using index and after i display using f-string
# and find total employee and total salary and Average salary and highest salary and second highest salary using sorted() method

employees = [('emp1' , 5000 , True),('emp2' , 2000 , False),('emp3' , 3000 , True),('emp4' , 4000 , False)]
print("---- All employees ----")
print(f" employees 1 {employees[0]}")
print(f" employees 2 {employees[1]}")
print(f" employees 3 {employees[2]}")
print(f" employees 4 {employees[3]} \n")
print("---- All employees display f-string ----")
print(f" Name :{employees[0][0]} | Salary :{employees[0][1]} | Full-Time: {employees[0][2]}")
print(f" Name :{employees[1][0]} | Salary :{employees[1][1]} | Full-Time: {employees[1][2]}")
print(f" Name :{employees[2][0]} | Salary :{employees[2][1]} | Full-Time: {employees[2][2]}")
print(f" Name :{employees[3][0]} | Salary :{employees[3][1]} | Full-Time: {employees[3][2]} \n")

# Calculate

# Total number of employees
print(f"Total Number of Employee : {len(employees)}")

# Total salary of all employees
total_salary = employees[0][1]+employees[1][1]+employees[2][1]+employees[3][1]
print(f"Total Number of Employee : {total_salary}")

# Average salary
avg = total_salary /4
print(f"Average salary Employee : {avg}")

# Name of the employee with the highest salary
print(f"Highest Salary : {max(employees[0][1] , employees[1][1] , employees[2][1] , employees[3][1])}")

# Find second highest salary with name
print("second highest : ")
aa = [employees[0][1] , employees[1][1] , employees[2][1] , employees[3][1]]
# aa.sort()
s1 = sorted(employees , key=lambda x : x[1])
temp = s1[-2]
print(temp[0] , temp[1])

# Create a static variable called bonus = 2000
bonus = 2000
# Add this bonus to employee 1 and employee 3's salary


employees[0] = (employees[0][0], employees[0][1] + bonus, employees[0][2])
employees[2] = (employees[2][0], employees[2][1] + bonus, employees[2][2])

# Print their updated salary with the bonus
print("----- updated salary -----")
print(f" Name :{employees[0][0]} | Salary :{employees[0][1]} | Full-Time: {employees[0][2]}")
print(f" Name :{employees[1][0]} | Salary :{employees[1][1]} | Full-Time: {employees[1][2]}")
print(f" Name :{employees[2][0]} | Salary :{employees[2][1]} | Full-Time: {employees[2][2]}")
print(f" Name :{employees[3][0]} | Salary :{employees[3][1]} | Full-Time: {employees[3][2]} \n")

# Check if employee 1 earns more than employee 2
if employees[0][1] > employees[1][1]:
    print(f"Employee 1 is earns more than employee 2  :{employees[0][1]}")
else:print(f"Employee 2 is earns more than employee 1 :{employees[1][1]}")


# Amit Shah earns more than Riya Mehta: True
print(f"{employees[0][0]} earns more than {employees[1][0]} : { True if employees[0][1] > employees[1][1] else False   }  ")