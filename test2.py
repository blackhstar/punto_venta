from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Inicio de sesion')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False , False )

img = PhotoImage(file='src/img/login.png')
Label(root , image=img , bg='white').place(x=50, y=50)

frame=Frame(root, width=350, height=350 , bg="white")
frame.place(x=480,y=70)

heading=Label(frame , text='Inicio de sesion', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

###########################################

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0,'Usuario')


user = Entry(frame , width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11) )
user.place(x=30,y=80)
user.insert(0,'Usuario')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295,height=2,bg='black').place(x=25,y=107)

#############################################

code = Entry(frame , width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11) )
code.place(x=30,y=150)
code.insert(0,'Contraseña')

Frame(frame, width=295,height=2,bg='black').place(x=25,y=177)

############################################

Button(frame,width=39,pady=7,text='Inicio de sesion', bg='#57a1f8', fg='white', border=0).place(x=35,y=204)


root.mainloop()