student  = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}
print(student)

# Add a new student "David" with marks 88.
print("--- Add a new student ---  ")
student.update({"david" : 88})
print(student)
# Update "Bob"'s marks to 82.
print("--- Update ---  ")

student.update({"david" : 88})
print(student)
# Delete "Alice" from the dictionary.
print("--- delete student ---  ")
student.pop("Alice")
print(student)

# Print all student names (keys).
print("--- Print all student names ---  ")
print(student.keys())
# Print all marks (values).
print("--- values  ---  ")
print(student.values())
# Print all student–mark pairs (items).
print("--- items ---  ")
print(student.items())
# Check if "Charlie" is in the dictionary.
print("--- Check if 'Charlie' is in the dictionary. ---")
if student.fromkeys("Charlie"):
    print("charlie is in ")
else:print(" not in ")
# Get the marks of "Eve" using .get() method with default value 0.
print("---- get() ---- ")
x = student.get("Eve" , 0)
print( x )

# Count the number of students in the dictionary.
print("--- Count the number of students in the dictionary. ---  ")
c = student.values()
print(len(c))
# Clear the dictionary and print it.