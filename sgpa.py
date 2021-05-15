import tkinter as tk
from tkinter import ttk
from tkinter import*
root = tk.Tk()

root.title("SGPA")
root.geometry("1000x800")

course_name = ttk.Label(root,text = "Enter Course Name :")
course_name.grid(row = 0 ,column = 0)
course_name.config(font = ("Courier",12))

course_credit = ttk.Label(root,text = "Enter Course Credit :")
course_credit.grid(row = 1 ,column = 0)
course_credit.config(font = ("Courier",12))



course_name_var = tk.StringVar()
course_name_entry = ttk.Entry(root, width = 20 ,textvariable =course_name_var )
course_name_entry.grid(row = 0 ,column = 2)

course_credit_var = tk.IntVar()
course_credit_entry = ttk.Entry(root, width = 20 ,textvariable =course_credit_var )
course_credit_entry.grid(row = 1 ,column = 2)

courses = []
credites = []
def add():
    course = course_name_var.get()
    credit = course_credit_var.get()
    courses.append(course)
    credites.append(credit)

    course_name_var.set("")
    course_credit_var.set("")
    for i in range (len(courses)) :

        text1 = f"class :{courses[i]}   score : {credites[i]}"
        Label(root,text =text1).grid(row = 4+i)



Button(root ,text = "ADD",command = add).grid(row = 2 ,column = 3)


root.mainloop()




