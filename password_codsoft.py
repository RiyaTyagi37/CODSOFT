from tkinter import*
import random
import string

root=Tk()
root.geometry("750x750")
root.title("Password generator")
myframe=LabelFrame(root,text="Password Generator")
myframe.pack()
mylabel=Label(myframe,text="Enter length")
mylabel.grid(row = 0, column = 0, pady = 2)
ent=Entry(myframe,width=10,borderwidth=5)
ent.grid(row = 0, column = 1, pady = 2)
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
number=['0','1','2','3','4','5','6','7','8','9','0']
password=[]
special=list(string.punctuation)

#to use the button
def eas():
    x=int(ent.get())
    if (x<6):
        slabel=Label(myframe,text="Minimum number must be 6")
        slabel.grid(row=4,column=0)
    elif (x>12):
        slabel2=Label(myframe,text="Maximum number must be 12")
        slabel2.grid(row=4,column=0)
    else:
        password.append(random.choice(upper))
        password.append(random.choice(number))
        password.append(random.choice(special))
        for i in range(3,x):
            password.append(random.choice(lower))
        random.shuffle(password)
        generated_password = ''.join(password)
        mylabel5.config(text=generated_password)
def med():
        x=int(ent.get())
        if (x<6):
            slabel=Label(myframe,text="Minimum number must be 6")
            slabel.grid(row=4,column=0)
        elif (x>12):
            slabel2=Label(myframe,text="Maximum number must be 12")
            slabel2.grid(row=4,column=0)
        else:
            password.append(random.choice(special))
            for i in range(2):
                password.append(random.choice(upper))
                password.append(random.choice(number))
            for i in range(x-5):
                password.append(random.choice(lower))
            random.shuffle(password)
            y=''.join(password)
            mylabel5.config(text=y)
def hard():
    x=int(ent.get())
    if (x<6):
        slabel=Label(myframe,text="Minimum number must be 6")
        slabel.grid(row=4,column=0)
    elif (x>12):
        slabel2=Label(myframe,text="Maximum number must be 12")
        slabel2.grid(row=4,column=0)
    else:
        for i in range(x//4):
            password.append(random.choice(upper))
            password.append(random.choice(number))
            password.append(random.choice(lower))
            password.append(random.choice(special))
        for i in range(x%4):
            password.append(random.choice(lower))
        random.shuffle(password)
        y=''.join(password)
        mylabel5.config(text=y)
    
mybutton=Button(myframe,text="Easy",command=eas)
mybutton.grid(row=2,column=0,pady=2)
mybutton2=Button(myframe,text="Medium",command=med)
mybutton2.grid(row=2,column=1,pady=2)
mybutton3=Button(myframe,text="Hard",command=hard)
mybutton3.grid(row=2,column=2,pady=2)
mylabel4=Label(myframe,text="Password")
mylabel4.grid(row=3,column=0,pady=2)
mylabel5=Label(myframe,text="                ",bg="white")
mylabel5.grid(row=3,column=1,pady=2)
root.mainloop()
