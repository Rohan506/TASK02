from tkinter import *
import os
import sqlite3


#login
def loggedin():

    global screen2
    global name
    global branch
    global regdid
    global name_entry
    global branch_entry
    global regdid_entry

    screen2 = Toplevel(screen)
    screen2.title("Student Database")
    screen2.geometry("300x250")
    name = StringVar()
    branch = StringVar()
    regdid = StringVar()

#Student Info
    Label(screen2, text = "Name :").pack()
    name_entry = Entry(screen2,textvariable = name)
    name_entry.pack()
    Label(screen2, text = "Branch :").pack()
    branch_entry = Entry(screen2,textvariable = branch)
    branch_entry.pack()
    Label(screen2, text = "Regd Id :").pack()
    regdid_entry = Entry(screen2,textvariable = regdid)
    regdid_entry.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "SUBMIT",fg = "black",bg ="light blue", command = do).pack()


#Subjects
def open_window():
    global tip
    tip = Toplevel(screen2)
    tip.title("SUBJECTS")
    tip.geometry("300x250")

    Label(tip, text = "Select a subject to insert marks: ").pack()

    Button(tip, text = "FCT",width = 10, command = open_window_fct).pack()

    Button(tip, text = "DSD", width =10, command = open_window_dsd).pack()

    Button(tip, text = "EVS", width = 10, command = open_window_evs).pack()

    Label(tip, text = "").pack()

    Button(tip, text = "SUBMIT",fg = "black",bg = "green",width =10, command = open_window3).pack()

#FCT
def open_window_fct():
    global fct
    global fct_marks
    global fct_entry
    fct_marks = IntVar()

    fct = Toplevel(tip)
    fct.title("FCT")
    fct.geometry("300x250")
    Label(fct, text = "Enter the marks: ").pack()

    fct_entry = Entry(fct,textvariable = fct_marks)
    fct_entry.pack()

    Button(fct, text = "Done", command = fct_submission).pack()

def fct_submission():
    Label(fct, text = "Submitted.", fg = "green").pack()
    fct1 = fct_marks.get()
    name1 = name.get()

    conn = sqlite3.connect("StudentData.db")
    with conn:
        cur = conn.cursor()
    cur.execute( '''UPDATE DETAILS SET FCT == "%s" WHERE Name == "%s"''' %(fct1,name1))
    conn.commit()
    cur.close()
    conn.close()

#DSD
def open_window_dsd():
    global dsd_marks
    global dsd_entry
    global dsd
    dsd_marks = IntVar()

    dsd = Toplevel(tip)
    dsd.title("DSD")
    dsd.geometry("300x250")
    Label(dsd, text = "Enter the marks obtained :").pack()

    dsd_entry = Entry(dsd,textvariable = dsd_marks)
    dsd_entry.pack()

    Button(dsd, text = "Done", command = dsd_submission).pack()

def dsd_submission():
    Label(dsd, text = "Submitted.", fg = "green").pack()
    dsd1 = dsd_marks.get()
    name1 = name.get()

    conn = sqlite3.connect("StudentData.db")
    with conn:
        cur = conn.cursor()
    cur.execute( '''UPDATE DETAILS SET DSD == "%s" WHERE Name == "%s"''' %(dsd1,name1))
    conn.commit()
    cur.close()
    conn.close()

#EVS
def open_window_evs():
    global evs_marks
    global evs_entry
    global evs
    evs_marks = IntVar()

    evs = Toplevel(tip)
    evs.title("EVS")
    evs.geometry("300x250")
    Label(evs, text = "Enter the marks obtained :").pack()

    evs_entry = Entry(evs,textvariable = evs_marks)
    evs_entry.pack()
    Button(evs, text = "Done", command = evs_submission).pack()

def evs_submission():
    Label(evs, text = "Submitted.", fg = "green").pack()
    evs1 = evs_marks.get()
    name1 = name.get()

    conn = sqlite3.connect("StudentData.db")
    with conn:
        cur = conn.cursor()
    cur.execute( '''UPDATE DETAILS SET EVS == "%s" WHERE Name == "%s"''' %(evs1,name1))
    conn.commit()
    cur.close()
    conn.close()




def do():
    open_window()
    put()
#ERROR
def invalid():
    screen3 = Toplevel(screen)
    screen3.title("")
    screen3.geometry("150x50")
    Label(screen3, text = "Invalid UserID or Password.", fg = "red").pack()

#GUI3
def open_window3():
    global tom
    tom = Toplevel(tip)
    tom.title("GUI 3")
    tom.geometry("300x250")

    Label(tom, text = "").pack()

    Button(tom, text = "CGPA",width = 10, command = cgpa).pack()

    Button(tom, text = "GRADE", width =10, command = grade).pack()

    Label(tom, text = "").pack()

    Button(tom, text = "New Input", width = 10,fg = "blue",bg="light blue", command = NewInput).pack()

    Button(tom, text = "Close", width = 10,fg = "black",bg="red", command = close).pack()

#CGPA calcultaion
def cgpa():
    global gpa
    scrcgpa = Toplevel(tom)
    scrcgpa.title("CGPA")
    scrcgpa.geometry("150x50")
    fctm = fct_marks.get()
    dsdm = dsd_marks.get()
    evsm = evs_marks.get()
    Label(scrcgpa, text = "CGPA obtained :").pack()
    gpa = (fctm + dsdm + evsm)/30.0
    Label(scrcgpa,text = float(gpa)).pack()

#Grade
def grade():
    scrgrade = Toplevel(tom)
    scrgrade.title("Grade")
    scrgrade.geometry("150x50")
    Label(scrgrade, text = "Grade Obtained: ").pack()
    if (gpa < 5.0):
        g = "D"
    elif(gpa < 6.0):
        g = "C"
    elif(gpa < 7.0):
        g = "B"
    elif(gpa < 8.0):
        g = "A"
    elif(gpa < 9.0):
        g = "E"
    elif(gpa < 10.1):
        g = "O"
    Label(scrgrade, text = str(g)).pack()

#OPEN NEW WINDOW
def NewInput():
    screen2.destroy()
    loggedin()
#Close
def close():
    screen.destroy()


conn = sqlite3.connect('StudentData.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS DETAILS(Name TEXT, Branch TEXT, RegdID INT, FCT REAL, DSD REAL, EVS REAL)")
conn.commit()

def put():
    name1 = name.get()
    branch1 = branch.get()
    regdid1 = regdid.get()
    conn = sqlite3.connect('StudentData.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO DETAILS (Name,Branch, RegdID) VALUES (?,?,? )",(name1,branch1,regdid1))
    conn.commit()

#Verification
def login_verify():
    user1 = userid.get()
    password1 = password.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    list_of_files = os.listdir()


    if user1 in list_of_files:

        file1 = open(user1, "r")
        verify = file1.read().splitlines()

        if password1 in verify:

            loggedin()

        else:
            invalid()
    else:
        invalid()


def signin():
    global screen
    global userid
    global password
    global username_entry
    global password_entry
    screen = Tk()
    screen.geometry("400x300")
    screen.title("Student Management system")
    Label(screen, text = "Username :").pack()
    userid = StringVar()
    username_entry = Entry(textvariable = userid)
    username_entry.pack()
    Label(screen, text = "Password :").pack()
    password = StringVar()
    password_entry = Entry(textvariable = password, show = "*")
    password_entry.pack()
    Button(screen, text = "Submit",fg="black",bg="light blue", command = login_verify).pack()
    screen.mainloop()


signin()
cur.close()
conn.close()
