# Define Question Structure:
#
# Decide how you will store each question. For example, a dictionary could hold:
# 'question_text': 'What is the capital of France?'
# 'options': ['Paris', 'London', 'Berlin', 'Rome'] (for multiple choice)
# 'correct_answer': 'Paris'
# Create a list of at least 5-10 such question objects/dictionaries. Initially, you can hardcode this list in your Python script.
#
# Display a Question:
# Write a function that takes a question object/dictionary as input.
# This function should print the question text.
# If it's a multiple-choice question, it should also print the options, numbered or lettered (e.g., A, B, C, D).
#
# Get User's Answer:
# Prompt the user to enter their answer.
# For multiple choice, they might enter the letter or number corresponding to their choice.
# Consider basic input validation (e.g., if options are A-D, ensure they enter one of those).
#
# Check the Answer and Keep Score:
# Write a function that compares the user's answer to the correct answer for the current question.
# Maintain a variable to keep track of the user's score. Increment it for correct answers.
# Provide immediate feedback (e.g., "Correct!" or "Wrong. The correct answer was X.").
#
# Run the Quiz:
# Loop through all the questions in your list.
# For each question, display it, get the user's answer, and check it.
#
# Display Final Results:
# After all questions have been answered, display the user's final score (e.g., "You got 7 out of 10 questions correct.").
# Optionally, display a percentage.
# give in single file of code where code is simple and easy
#
# Define a list of question objects (dictionaries)
questions = [
    {
        'question_text': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct_answer': 'Paris'
    },
    {
        'question_text': 'Which planet is known as the Red Planet?',
        'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'correct_answer': 'Mars'
    },
    {
        'question_text': 'What is the largest ocean on Earth?',
        'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic ocean', 'Pacific Ocean'],
        'correct_answer': 'Pacific ocean'
    },
    {
        'question_text': 'What is the tallest mountain in the world?',
        'options': ['Mount everest', 'K2', 'Kangchenjunga', 'Mount Kilimanjaro'],
        'correct_answer': 'Mount everest'
    },
    {
        'question_text': 'Who wrote the play "Romeo and Juliet"?',
        'options': ['Charles Dickens', 'William shakespeare', 'Mark Twain', 'Jane Austen'],
        'correct_answer': 'William shakespeare'
    },
    {
        'question_text': 'What is the hardest natural substance on Earth?',
        'options': ['Gold', 'Diamond', 'Iron', 'Platinum'],
        'correct_answer': 'Diamond'
    },
    {
        'question_text': 'Which country is the largest by area?',
        'options': ['China', 'Canada', 'United States', 'Russia'],
        'correct_answer': 'Russia'
    },
    {
        'question_text': 'Which gas do plants absorb from the atmosphere for photosynthesis?',
        'options': ['Oxygen', 'Carbon dioxide', 'Nitrogen', 'Hydrogen'],
        'correct_answer': 'Carbon dioxide'
    },
    {
        'question_text': 'What is the longest river in the world?',
        'options': ['Amazon River', 'Nile river', 'Yangtze River', 'Mississippi River'],
        'correct_answer': 'Nile river'
    },
    {
        'question_text': 'What is the smallest country in the world?',
        'options': ['Monaco', 'Vatican city', 'San Marino', 'Liechtenstein'],
        'correct_answer': 'Vatican city'
    }
]

# print(questions[0]['options'][1])

answer_count = 0


def show_question_main():
    global answer_count

    for index, qst in enumerate(questions, start=1):

        print(f"\n{index}.Question: {qst['question_text']}")

        for idx, option in enumerate(qst['options']):
            print(f"{chr(65 + idx)}. {option}")

            # print(f"Options: {' , '.join(qst['options'])}")

        give_answer = input("Enter Answer -->  :").capitalize()
        print(give_answer)

        # ans_option_list = qst['options'] # here inside all option that question
        ans_option = ["A", "B", "C", "D"]

        ans_index = ans_option.index(give_answer)

        # ans_index_list = ans_option_list.index(give_answer)# here A , B , C , D
        # print(ans_index_list)

        user_ans = qst['options'][ans_index]  # user anser string
        user_ans_list = qst['options'][ans_index]

        print(f"string of user answer ---->{user_ans}")

        correct_answer = qst['correct_answer']
        print(f"correct_answer ---> {correct_answer}")

        print("YOUR ANSWER --->", qst['options'][ans_index])

        if correct_answer == user_ans:  # or ans_index_list == user_ans_list
            answer_count += 1
            print("you are correct........")
        else:
            print("you are wrong..!!!!!!")

    print(f"\nYou got {answer_count} out of 10 questions correct.")


