print("Enter Student Information")
name = (input("Student Name  : "))
id =   (input("Student Id    : "))
section = (input("Section    : "))
semester = (input("Semester  : "))
print("\nEnter Course Information")
number = int(input("Enter Number Of Course : "))
total_gpa=0
total_credit = 0
course1 = []
grade1 = []

credit1 = []
grade_point1 = []


for i in range(number):
    course=(input("Enter name Of Course   Code: "))
    credit= (int(input("Enter a course credit :")))
    marks = (float(input("Enter Marks         : ")))
    if 80<= marks <= 100 :
        grade = "A+"
        grade_point = 4.00

    elif 75<= marks < 80 :
        grade = "A"
        grade_point = 3.75

    elif 70<= marks < 75 :
        grade = "A-"
        grade_point = 3.50

    elif 65<= marks < 70 :
        grade = "B+"
        grade_point = 3.25

    elif 60<= marks< 65 :
        grade = "B"
        grade_point = 3.00

    elif 55<= marks< 60 :
        grade = "B-"
        grade_point = 2.75

    elif 50<= marks < 55 :
        grade = "C+"
        grade_point = 2.50

    elif 45<= marks < 50 :
        grade = "C"
        grade_point = 2.25

    elif 40<= marks  < 45 :
        grade = "D"
        grade_point = 2.00

    else :
        grade = "F"
        grade_point = 0.00


    total_gpa = total_gpa+grade_point*credit
    total_credit = total_credit+credit
    course1.append(course)
    credit1.append(credit)
    grade1.append(grade)
    grade_point1.append(grade_point)

sgpa = total_gpa/total_credit

print("\n\n")
print("Student Name  : ",name)
print("Student Id    : ",id)
print("Section       : ",section)
print("Semester      : ",semester)
print("\n")
print("Course Code         Course Credit          Grades             Grades Point")
for i in range(number) :
    print(course1[i],"                   ",credit1[i],"                 ",grade1[i],"                ",grade_point1[i])
print("\n")
print("Total Credit :",total_credit )
print("SGPA         :"+"{:.2f}".format(sgpa))




