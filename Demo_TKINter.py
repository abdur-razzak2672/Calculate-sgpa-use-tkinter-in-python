import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk()
root.title("Razzak")
root.geometry("1000x700")
root.configure(background = "cadet blue")


#calculation
def process_result() :
    windows = Tk()
    windows.title("Student Result")
    windows.geometry("650x500")
    windows.configure(background="cadet blue")




    for i in range(len(courses)):
        s_name = f"Student Name  : {student_name4[i]}\nStudent Id: {student_id4[i]}\nSection : {section4[i]}\nSemester : {semester4[i]}\n\n"
        text7 = Label(windows, bg="cadet blue", width=72, text=s_name)
        text7.config(font=("Arial", 12))
        text7.grid(row=0, column=0)

        sgpa = sum(total_gpas)/ sum(credit1)
        sgpa1 ="{:.2f}".format(sgpa)
        text = f"SGPA : {sgpa1}                       Total Credits Taken : {sum(credit1)}"
        text5 = Button(windows, bg="light cyan", text=text)
        text5.place(x=150, y=380)
        text5.config(font=("Arial", 12))

    text1 = f"Course Code          Course Credit            Grades            Grades Point\n"
    text2 = Label(windows,bg = "light blue",width = 72, text=text1)
    text2.grid(row=10)
    text2.config(font=("Arial", 11))
    for i in range(len(courses)):
        text3 = f"       {courses[i]}                          {credit1[i]}                            {grade1[i]}                        {grade_point1[i]}      "
        text4 = Label(windows,bg = "Sky blue",width = 72, text=text3)
        text4.config(font=("Arial", 12))
        text4.grid(row = 11+i)
    back =  Button(windows,bg = "sea green",text = "Show again",command = lambda: windows.destroy())
    back.place(x=400,y=430)
    back.config(font=("Arial", 11))


    windows.mainloop()

# Define Add button method


courses = []

markss =[]

total_gpas = []
grade1 = []
credit1 = []


grade_point1 = []

student_name4 =[]
student_id4 =[]
section4 = []
semester4 = []



def add():

    student_name3 = name2.get()
    student_name4.append(student_name3)
    student_id3 = id2.get()
    student_id4.append(student_id3)
    section3 = section2.get()
    section4.append(section3)
    semester3 = semester2.get()
    semester4.append(semester3)

    course3 = course2.get()
    credit3 = credit2.get()
    marks3 =marks2.get()
    credit1.append(credit3)
    courses.append(course3)
    markss.append(marks3)


    course2.set("")
    credit2.set("")
    marks2.set("")
    text5 = f"       Course Code          Marks                Credit            Grades Point\n"
    text6 = Label(root,bg = "light blue",width = 50, text=text5)
    text6.grid(row=0)
    text6.config(font=("Arial", 11))
    for i in range (len(courses)) :

        if 80 <= float(marks3) <= 100:
            grade = "A+"
            grade_point = 4.00

        elif 75 <= float(marks3) < 80:
            grade = "A"
            grade_point = 3.75

        elif 70 <= float(marks3) < 75:
            grade = "A-"
            grade_point = 3.50

        elif 65 <= float(marks3) < 70:
            grade = "B+"
            grade_point = 3.25

        elif 60 <= float(marks3) < 65:
            grade = "B"
            grade_point = 3.00

        elif 55 <= float(marks3) < 60:
            grade = "B-"
            grade_point = 2.75

        elif 50 <= float(marks3) < 55:
            grade = "C+"
            grade_point = 2.50

        elif 45 <= float(marks3) < 50:
            grade = "C"
            grade_point = 2.25

        elif 40 <= float(marks3) < 45:
            grade = "D"
            grade_point = 2.00

        else:
            grade = "F"
            grade_point = 0.00


    grade1.append(grade)
    grade_point1.append(grade_point)
    total_gpa = grade_point * credit3
    total_gpas.append(total_gpa)

    text1 = f"            {courses[i]}                       {markss[i]}                       {credit1[i]}                        {grade1[i]}       "
    text2 = Label(root, bg="Sky blue", width=50, text=text1)
    text2.config(font=("Arial", 12))
    text2.grid(row=5 + i)


Button(root, text="SUBMIT",command =process_result, bg="sea green").place(x= 640 ,y= 420)
exit =  Button(root,bg = "sea green",text = "EXIT",command = lambda: root.destroy())
exit.place(x=550,y=420)
exit.config(font=("Arial", 10))

# hints
name2 = StringVar()

id2 = StringVar()

section2 = StringVar()

semester2 = StringVar()

#result hints
course2 = StringVar()

credit2 = IntVar()

marks2 = IntVar()

number2 = IntVar()

result_button2 = StringVar()
result_button2.set("show result")


#input var for Student Information
student_name = Entry(root,textvariable = name2 , width =30).place(x= 150 ,y= 300)
student_id = Entry(root,textvariable = id2, width =30).place(x= 150 ,y=340)
student_section = Entry(root,textvariable = section2 , width =30).place(x= 150 ,y= 380)
semester = Entry(root,textvariable = semester2 , width =30).place(x= 150 ,y= 420)

#input var for result information
course = tk.Label(root,text = "Enter Course Name  :").place(x= 475 ,y=300)

credit = tk.Label(root,text = "Enter Course Credit  :").place(x= 475 ,y=340)
marks = tk.Label(root,text =  "Enter Marks               :").place(x= 475 ,y=380)


student_name = tk.Label(root,text="Student Name  : ").place(x= 50 ,y=300)
student_id = tk.Label(root,text="Student Id         : ").place(x= 50 ,y= 340)
student_section = tk.Label(root,text="Section              : ").place(x= 50 ,y= 380)
semester = tk.Label(root,text="Semester           : ").place(x= 50 ,y= 420)



#course.place(x=20 ,y=200)
#course.config(font = ("Courier",12))
course = Entry(root,textvariable = course2 , width =30).place(x= 600 ,y=300)

credit = Entry(root,textvariable = credit2 , width =30).place(x= 600 ,y= 340)
marks = Entry(root,textvariable = marks2 , width =30).place(x= 600 ,y= 380)


#button
add_button = Button(root,command = add ,text = "ADD",bg = "sea green").place(x= 750 ,y= 420)

root.mainloop()

