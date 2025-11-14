#starting = 3:40 ending = 4:40  1 hour.
# here i create l1 name list and it add all item in the list after i apply all methdos append() , extend() , insert() , remove() , pop(), index(),  count(), sort(),copy()
# and after i create one more empty list and where append item in using for loop

l1 = ["Pay bills", "Read book", "Write report", "Pay bills", "Call mom"]
# Append the task "Exercise".
print(f"---- list ---- \n {l1}")
l1.append("Exercise")
print(f"---- New add item  ---- \n {l1}")
# Extend the list with:
new_l = ["Grocery shopping", "Clean room"]
l1.extend(new_l)
print(f" ------ Extend ------ \n {l1} ")

# Insert "Attend meeting" at index 3.
print(f" ------ INSERT  ------  ")
l1.insert( 3,"Attend meeting" )
print(l1)
# Remove the first "Pay bills" from the list.
print(f" ------ remove  ------ ")
l1.remove("Pay bills")
print(l1)
# Pop the last task from the list and print it.
print(f" ------ pop  ------ ")
l1.pop()
print(f"{l1}")
# Find and print the index of "Read book".
print(f" ------ index  ------ ")
a = l1.index("Read book")
print(f"index of : Read book : {a}")
# Count and print how many times "Pay bills" still appears.
print(f" ------ count   ------ ")
c = l1.count("Read book")
print(f"Pay bills appears : {c}")
# Sort the list alphabetically.
print(f" ------ sort ------ ")
l1.sort()
print(f" sort : {l1}")
# Reverse the order of the sorted list.
print(f" ------ sort Reverse ------ ")
l1.sort(reverse=True)
print(f" sort Reverse : {l1}")

# Copy the final task list to a new list called backup_tasks.
backup_tasks = l1.copy()
print(f" backup list  : {backup_tasks}")
# Clear the original tasks list.
print(f" ------ crear ------ ")
l1.clear()
print(f"crear : {l1}")

# create new list new_task = ['task_completed','python']

new_task = ['task_completed','python']
# add a  empty list(new_to_do_list) and append all the new_task list element using loop.
print(f" ------ append list in new_to_do_list ------ ")
new_to_do_list = []
for i in new_task:
    new_to_do_list.append(i)
print(f"new_to_do_list {new_to_do_list}")

# merge new_task and new_to_do_list
print("---- merge list ----")
new_task.extend(new_to_do_list)
print(new_task)