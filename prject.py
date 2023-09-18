from tkinter import*
root = Tk()
root.title('Project')
root.geometry('800x600')

def display():
        n=int(var.get())
        a=int(e1.get())
        b=int(e2.get())
        m,t=0,0
        str=""
        if(n==1):
            k=a&b
        elif(n==2):
            k=a|b
        elif(n==3):
            k=~a
            p=~b
        elif(n==4):
            k=a^b
        if(n==3):
            m=k
            t=p
            stm="%s"%m+",%s"%t
            myText.set(stm) 
        if(n in [1,2,4]):
            m=k
            myText.set(m) 

def clear_all() : 
  
    # whole content of entry boxes is deleted  
    e1.delete(0)    
    e2.delete(0, END)
    #for deseleting radiobuttons
    r1.deselect()
    r2.deselect()
    r3.deselect()    
    r4.deselect()
    #To clear the content of a disabled field first we able it then we delete it
    e4.config(state=NORMAL)
    e4.delete(0,END)
    e4.config(state=DISABLED)
    #setting focus on the first number entry field
    e1.focus_set()    

def exp_window():
    newin= Toplevel(root)
    newin.title("New Window")
    newin.geometry("800x600")
    def exit():
        newin.destroy()
    def calc2():
        k,p=0,0
        str1,str2="",""
        a=int(e1.get())
        b=int(e2.get())
        n=int(var.get())
        no1.set(a)
        no2.set(b)
        bi1=bin(a)
        bi2=bin(b)
        binary1.set(bi1[2:])
        binary2.set(bi2[2:])
        if(n==1):
            op.set("AND")
            k=a&b
        elif(n==2):
            op.set("OR")
            k=a|b
        elif(n==3):
            op.set("NOT")
            k=~a
            p=~b
        elif(n==4):
            op.set("XOR")
            k=a^b
        if(n==3):
            an1=bin(k)
            an2=bin(p)
            o1=an1[3:]
            o2=an2[3:]
            str1="%s,"%o1,"%s"%o2
            opans.set(str1)
            str2="%s"%k,",%s"%p
            deci.set(str2)
            
        if(n in [1,2,4]):
            an=bin(k)
            opans.set(an[2:])
            deci.set(k)
    no1=StringVar()
    no2=StringVar()
    binary1=StringVar()
    binary2=StringVar()
    op=StringVar()
    opans=StringVar()
    op.set("Operation")
    deci=StringVar()
    calc2()
    exp=Frame(newin, height=600, width=800, bg='grey', cursor='cross')
    num1=Label(exp,text='Number 1',font=('courier',20), fg='blue', bg='yellow')
    num1.place(x=120,y=100)
    val1=Entry(exp,text="",textvariable=no1,state=DISABLED,width=5, fg='blue', bg='white',font=('Arial',20))
    val1.place(x=250,y=100)
    num2=Label(exp,text='Number 2',font=('courier',20), fg='blue', bg='yellow')
    num2.place(x=120,y=140)
    val2=Entry(exp,text="",textvariable=no2,state=DISABLED,width=5, fg='blue', bg='white',font=('Arial',20))
    val2.place(x=250,y=140)
    bin1=Label(exp,text='Binary 1',font=('courier',20), fg='blue', bg='yellow')
    bin1.place(x=400,y=100)
    val3=Entry(exp,text="",textvariable=binary1,state=DISABLED,width=10, fg='blue', bg='white',font=('Arial',20))
    val3.place(x=535,y=100)
    bin2=Label(exp,text='Binary 2',font=('courier',20), fg='blue', bg='yellow')
    bin2.place(x=400,y=140)
    val4=Entry(exp,text="",textvariable=binary2,state=DISABLED,width=10, fg='blue', bg='white',font=('Arial',20))
    val4.place(x=535,y=140)
    op=Label(exp,text="",textvariable=op,state=DISABLED,width=8,font=('courier',20), fg='blue', bg='pink')
    op.place(x=400,y=200)
    op_val=Entry(exp,text="",textvariable=opans,state=DISABLED,width=10, fg='blue', bg='white',font=('Arial',20))
    op_val.place(x=535,y=200)
    dec_res=Label(exp,text='Decimal Result',font=('courier',18), fg='blue', bg='orange')
    dec_res.place(x=250,y=300)
    dec_val=Entry(exp,text="",textvariable=deci,state=DISABLED,width=8, fg='blue', bg='white',font=('Arial',19))
    dec_val.place(x=452,y=300)
    exit_b=Button(exp,text='Exit', width=15, height=2,bg='green3', fg='blue', activebackground='green',activeforeground='red',command=exit)
    exit_b.place(x=350,y=370)
    exp.pack()
    newin.mainloop()    
    
f=Frame(root, height=600, width=800, bg='grey', cursor='cross')
f.propagate(0)
l1=Label(f,text='Number 1',font=('courier', 20), fg='blue', bg='yellow')
l1.place(x=150,y=100)
l2=Label(f,text='Number 2',font=('courier', 20), fg='blue', bg='yellow')
l2.place(x=470,y=100)
e1=Entry(f,width=5, fg='blue', bg='white',font=('Arial', 20))
#e1.bind('',display)
e1.place(x=285,y=100)
e2=Entry(f,width=5, fg='blue', bg='white',font=('Arial', 20))
#e2.bind('',display)
e2.place(x=606,y=100)

var=IntVar()
r1=Radiobutton(f,bg='pink',fg='green', font=('Georgia', 20),text='AND', variable=var,value=1)
r1.place(x=150,y=170)
r2=Radiobutton(f,bg='pink',fg='green', font=('Georgia', 20),text='OR', variable=var,value=2)
r2.place(x=360,y=170)
r3=Radiobutton(f,bg='pink',fg='green', font=('Georgia', 20),text='NOT', variable=var,value=3)
r3.place(x=150,y=218)
r4=Radiobutton(f,bg='pink',fg='green', font=('Georgia', 20),text='XOR', variable=var,value=4)
r4.place(x=360,y=218)

b1=Button(f,text='Result', width=15, height=2,bg='orange', fg='blue', activebackground='green',activeforeground='red',command=display)
b1.place(x=235,y=300)
b2=Button(f,text='Explaination', width=15, height=2,bg='orange', fg='blue', activebackground='green',activeforeground='red',command=exp_window)
b2.place(x=435,y=300)

myText=StringVar()
l3=Label(f,text='Result is:',font=('courier', 20), fg='blue', bg='yellow')
l3.place(x=150,y=390)
e4=Entry(f,text="",textvariable=myText,state=DISABLED,font=('courier', 20), fg='black', bg='White')
e4.place(x=315,y=390)

b3=Button(f,text='Clear', width=15, height=2,bg='green3', fg='blue', activebackground='green',activeforeground='red',command=clear_all)
b3.place(x=335,y=460)
f.pack()
root.mainloop()
#coded by shadan 