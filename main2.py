from tkinter import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import datetime
import csv

root = Tk()
root.geometry('600x700')
root.title("Registration Form")
root.configure(background='grey')


#defining function msg() using messagebox
def msg():
    course = cvar.get()
    select = var.get()
    if(select == 1 or select == 2):
        # get the index of the last character in the widget,if it is zero,it is empty
        if (e1.index("end") == 0):
            mb.showwarning('Missing details', 'enter your name')
        elif(e2.index("end") == 0):
            mb.showwarning('Missing details', 'enter your email id')
        elif(e3.index("end") == 0):
            mb.showwarning('Missing details', 'enter your contact number')
        elif(e4.index("end") == 0):
            mb.showwarning('Missing details', 'enter your Password')
        elif(e5.index("end") == 0):
            mb.showwarning('Missing details', 'Confirm your Password')
        elif(e4.get()!=e5.get()):
            mb.showwarning('Missing details', 'Recheck your Password')    
        else:
            mb.showinfo('Success', 'Registration done successfully')
    else:
            mb.showinfo('Missing details', 'enter your gender')

#exporting entered data
def save():
    g = var.get()
    course = cvar.get()
    db = dob.get_date()
    d = db.strftime('%d/%m/%Y')
    now = datetime.datetime.now()
    if(g==1):
        gender ='male'
    else:
        gender ='female'

    
    #save data in csv file
    with open('Users.csv', 'a') as fs:
        w = csv.writer(fs)
        w.writerow([ e1.get(),e4.get(),e2.get(),e3.get(),d,gender,course,now.strftime("%d-%m-%Y %H:%M")])
        fs.close()

def saveinfo():
    save()
    msg()

def page2():
     def Login():
         e1 = Entry1.get()
         e2 = Entry2.get()

         if e1 == "" or e2 == "":
             tkinter.mb.showinfo('Error', 'Enter all the values in!')
         else:
             x = 0
             with open('Users.csv', 'r') as csv_file:
                 csv_reader = csv.reader(csv_file)
                 for row in csv_reader:
                     if x == 0:
                         for field in row:
                             if field == e1 and row[1] == e2 and x==0:
                                 tkinter.mb.showinfo('Login', 'Logged in Successfully')
                                 x = 1
                                 break
                             else:
                                 tkinter.mb.showinfo('Login', 'Login failed, please recheck your password')
                                 x = 1
                                 break
     top = Tk()
     top.geometry("300x300")
     Button1 = Button(text="Submit", command=Login)
     Button1.place(x=130, y=200)
     text1 = Label(top, text="Username:")
     text1.place(x=50, y= 80)
     text2 = Label(top, text="Password:")
     text2.place(x=50, y= 140)
     Entry1 = Entry(top)
     Entry1.place(x=125, y=82)
     Entry2 = Entry(top)
     Entry2.place(x=125, y=142)
     top.mainloop()
    

# creating labels and entry widgets


l1 = Label(root, text="BITS Registration form",width=25,font=("times",20,"bold"),bg='blue',fg='white')
l1.place(x=70,y=50)
l2 = Label(root, text="Full Name",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l2.place(x=70,y=130)
e1 = Entry(root,width=30,bd=2)
e1.place(x=240,y=130)
l3 = Label(root, text="Email",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l3.place(x=70,y=180)
e2 = Entry(root,width=30,bd=2)
e2.place(x=240,y=180)
l4 = Label(root, text="DOB",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l4.place(x=70,y=230)

# dateEntry -Date selection entry with drop-down calendar
dob = DateEntry(root, width=27, background='brown', foreground='white',date_pattern='dd/mm/Y', borderwidth=3)
dob.place(x=240,y=230)

l5 = Label(root, text="Gender", width=20, font=("times",12,"bold"),anchor="w",bg='grey')
l5.place(x=70,y=280)

# radiobuttons
var = IntVar()
r1 = Radiobutton(root, text="Male", variable=var, value=1, font=("times",12),bg='grey')
r1.place(x=235,y=280)
r2 = Radiobutton(root, text="Female", variable=var, value=2, font=("times",12),bg='grey')
r2.place(x=315,y=280)

l6 = Label(root, text="Contact no.",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l6.place(x=70,y=320)
e3 = Entry(root,width=30,bd=2)
e3.place(x=240,y=320)
l7 = Label(root, text="Select campus",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l7.place(x=70,y=370)

# create a dropdown menu with the OptionMenu widget
cvar = StringVar()
cvar.set("Select campus")
option = ("pilani", "goa", "hyderabad","dubai")
o = OptionMenu(root,cvar, *option)
o.config(font=("times",11),bd=3)
o.place(x=240,y=365,width=190)

l8 = Label(root, text="Create Password",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l8.place(x=70,y=425)
e4 = Entry(root,width=30,bd=2)
e4.place(x=240,y=425)

l9 = Label(root, text="Confirm Password",width=20,font=("times",12,"bold"),anchor="w",bg='grey')
l9.place(x=70,y=475)
e5 = Entry(root,width=30,bd=2)
e5.place(x=240,y=475)
# submit and cancel buttons
b1 = Button(root, text='Submit',command=saveinfo,width=15,bg='green',fg='white',font=("times",12,"bold"))
b1.place(x=120,y= 550)
b2 = Button(root, text='Cancel',command=root.destroy,width=15,bg='maroon',fg='white',font=("times",12,"bold"))
b2.place(x=320,y=550)
b3 = Button(root, text='Already registered,sign in',command=page2,width=37,bg='blue',fg='white',font=("times",12,"bold"))
b3.place(x=120,y=600)


root.mainloop()




