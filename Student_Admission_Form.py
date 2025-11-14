#this variable are use for get student name
Student_nm = input("Enter Student Name :")

#this variable are use for get student surname
Student_sr_nm = input("Enter Student surname :")

#this variable are use for get student City
Student_city = input("enter City : ")

#this variable are use for get student branch
Student_branch = input("Enter Branch : ")

#this variable are use for get student enrollment number
Student_enrol_no = int(input("Enter Enrollment Number :"))

#this variable are use for get current semester
Student_sem =   int(input("Enter Semester Number :"))

#this variable are use for get main subject of student
Student_main_sub = input("enter main subject  ")

#staic variable use for university name
university = "darshan University "

print("----  display details ------\n")

print(f"Hello Gays my Name is {Student_nm } { Student_sr_nm} And I'm from {Student_city} \n I am Current pursuing my {Student_branch} Semester {Student_sem} in {university} \n my main subject is {Student_main_sub} and my Enrolment Number is {Student_enrol_no}")
# print(f"I am Current pursuing my {Student_branch} Semester {Student_sem} in {university}")
# print(f"my main subject is {Student_main_sub} and my Enrolment Number is {Student_enrol_no}")

print("\n")
print("--- variable datatype ----")
print(f" Student Name : {Student_nm} --> {type(Student_nm)} " )
print(f" Student Surname :{Student_sr_nm} --> {type(Student_sr_nm)} " )
print(f" Student City :{Student_city} --> {type(Student_city)} " )
print(f" Student Branch :{Student_branch} --> {type(Student_branch)} " )
print(f" Student Enrollment Number :{Student_enrol_no} --> {type(Student_enrol_no)} " )
print(f" Student Semester :{Student_sem} --> {type(Student_sem)} " )
print(f" Student Main Subject :{Student_main_sub} --> {type(Student_main_sub)} " )
print(f" university :{university }--> {type(university)} " )

