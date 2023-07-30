import random
from datetime import datetime

class parking:
  def __init__(self,parkticket,park,parkname,parkvechno):
      self.parkticket = parkticket
      self.park = park
      self.parkname = parkname
      self.parkvechno = parkvechno





global slot1,slot2,slot3
slot1=parking(0,1,0,0)
slot2=parking(0,2,0,0)
slot3=parking(0,3,0,0)
slot4=parking(0,4,0,0)
slot5=parking(0,5,0,0)
slot6=parking(0,6,0,0)
slot7=parking(0,7,0,0)
slot8=parking(0,8,0,0)







def park(i):

    global parkno
    parkno = StringVar()


    global name
    name  = StringVar()
    global vechno
    vechno = StringVar()
    global ticketno
    ticketno = StringVar()
    global checkticketno
    checkticketno = StringVar()


    rw = Toplevel()
    rw.geometry("400x400")
    rw.configure(bg="black")
    rw.title("LOGIN")

    Label(rw, text="Name").grid(row=0, column=0)
    name = Entry(rw, textvariable=name)
    name.grid(row=0, column=1)
    Label(rw, text="Vehicle no.").grid(row=1, column=0)
    vech = Entry(rw, textvariable=vechno)
    vech.grid(row=1, column=1)
    Label(rw, text="slotno").grid(row=2, column=0)



    Entry(rw, textvariable=parkno,state=DISABLED).grid(row=2, column=1)
    parkno.set(i)
    Button(rw, text="GET TICKET",command=ticket).grid(row=3, column=1)
    Label(rw, text="ticket no.").grid(row=4, column=0)
    Entry(rw, textvariable=ticketno,show="*").grid(row=4, column=1)
    Button(rw, text="submit",command=parkcheck).grid(row=5, column=1)








def parkcheck():
    if str(b)==ticketno.get():
        if parkno.get() == "1":
            print("in")
            global slot1
            slot1=parking(ticketno.get(),1,name.get(),vechno.get())
            print(slot1.parkticket)
            print(slot1.park)

            messagebox.showinfo("SUCESS ", "your car is parked safely")
            Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
               activeforeground="white").grid(row=2, column=0)
            Button(r, text="leave",width=6,command=lambda:leave(1)).grid(row=3, column=0,pady=(0,20),padx=10)
            addtofile()
        elif parkno.get() == "2":
            print("in")
            global slot2
            slot2=parking(ticketno.get(), 2,name.get(),vechno.get())
            print(slot2.parkticket)
            print(slot2.park)

            messagebox.showinfo("SUCESS ", "your car is parked safely")
            Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
               activeforeground="white").grid(row=2, column=1)
            Button(r, text="leave",width=6,command=lambda:leave(2)).grid(row=3, column=1,pady=(0,20),padx=10)
            addtofile()
        elif parkno.get() == "3":
            print("in")
            global slot3
            slot3=parking(ticketno.get(), 3,name.get(),vechno.get())
            print(slot3.parkticket)
            print(slot3.park)

            messagebox.showinfo("SUCESS ", "your car is parked safely")
            Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
               activeforeground="white").grid(row=2, column=2)
            Button(r, text="leave",width=6,command=lambda:leave(3)).grid(row=3, column=2,pady=(0,20),padx=10)
            addtofile()
        elif parkno.get() == "4":
            print("in")
            global slot4
            slot4=parking(ticketno.get(), 4,name.get(),vechno.get())
            print(slot4.parkticket)
            print(slot4.park)

            messagebox.showinfo("SUCESS ", "your car is parked safely")
            Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
               activeforeground="white").grid(row=2, column=3)
            Button(r, text="leave",width=6,command=lambda:leave(4)).grid(row=3, column=3,pady=(0,20),padx=10)
            addtofile()
        elif parkno.get() == "5":
            print("in")
            global slot5
            slot5 = parking(ticketno.get(), 5,name.get(),vechno.get())
            print(slot5.parkticket)
            print(slot5.park)

            messagebox.showinfo("SUCESS ", "your car is parked safely")
            Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
                   activeforeground="white").grid(row=4, column=0)
            Button(r, text="leave", width=6, command=lambda:leave(5)).grid(row=5, column=0)
            addtofile()
        elif parkno.get() == "6":
            print("in")
            global slot6
            slot6 = parking(ticketno.get(), 6,name.get(),vechno.get())
            print(slot6.parkticket)
            print(slot6.park)

            messagebox.showinfo("SUCESS ", "your car is parked safely")
            Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
                   activeforeground="white").grid(row=4, column=1)
            Button(r, text="leave", width=6, command=lambda:leave(6)).grid(row=5, column=1)
            addtofile()

        elif parkno.get() == "7":
            print("in")
            global slot7
            slot7 = parking(ticketno.get(), 7,name.get(),vechno.get())
            print(slot7.parkticket)
            print(slot7.park)

            messagebox.showinfo("SUCESS ", "your car is parked safely")
            Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
                   activeforeground="white").grid(row=4, column=2)
            Button(r, text="leave", width=6, command=lambda:leave(7)).grid(row=5, column=2)
            addtofile()
        elif parkno.get() == "8":
            print("in")
            global slot8
            slot8 = parking(ticketno.get(), 8,name.get(),vechno.get())
            print(slot8.parkticket)
            print(slot8.park)

            messagebox.showinfo("SUCESS ", "your car is parked safely")
            Button(r, text="NP", border=0, fg="white", bg="red", width=6, height=4, activebackground="red",
                   activeforeground="white").grid(row=4, column=3)
            Button(r, text="leave", width=6, command=lambda:leave(8)).grid(row=5, column=3)
            addtofile()
    else:
        messagebox.showerror("ERROR", "INCORRECT TICKET NUMBER")

