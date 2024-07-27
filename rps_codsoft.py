from tkinter import*
import random
root=Tk()
root.geometry("750x750")
root.title("Game")
myframe=LabelFrame(root,text="STONE PAPER SCISSOR")
myframe.pack()
label1=Label(myframe,text="STONE PAPER SCISSOR")
label1.grid(row=0,column=2,pady=2)

c=["ROCK","PAPER","SCISSOR"]
a=""
comp=0
you=0

def scissor():
    global a
    a="SCISSOR"
    b=random.choice(c)
    label5.config(text=a)   
    label3.config(text=b)
    winlose(a,b)
    
def rock():
    global a
    a="ROCK"
    b=random.choice(c)
    label5.config(text=a)
    label3.config(text=b)
    winlose(a,b)
    
def paper():
    global a
    a="PAPER"
    b=random.choice(c)
    label5.config(text=a)
    label3.config(text=b)
    winlose(a,b)
    

def winlose(a,b):
    global comp
    global you
    if a=="ROCK" and b=="ROCK":
        pass    
    elif a=="ROCK" and b=="PAPER":
        comp=comp+1   
    elif a=="ROCK" and b=="SCISSOR":
        you=you+1   
    elif a=="PAPER" and b=="ROCK":
        you=you+1    
    elif a=="PAPER" and b=="PAPER":
        pass    
    elif a=="PAPER" and b=="SCISSOR":
        comp=comp+1   
    elif a=="SCISSOR" and b=="ROCK":
        comp=comp+1    
    elif a=="SCISSOR" and b=="PAPER":
        you=you+1    
    elif a=="SCISSOR" and b=="SCISSOR":
        pass
    a=str(comp)
    b=str(you)
    label8.config(text=a)
    label9.config(text=b)
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    
def replay():
    global a
    a = ""
    label5.config(text="                   ")
    label3.config(text="                   ")
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    

photo = PhotoImage(file = r"C:\Users\Tanishk\Downloads\scissor.jpeg").subsample(5,5)
button1=Button(myframe,text="SCISSOR",image=photo,command=scissor)
button1.grid(row=1,column=0,padx=10,pady=10)

photo2=PhotoImage(file=r"C:\Users\Tanishk\Downloads\paper.jpeg").subsample(5,5)
button2=Button(myframe,text="PAPER",image=photo2,command=paper)
button2.grid(row=1,column=2,pady=2)

photo3=PhotoImage(file=r"C:\Users\Tanishk\Downloads\rock2.png").subsample(2,2)
button3=Button(myframe,text="ROCK",image=photo3,command=rock)
button3.grid(row=1,column=4,padx=20,pady=2)

label2=Label(myframe,text="Computer choose")
label2.grid(row=3,column=0,padx=55,columnspan=3)
label3=Label(myframe,text="                   ",bg="pink")
label3.grid(row=3,column=3,columnspan=2)
label4=Label(myframe,text="You choose")
label4.grid(row=5,column=0,padx=55,pady=10,columnspan=3)
label5=Label(myframe,text="                   ",bg="sky blue")
label5.grid(row=5,column=3,columnspan=2)
label6=Label(myframe,text="COMPUTER")
label6.grid(row=6,column=2,columnspan=2,pady=10)
label7=Label(myframe,text="You")
label7.grid(row=6,column=4,columnspan=2)
label8=Label(myframe,text="     0      ",bg="pink")
label8.grid(row=7,column=2,columnspan=2)
label9=Label(myframe,text="     0        ",bg="sky blue")
label9.grid(row=7,column=4,columnspan=2)

button4=Button(myframe,text="Play again",command=replay)
button4.grid(row=8,column=2,pady=30,padx=50,columnspan=2)
button5=Button(myframe,text="EXIT",command=root.destroy)
button5.grid(row=9,column=2,padx=50,pady=10,columnspan=2)

root.mainloop()
