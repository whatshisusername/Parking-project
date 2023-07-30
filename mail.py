"""def c( ):
    global pas
    global pasa
    global pasb
    global pasc
    global pasd
    global cpas, cpasa, cpasb, cpasc, cpasd
    global pna, pnb, pnc, pnd
    global pno
    pas = ps.get()

    cpas = cps.get()
    print(pas, cpas)
    pno = parkno.get()
    print(pno)
    pasa, pasb, pasc, pasd = 0, 0, 0, 0
    cpasa, cpasb, cpasc, cpasd = 0, 0, 0, 0

    if pas == cpas:

        if pno == "1":
            messagebox.showinfo("SUCESS ", "your car is parked safely")

        pna = "1"
        pasa = pas

        cpasa = cpas
        print(pasa, cpasa)
        Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
               activeforeground="white").grid(row=2, column=0)
        Button(r, text="Leave1", command=b, width=6).grid(row=3, column=0)
        elif pno == "2":
        messagebox.showinfo("SUCESS ", "your car is parked safely")

        pnb = "2"
        pasb = pas
        cpasb = cpas
        Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
               activeforeground="white").grid(row=2, column=1)
        Button(r, text="Leave2", command=b, width=6).grid(row=3, column=1)
        elif pno == "3":
        messagebox.showinfo("SUCESS ", "your car is parked safely")

        pnc = "3"
        pasc = pas
        cpasc = cpas
        Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
               activeforeground="white").grid(row=2, column=2)
        Button(r, text="Leave3", command=b, width=6).grid(row=3, column=2)
        elif pno == "4":
        messagebox.showinfo("SUCESS ", "your car is parked safely")

        pnd = "4"
        pasd = pas
        cpasd = cpas
        Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
               activeforeground="white").grid(row=2, column=3)
        Button(r, text="Leave4", command=b, width=6).grid(row=3, column=3)
        else:
        messagebox.showinfo("ERROR ", "INCORRECT PARKING SLOT OR NO ENTRIES(")

    else:
    messagebox.showinfo("ERROR", "INCORRECT PASSWORD OR NO ENTRIES")

def b( ):
    global ps1
    global cps1
    global password1
    global cpassword1
    global parkno1
    global no1
    no1 = StringVar()

    rw = Toplevel(r)
    rw.geometry("300x300")
    rw.configure(bg="skyblue")
    rw.title("LOGIN")
    ps1 = StringVar()
    cps1 = StringVar()
    Label(rw, text="password").grid(row=0, column=0)
    password1 = Entry(rw, textvariable=ps1, show="*")
    password1.grid(row=0, column=1)
    Label(rw, text="confrim  password").grid(row=1, column=0)
    cpassword1 = Entry(rw, textvariable=cps1, show="*")
    cpassword1.grid(row=1, column=1)
    Label(rw, text=" parking slot no").grid(row=2, column=0)
    parkno1 = Entry(rw, textvariable=no1)
    parkno1.grid(row=2, column=1)

    Button(rw, text="submit", command=d).grid(row=3, column=0)


def d( ):
    pas1 = ps1.get()
    cpas1 = cps1.get()
    print(pas1, cpas1)
    pno1 = parkno1.get()
    print(pno1)

    if pas1 == pas and cpas1 == cpas:
        if pas1 == pasa and cpas1 == cpasa and pno1 == "1" and pno1 == pna:
            messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

    Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
           activeforeground="red").grid(row=2, column=0)
    Button(r, text="Park1", command=a, width=6).grid(row=3, column=0)
    elif pas1 == pasb and cpas1 == cpasb and pno1 == "2" and pno1 == pnb:
    messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

    Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
           activeforeground="red").grid(row=2, column=1)
    Button(r, text="Park2", command=a, width=6).grid(row=3, column=1)
    elif pas1 == pasc and cpas1 == cpasc and pno1 == "3" and pno1 == pnc:
    messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

    Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
           activeforeground="red").grid(row=2, column=2)
    Button(r, text="Park3", command=a, width=6).grid(row=3, column=2)
    elif pas1 == pasd and cpas1 == cpasd and pno1 == "4" and pno1 == pnd:
    messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

    Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
           activeforeground="red").grid(row=2, column=3)
    Button(r, text="Park4", command=a, width=6).grid(row=3, column=3)
    else:
    messagebox.showinfo("ERROR", "INCORRECT PASSWORD")


def a( ):
    global ps
    global cps
    global password
    global cpassword
    global parkno
    global no
    no = StringVar()
    global name
    namev = StringVar()
    global vech
    vechv = StringVar()

    rw = Toplevel(r)
    rw.geometry("300x300")
    rw.configure(bg="black")
    rw.title("Login Page")
    ps = StringVar()
    cps = StringVar()
    Label(rw, text="Name", bg="black", fg="white", pady=5, padx=3).grid(row=0, column=0)
    name = Entry(rw, textvariable=namev)
    name.grid(row=0, column=1)
    Label(rw, text="Vehicle no.", bg="black", fg="white", pady=5, padx=3).grid(row=2, column=0)
    vech = Entry(rw, textvariable=vechv)
    vech.grid(row=2, column=1)

    Label(rw, text="Password", bg="black", fg="white", pady=5, padx=3).grid(row=4, column=0)
    password = Entry(rw, textvariable=ps, show="*")
    password.grid(row=4, column=1)
    Label(rw, text="Confirm Password", bg="black", fg="white", pady=5, padx=3).grid(row=6, column=0)
    cpassword = Entry(rw, textvariable=cps, show="*")
    cpassword.grid(row=6, column=1)
    Label(rw, text="Parking Slot No", bg="black", fg="white", pady=5, padx=3).grid(row=8, column=0)
    parkno = Entry(rw, textvariable=no)
    parkno.grid(row=8, column=1)
    Button(rw, text="Submit", command=c, padx=15).grid(row=10, column=0)


def i( ):
    messagebox.showinfo("INFO",'Welcome to Parking System,Click on park to park your car,Click on leave to take your CarHappy to help you')"""





from tkinter import *
from tkinter import messagebox


r=Tk( )
r.configure(bg="grey")
Button(r,text="C",border=0,fg="green",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=2,column=0)
Button(r,text="Park1",width=6).grid(row=3,column=0,pady=(0,20),padx=10)

Button(r,text="C",border=0,fg="green",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=2,column=1)
Button(r,text="Park2",width=6).grid(row=3,column=1,pady=(0,20),padx=10)

Button(r,text="C",border=0,fg="green",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=2,column=2)
Button(r,text="Park3",width=6).grid(row=3,column=2,pady=(0,20),padx=10)

Button(r,text="C",border=0,fg="green",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=2,column=3)
Button(r,text="Park4",width=6).grid(row=3,column=3,pady=(0,20),padx=10)

Button(r,text="C",border=0,fg="green",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=4,column=0)
Button(r,text="Park5",width=6).grid(row=5,column=0)

Button(r,text="C",border=0,fg="green",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=4,column=1)
Button(r,text="Park6",width=6).grid(row=5,column=1)

Button(r,text="C",border=0,fg="green",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=4,column=2)
Button(r,text="Park7",width=6).grid(row=5,column=2)

Button(r,text="C",border=0,fg="green",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=4,column=3)
Button(r,text="Park8",width=6).grid(row=5,column=3)

Label(r,text="WELCOME TO PARKING.LTD",fg="white",bg="black").grid(row=0,column=5)

Button(r,text="INFO",fg="white",bg="blue").grid(row=6,column=0)
r.mainloop( )