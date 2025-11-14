print("1. Ask the user to enter a string. Print how many characters.")
str1 = input("Enter a String :")
print(f"characters is : {len(str1)}")

print(" \n2.Given numbers = [15, 22, 3, 89, 7], print the smallest and largest.")
numbers = [15, 22, 3, 89, 7]
print(f"smallest : {min(numbers)} and largest : {max(numbers)}")

print("\n 3.Take an integer input from the user and print its absolute value. ")
num = int(input("Enter minus values :"))
print(f"absolute number is : {abs(num)} ")

print(f"\n4.calculate 7 raised to the power of 4.")
print(f"power : {pow(7 , 4)}")

print("\n5.Sort the list nums = [12, 5, 18, 3, 25] in ascending order.")
nums = [12, 5, 18, 3, 25]
print(sorted(nums))

print("\n6.Find the sum of [2, 4, 6, 8, 10].")
l1 = [2, 4, 6, 8, 10]
print(f"Sum Of list :{sum(l1)}")

print("\n7.Take a floating number from the user (e.g., 5.6789) and round it to 2 decimal places.")
num = float(input(f"Enter floating number :"))
print(round(num , 2))

print("\n8.Perform type conversions : ")
print("Convert '456' (string) to an integer.")
s1 = '456'
print(f"before convert : {s1} , {type(s1)}")
i1 = int(s1)
print(f"After convert : {i1} , {type(i1)}")


print("\nConvert 250 (integer) to a string.")
i2 = 250
print(f"before convert : {i2} , {type(i2)}")
s2 = str(i2)
print(f"After convert : {s2} , {type(s2)}")


print("\nConvert [4, 5, 6] (list) to a tuple.")
l2 = [4, 5, 6]
print(f"before convert : {l2} , {type(l2)}")
t1 = tuple(l2)
print(f"After convert : {t1} , {type(t1)}")

print("\n9.For the list [True, False, True]")
# Check with any() if at least one is True.
# Check with all() if all are True.
my_list = [True, False, True]

check = any(my_list) # here all at list one TRUE so it return TRUE
print(f"any() result: {check}")

check_all = all(my_list)# here all are TRUE so it return TRUE if any one are FALSE so it return FALSE
print(f"all() result: {check_all}")



print("\n10.print the index and item for the list ['red', 'green', 'blue']")
l3 = ['red', 'green', 'blue']
for index, item in enumerate(l3):
    print(index, item)


print("\n11.display the list [1, 2, 3, 4, 5] in reverse order.")
l4 = [1, 2, 3, 4, 5]
print(sorted(l4 , reverse=True))

print("\n12.Use filter() and a lambda function to keep only even numbers from [10, 15, 20, 25, 30]")
l5 = [10, 15, 20, 25, 30]
even = filter(lambda x : x % 2 == 0 , l5)
even_num = list(even)
print(even_num)

# 13.combine two lists into a dictionary:
keys = ["id", "name", "age"]
values = [1, "John", 30]

dict = dict(zip(keys, values))

print(dict)

