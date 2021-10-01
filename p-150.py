from tkinter import *
import random
root=Tk()
root.title("1D list")
root.geometry("400x400")


labelitems = Label(root,text="water,blanket,food,book,chips")
label_display = Label(root)

def randomnumberlist():
    randomitem=random.sample(range(labelitems,1,5),1)
    labelitems["text"]="Random list: " + str(randomList)
    randomList.sort()
    label_display["text"]="remember item: " + str(randomitem)
    

btn = Button(root,text="Generate random item",command=randomnumberlist)



labelitems.pack()
btn.pack()
label_display.pack()












root.mainloop()
