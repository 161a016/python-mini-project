from tkinter import *
import os

tk=Tk()

def getvals():
    print('Submitting forms')

    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodServicevalue.get()}")
    os.getcwd()
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),foodServicevalue.get()}\n")

tk.geometry("1500x400")
tk.title('this is my second application that i have made ')

Label(tk,text="Welcome to rishabh first tool",font="comicsansms 13 bold ",pady=13).grid(row=0,column=3)

name=Label(tk,text="Name")
phone=Label(tk,text="Phone")
gender=Label(tk,text="Gender")
emergency=Label(tk,text="Emergency")
paymentmode=Label(tk,text="payment")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)


namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodServicevalue=IntVar()

nameentry=Entry(tk,textvariable=namevalue)
phonentry=Entry(tk,textvariable=phonevalue)
genderentry=Entry(tk,textvariable=gendervalue)
emergencyentry=Entry(tk,textvariable=emergencyvalue)
paymentmodeentry=Entry(tk,textvariable=paymentmodevalue)
foodServiceentry=Entry(tk,textvariable=foodServicevalue)

nameentry.grid(row=1,column=3)
phonentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)
foodServiceentry.grid(row=6,column=3)

foodservice=Checkbutton(text="Wants a prebook your meals",variable=foodServicevalue)

foodservice.grid(row=6,column=3)


Button(text="Summit your meal",command=getvals).grid(row=7,column=3)









tk.mainloop()