# show_question()
def show_question_beta():
    global answer_count

    for index, qst in enumerate(questions, start=1):

        print(f"\n{index}.Question: {qst['question_text']}")

        for idx, option in enumerate(qst['options']):
            print(f"{chr(65 + idx)}. {option}")

        # print(f"Options: {' , '.join(qst['options'])}")
        try:
            give_answer = input("Enter Answer -->  :").capitalize()
            print(give_answer)

            correct_answer = qst['correct_answer']
            print(f"correct_answer ---> {correct_answer}")
            if len(give_answer) == 1:
                print("Truuu if :----->")
                ans_option = ["A", "B", "C", "D"]
                ans_index = ans_option.index(give_answer)

                user_ans = qst['options'][ans_index]  # user anser string
                print(f"string of user answer ---->{user_ans}")
                print("YOUR ANSWER --->", qst['options'][ans_index])

                if correct_answer == user_ans:  # or ans_index_list == user_ans_list
                    answer_count += 1
                    print("you are correct........")
                else:
                    print("you are wrong..!!!!!!")
            else:
                print(f"\n flaseeeee if ------> : ")
                ans_option_list = qst['options']  # here inside all option that question
                print(ans_option_list)
                ans_index_list = ans_option_list.index(give_answer)  # here this variable store option list index
                print(ans_index_list)

                user_ans_list = qst['options'][ans_index_list]
                print(f"string of user answer ---->{user_ans_list}")
                print("YOUR ANSWER --->", qst['options'][ans_index_list])

                if correct_answer == user_ans_list:  # or ans_index_list == user_ans_list
                    answer_count += 1
                    print("you are correct........")
                else:
                    print("you are wrong..!!!!!!")
        except ValueError:
            print("you are wrong..!!!!!!")#Invalid Input please Enter [A-B-C-D] OR full answer!!!!!!

        # for idx, option in enumerate(qst['options']):
        #     print(f"{chr(65 + idx)}. {option}")

    print(f"\nYou got {answer_count} out of 10 questions correct.")


#show_question_beta()


def show_question_beta_1():
    global answer_count

    for index, qst in enumerate(questions, start=1):

        print(f"\n{index}. Question: {qst['question_text']}")

        # Display options for the question
        for idx, option in enumerate(qst['options']):
            print(f"{chr(65 + idx)}. {option}")

        try:
            give_answer = input("Enter Answer -->  :").strip().upper()  # Convert to uppercase for uniform comparison
            print(f"Your input: {give_answer}")

            correct_answer = qst['correct_answer'].upper()  # Convert correct answer to uppercase as well
            print(f"correct_answer ---> {correct_answer}")

            # Check if the user entered a letter answer (A, B, C, or D)
            if give_answer in ['A', 'B', 'C', 'D']:  # Letter-based answer
                ans_option = ["A", "B", "C", "D"]
                ans_index = ans_option.index(give_answer)

                user_ans = qst['options'][ans_index]  # Get the option text
                print(f"string of user answer ---->{user_ans}")
                print("YOUR ANSWER --->", user_ans)

                if correct_answer == user_ans.upper():  # Convert user's answer to uppercase for comparison
                    answer_count += 1
                    print("You are correct........")
                else:
                    print("You are wrong..!!!!!!")

            else:  # Full answer input
                # Normalize the input to uppercase for comparison
                normalized_input = give_answer.capitalize()

                if normalized_input in qst['options']:  # Check if the input is a valid option
                    user_ans = normalized_input
                    print(f"string of user answer ---->{user_ans}")
                    print("YOUR ANSWER --->", user_ans)

                    if correct_answer == user_ans.upper():  # Compare with the uppercase version of the correct answer
                        answer_count += 1
                        print("You are correct........")
                    else:
                        print("You are wrong..!!!!!!")
                else:
                    print(f"Invalid full answer input: '{give_answer}'! Please enter a valid option.")

        except ValueError:
            print("You are wrong..!!!!!!")  # Invalid Input please enter [A-B-C-D] or full answer!!!!!!

    print(f"\nYou got {answer_count} out of 10 questions correct.")



show_question_beta_1()
