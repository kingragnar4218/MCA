# Create a Python program that takes multiple inputs from the user, performs operations, and handles different types of exceptions.
# Requirements:
# Ask the user to input:
# An integer a
# An integer b
# A list of integers separated by spaces

# Perform the following operations:
# Divide a by b
# Find the b-th element in the list
# Convert all list elements to integers

# Use try-except to handle:
# ValueError → non-integer input or conversion errors
# ZeroDivisionError → division by zero
# IndexError → accessing an index not in the list
# TypeError → invalid operations
# Print clear error messages for each exception.
# Use finally to print "Program execution finished."


# Ask the user to input:
# An integer a
# An integer b
# A list of integers separated by spaces


try:

    a = int(input("Enter Values A :"))
    b = int(input("Enter Values B :"))
    try:

        try:
            c = a / b
            print(f"divide {c}")

        except TypeError:
            print("TypeError → invalid operations")


    except ZeroDivisionError:
        print("division by zero is not possible ")

except ValueError:
    print("non-integer input or conversion errors")
finally:
    print("Program execution finished")



input_list = input("Enter list values :")
print(input_list)

x = input_list.split(' ')

print(f"New list : {x}")
print("\n")
try:
    print(f"index values : {x[b]}")
except IndexError:
    print("IndexError: list index out of range")
