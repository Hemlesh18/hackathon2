from tkinter import *
from tkinter import messagebox
import tkinter as tk
import customtkinter

root = tk.Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

###### it's the picture###
img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

#### it's the frame
Frame=Frame(root,width=350,height=350,bg="white")
Frame.place(x=480,y=70)

#### it's the heading
heading=Label(Frame,text=' Welcome Jarvise',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=70,y=5)



#### it's the question text box

user = Entry(Frame,width=30,fg='black',border=1,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=28, y=80)
user.insert(0,'provide your question')


#####it's the answere text box

text_area = Text(root,font="Robote 10",bg="white")
text_area.place(x=508, y=200,width=250,height=250)

### it's a button

hello_button=tk.Button(Frame,text="start",fg="black",bg="blue")
hello_button.place(x=30, y=50)

quit_button=tk.Button(Frame,text="Quit",fg="black",bg="red",command=quit)
quit_button.place(x=70, y=50)




root.mainloop()


