def leave(j):
    global checkticketno1
    global  parknoleave,checkparkname,checkparkvechno


    rw = Toplevel(r)
    rw.geometry("300x300")
    rw.configure(bg="skyblue")
    rw.title("LOGIN")
    checkticketno1 = StringVar()
    checkparkname = StringVar()
    checkparkvechno = StringVar()
    parknoleave = StringVar()
    Label(rw, text="NAME").grid(row=0, column=0)
    Entry(rw, textvariable=checkparkname).grid(row=0, column=1)
    Label(rw, text="VECHILE NO.").grid(row=1, column=0)
    Entry(rw, textvariable=checkparkvechno).grid(row=1, column=1)
    Label(rw, text="slotno").grid(row=2, column=0)
    parknoleave.set(j)
    Entry(rw, textvariable=parknoleave,state=DISABLED).grid(row=2, column=1)






    Button(rw, text="submit",command=leavecheck).grid(row=3, column=0)






def leavecheck():





    if 1>2:
        print("1")
    elif slot1.parkname == checkparkname.get() and slot1.park==1 and slot1.parkvechno == checkparkvechno.get():
        messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

        Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
               activeforeground="red").grid(row=2, column=0)
        Button(r, text="Park", command=lambda:park(1), width=6).grid(row=3, column=0,pady=(0,20),padx=10)

    elif slot2.parkname == checkparkname.get() and slot2.park==2 and slot2.parkvechno == checkparkvechno.get():
        messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

        Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
               activeforeground="red").grid(row=2, column=1)
        Button(r, text="Park", command=lambda:park(2), width=6).grid(row=3, column=1,pady=(0,20),padx=10)
    elif slot3.parkname == checkparkname.get() and slot3.park==3 and slot3.parkvechno == checkparkvechno.get():
        messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

        Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
               activeforeground="red").grid(row=2, column=2)
        Button(r, text="Park", command=lambda:park(3), width=6).grid(row=3, column=2,pady=(0,20),padx=10)
    elif slot4.parkname == checkparkname.get() and slot4.park==4 and slot4.parkvechno == checkparkvechno.get():
        messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

        Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
               activeforeground="red").grid(row=2, column=3)
        Button(r, text="Park", command=lambda:park(4), width=6).grid(row=3, column=3,pady=(0,20),padx=10)
    elif slot5.parkname == checkparkname.get() and slot5.park==5 and slot5.parkvechno == checkparkvechno.get():
        messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

        Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
               activeforeground="red").grid(row=4, column=0)
        Button(r, text="Park", command=lambda:park(5), width=6).grid(row=5, column=0)
    elif slot6.parkname == checkparkname.get() and slot6.park==6 and slot6.parkvechno == checkparkvechno.get():
        messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

        Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
               activeforeground="red").grid(row=4, column=1)
        Button(r, text="Park", command=lambda:park(6), width=6).grid(row=5, column=1)
    elif slot7.parkname == checkparkname.get() and slot7.park==7 and slot7.parkvechno == checkparkvechno.get():
        messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

        Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
               activeforeground="red").grid(row=4, column=2)
        Button(r, text="Park", command=lambda:park(7), width=6).grid(row=5, column=2)
    elif slot8.parkname == checkparkname.get() and slot8.park==8 and slot8.parkvechno == checkparkvechno.get():
        messagebox.showinfo("PARKING,ltd", "Thanks for using parking,ltd")

        Button(r, text="P", border=0, fg="red", bg="black", width=6, height=4, activebackground="black",
               activeforeground="red").grid(row=4, column=3)
        Button(r, text="Park", command=lambda:park(8), width=6).grid(row=5, column=3)


    else:
        messagebox.showerror("ERROR", "INCORRECT CRIDENTIALS")











