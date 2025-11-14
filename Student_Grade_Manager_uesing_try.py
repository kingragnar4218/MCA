# Objective:
# Build a program that reads student grades from a file, calculates the average, and handles multiple possible errors.
# Instructions:
# Ask the user to enter a filename (e.g., grades.txt).
# The file will contain one grade per line (e.g., 85, 90, 78).
# Use a try block to:
# Open the file.
# Read all the lines.
# Convert them into integers.
# Calculate the average grade.
# Handle errors with except blocks:
# FileNotFoundError → if the file does not exist.
# PermissionError → if the file exists but cannot be accessed.
# ValueError → if the file contains something that is not a valid number.
# Use an else block to:
# Print the average grade if everything succeeds.
# Use a finally block to:
# Print "Grade processing completed." no matter what.
try:

    file_name = input("Enter file name You want to open :")
    f = open(file_name)
    # print(f.read())
    stud = 0

    for index, mark_str in enumerate(f, start=1):
        l1 = mark_str.split(",")
        marks = [int(mark) for mark in l1]
        avg = sum(marks) / len(marks)
        stud += 1
        # print(avg)
        print(f"Average grade For student {index} : {round(avg, 2)}")
except FileNotFoundError:
    print("Error: File not found!")
except ValueError:
    print("Error: Invalid grade value found in file!")
except PermissionError:
    print("Error: You don’t have permission to read this file.")

finally:print("Grade processing completed.")





