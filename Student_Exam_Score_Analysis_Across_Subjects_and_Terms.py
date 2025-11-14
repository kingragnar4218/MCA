# You need to:
#
# For each student, for each subject, calculate the average score across all 3 terms.
#
# Find for each student the subject with the highest average score.
#
# Output a dictionary where each student ID maps to:
#
# {
#   'name': student_name,
#   'best_subject': subject_name_with_highest_avg,
#   'average_score': highest_avg_score
# }
# Example Input:
# You have three dictionaries:
#
# students → Student IDs → Names
#
# subjects → Subject IDs → Subject names
#
# term_scores → Term numbers (1, 2, 3) → dict mapping Student IDs → dict mapping Subject IDs → Score
#
# students = {
#     1: "Alice",
#     2: "Bob",
#     3: "Charlie"
# }
#
# subjects = {
#     101: "Math",
#     102: "Science",
#     103: "History"
# }
#
# term_scores = {
#     1: {  # Term 1
#         1: {101: 80, 102: 75, 103: 90},
#         2: {101: 60, 102: 65, 103: 70},
#         3: {101: 85, 102: 80, 103: 88}
#     },
#     2: {  # Term 2
#         1: {101: 82, 102: 78, 103: 85},
#         2: {101: 65, 102: 68, 103: 72},
#         3: {101: 88, 102: 83, 103: 90}
#     },
#     3: {  # Term 3
#         1: {101: 85, 102: 80, 103: 87},
#         2: {101: 70, 102: 70, 103: 75},
#         3: {101: 90, 102: 85, 103: 92}
#     }
# }
# Expected Output:
# {
#     1: {'name': 'Alice', 'best_subject': 'Math', 'average_score': 82.33},
#     2: {'name': 'Bob', 'best_subject': 'History', 'average_score': 72.33},
#     3: {'name': 'Charlie', 'best_subject': 'Math', 'average_score': 87.67}
# }

students = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

subjects = {
    101: "Math",
    102: "Science",
    103: "History"
}

term_scores = {
    1: {  # Term 1
        1: {101: 80, 102: 75, 103: 90},
        2: {101: 60, 102: 65, 103: 70},
        3: {101: 85, 102: 80, 103: 88}
    },
    2: {  # Term 2
        1: {101: 82, 102: 78, 103: 85},
        2: {101: 65, 102: 68, 103: 72},
        3: {101: 88, 102: 83, 103: 90}
    },
    3: {  # Term 3
        1: {101: 85, 102: 80, 103: 87},
        2: {101: 70, 102: 70, 103: 75},
        3: {101: 90, 102: 85, 103: 92}
    }
}


def student_scores(students, subjects, term_scores):
    student_summary = {}
    for student_id, student_name in students.items():

        subject_averages = {}
        for subject_id, subject_name in subjects.items():

            mark = []
            for term_num in term_scores:
                # print(f"name:{students[i], subjects[i + 100], term_scores[i][i][i + 100]}")
                score = term_scores[term_num][student_id][subject_id]
                mark.append(score)

            total_mark = sum(mark)
            print(total_mark)
            average = total_mark / len(term_scores)
            subject_averages[subject_name] = average

        # find max number
        best_subject_name = max(subject_averages, key=subject_averages.get)
        highest_avg_score = round(subject_averages[best_subject_name], 2)

        student_summary.update({
            student_id: {
                'name': student_name,
                'best_subject': best_subject_name,
                'average_score': highest_avg_score
            }
        })

    return student_summary


output_summary = student_scores(students, subjects, term_scores)
print(output_summary)