def i():
    messagebox.showinfo("INFO",
                        '''welcome to parking ltd
                        
    1.click on park to park ur car
    2.click on leave to take ur car
                        
        Happy to help you''')

def ticket():
    a=str(random.randint(100000,200000))
    global b
    b=a

    popup=Toplevel(r)
    popup.title("TICKET")
    popup.geometry("300x300")

    Label(popup, text="                   ").grid(row=0, column=0)
    Label(popup,text="YOUR TICKET NO IS "+a).grid(row=1,column=1)

def addtofile():




    list=[str(parkno.get()),str(name.get()),str(vechno.get()),str(datetime.now().date()),str(datetime.now().time())]

    
    from csv import writer
    with open("parkingfile.csv", 'a+', newline='') as write_obj:

        csv_writer = writer(write_obj)

        csv_writer.writerow(list)










from tkinter import *
from tkinter import messagebox


r=Tk( )
r.configure(bg="grey")
Button(r,text="P",border=0,fg="red",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=2,column=0)
Button(r,text="Park",width=6,command=lambda:park(1)).grid(row=3,column=0,pady=(0,20),padx=10)

Button(r,text="P",border=0,fg="red",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=2,column=1)
Button(r,text="Park",width=6,command=lambda:park(2)).grid(row=3,column=1,pady=(0,20),padx=10)

Button(r,text="P",border=0,fg="red",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=2,column=2)
Button(r,text="Park",width=6,command=lambda:park(3)).grid(row=3,column=2,pady=(0,20),padx=10)

Button(r,text="P",border=0,fg="red",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=2,column=3)
Button(r,text="Park",width=6,command=lambda:park(4)).grid(row=3,column=3,pady=(0,20),padx=10)

Button(r,text="P",border=0,fg="red",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=4,column=0)
Button(r,text="Park",width=6,command=lambda:park(5)).grid(row=5,column=0)

Button(r,text="P",border=0,fg="red",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=4,column=1)
Button(r,text="Park",width=6,command=lambda:park(6)).grid(row=5,column=1)

Button(r,text="P",border=0,fg="red",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=4,column=2)
Button(r,text="Park",width=6,command=lambda:park(7)).grid(row=5,column=2)

Button(r,text="P",border=0,fg="red",bg="black",width=6,height=4,activebackground="black",activeforeground="green").grid(row=4,column=3)
Button(r,text="Park",width=6,command=lambda:park(8)).grid(row=5,column=3)

Label(r,text="WELCOME TO PARKING.LTD",fg="white",bg="black").grid(row=0,column=5)

Button(r,text="INFO",fg="white",bg="blue",command=i).grid(row=6,column=0)

r.mainloop( )







