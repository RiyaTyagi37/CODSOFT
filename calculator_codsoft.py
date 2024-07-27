from tkinter import*

def click(value):
    x=ent.get()
    if value=="AC":
        ent.delete(0,END)
    elif value=="+/-":
        if x:
            if x[0]=="-":
                ent.delete(0)
            else:
                ent.insert(0,"-")
    elif value=="=":
        try:
            b=eval(x)
            ent.delete(0,END)
            ent.insert(END,b)
        except exception as e:
            ent.delete(0,END)
            ent.insert(END,"ERROR")
    else:
        ent.insert(END,value)

        

root=Tk()        
root.geometry("750x750")
root.title("Calculator")
myframe=LabelFrame(root,text="Calculator")
myframe.pack()
 
ent=Entry(myframe,width=15)
ent.grid(row = 1, column = 0, pady = 2,columnspan=3)
buttons=[
    ("AC",2,0),("+/-",2,1),("%",2,2),("/",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("*",3,3),
    ("4",4,0),("5",4,1),("6",4,2),("-",4,3),
    ("7",5,0),("8",5,1),("9",5,2),("+",5,3),
    ("0",6,0,2),(".",6,2),("=",6,3)
]
for(text,row,col,*span) in buttons:
    width=5 if text=="0" else 4
    columnspan =span[0] if span else 1
    Button(myframe,text=text,width=width,command=lambda t=text: click(t)).grid(row=row,column=col,columnspan=columnspan,pady=2)
root.mainloop()
