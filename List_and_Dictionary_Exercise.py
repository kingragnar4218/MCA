# Python program to find the sum of all items in a dictionary.
d = {'a': 100, 'b': 200, 'c': 300}
item_list = d.values()
item_sum = sum(item_list)
print(f"Sum of item : {item_sum} ")

#Merging or Concatenating two Dictionaries in Python
print("---- Concatenating two Dictionaries in Python ----+")
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}
d1.update(d2)
print(d1)


#Convert List of Lists to Dictionary - Python
print("--- List of Lists to Dictionary ---")
a = [["a", 1], ["b", 2], ["c", 3]]
d3 = {key : value for key , value in a }
print(d3)


#Find the Length of a List without using len()
print("---- Length of a List without using len()---- ")
a = [1, 2, 3, 4, 5]
count = 0
for i in a :
    count += 1
print(count)



#Check if element exists in list in Python
print("---- element exists in list ---- ")
a = [10, 20,30, 40, 50]
find = list(filter(lambda x : x == 30 , a  ))
print(find)
print(f"{'Element exists in the list' if find[0] == 30 else 'Element not in the list'}")


#Find Sum and Average of List in Python

print("---- Sum and Average of List ---- ")
a = [10, 20, 30, 40, 50]
a_sum = sum(a)
print(f"Sum of item : {a_sum} ")
a_avg = a_sum / len(a)
print(f"Average of the list: {a_avg}")

#Multiply All Numbers in the List
print("---- Multiply All Numbers in the List ----")
a = [2, 4, 8, 3]
mul = 1
for i in a :
    mul *= i
print(mul)


#Print even numbers in a list - Python
print("---- even numbers in a list ----")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x : x % 2 == 0 , a))
print(even)

#Python program to find second largest number in a list
a = [10, 20, 4, 45, 99]
print("---- find second largest --- ")
a.sort()
print(a[-2])



#Python program to count positive and negative numbers in a list
a = [10, -20, 30, -40, 50, -60, 0]
Positive = 0
Negative = 0
for i in a :
    if i > 0 :
        Positive += 1
    else:
        if i == 0 :
            continue
        Negative += 1
print(f"Positive {Positive}")
print(f"Negative {Negative}")


# Program to create grade calculator in PythonProgram to create grade calculator in Python
# 1. Take Number of students as user input
# 2. Take comma seperated marks for every students
# 3. Print Every student's average score and grade
#
# 1. score >= 90 : "A"
# 2. score >= 80 : "B"
# 3. score >= 70 : "C"
# 4. score >= 60 : "D"
# 5. score < 60 :"F"
# Output
# Your percentage is 78%
# Your Grade is B1 based on the entered 5 Subjects.Your Grade is B based on 5 Subjects.
print("----- grade calculator -----")

def calculate_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"

def mark_student():
    number_of_students = int(input("Enter The Number Of Students: "))
    main_marks = []

    for i in range(number_of_students):
        marks = input(f"Enter marks for Student {i + 1} ").split(',')

        marks = [int(mark) for mark in marks]

        main_marks.append(marks)

    for i in range(len(main_marks)):

        student_marks = main_marks[i]
        average_score = sum(student_marks) / len(student_marks)
        grade = calculate_grade(average_score)

        print(f"Student {i + 1} ==> Average Score: {average_score}")
        print(f"Grade: {grade} Based on {len(student_marks)} subjects.")
#mark_student()


# 1.Remove empty tuples from a list
# Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
# Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]
# Input : tuples = [(”,”,’8′), (), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”), (), (”,”),()]
# Output : [(”, ”, ‘8’), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”, ”)]

print("----- Remove empty tuples from a list -----")
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]
print(f"Befor : {tuples}")
res = list(filter(None, tuples))
print(f"After {res}")

tuples1 = [(",",'8'), (), ('0', '00', '000'), ('birbal', ", '45'), ("), (), (","),()]
print(f"Befor : {tuples1}")
res1 = list(filter(None, tuples1))
print(f"After {res1}")

# 2.Find all duplicate characters in string

print("------ Find all duplicate characters in string ------ ")

string = input("Enter String : ")


def find_dup(s):
    char_counts = {}
    duplicates = []
    for i in s:
        if i in char_counts:
            char_counts[i] += 1
        else:
            char_counts[i] = 1

    for i,count in char_counts.items():
        if count > 1:
            duplicates.append(i)

    return duplicates

output = find_dup(string)
print(f"Output: {output}")


my_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
new_list = [[key , value] for key , value in my_dict.items()]
print(new_list )


print("------------------------------------")



# Function to display a question
def display_question(question):
    print(question['question_text'])
    for idx, option in enumerate(question['options']):
        print(f"{chr(65 + idx)}. {option}")  # A, B, C, D...


# Function to get and validate user's answer
def get_user_answer(question):
    valid_answers = ['A', 'B', 'C', 'D']
    while True:
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer in valid_answers:
            return question['options'][valid_answers.index(answer)]
        else:
            print("Invalid input. Please choose A, B, C, or D.")


# Function to check if the user's answer is correct and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


# Main function to run the quiz
def run_quiz():
    score = 0
    total_questions = len(questions)

    for question in questions:
        display_question(question)
        user_answer = get_user_answer(question)
        if check_answer(user_answer, question['correct_answer']):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {question['correct_answer']}\n")

    # Display final results
    print(f"You got {score} out of {total_questions} questions correct.")
    percentage = (score / total_questions) * 100
    print(f"Your score: {percentage:.2f}%")


# Run the quiz
if __name__ == "__main__":
    run_quiz()
