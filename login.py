from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk

class Login(tk.Frame):
        def __init__(self, padre , controlador):
            super().__init__(padre)
            self.place(x=0 , y= 0 , width = 1100 , height=650)
            self.controlador = controlador
            self.logged_user = None
            self.widgets()

        def widgets(self):
            fondo = tk.Frame(self , bg="#a9a9a9", highlightbackground="gray", highlightthickness=1)
            fondo.place(x=0 , y=0 , width=1100 , height=650)

            frame1 = tk.Frame(self , bg="#FFFFFF", highlightbackground="black", highlightthickness=1)
            frame1.place(x=350 , y=50 , width=400 , height=560)

            self.logo_image = Image.open("imagenes/logo.png")
            self.logo_image = self.logo_image.resize((200, 200), Image.Resampling.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = tk.Label(frame1 , image=self.logo_image , bg="#ffffff")
            self.logo_label.place(x=100, y=20)

            user = tk.Label(frame1 , text="Nombre de usuario" , font="sans 16 bold" , background="#FFFFFF")
            user.place(x=100, y=250)
            self.username = ttk.Entry( frame1 , font="sans 16 bold" , background="#FFFFFF")
            self.username.place(x=100, y=290, width=240 , height=40)

            #self.entry_user = tk.Entry(frame1 , font="sans 12 bold" , bg="#FFFFFF")
            #SSself.entry_user.place(x=100, y=280)

            password = tk.Label(frame1 , text="Contraseña" , font="sans 16 bold" , background="#FFFFFF")
            password.place(x=100, y=340)
            self.password = ttk.Entry( frame1 , font="sans 16 bold" , background="#FFFFFF",show="*")
            self.password.place(x=100, y=380, width=240 , height=40)

            btn1 = tk.Button(frame1 , text="Iniciar" , font="sans 16 bold" , background="#87fd7d")
            btn1.place(x=100, y=440, width=240 , height=40)

            btn1 = tk.Button(frame1 , text="Registrar" , font="sans 16 bold" , background="#ff4e2a")
            btn1.place(x=100, y=500, width=240 , height=40)

            #logo = tk.PhotoImage(file="logo.png")
            #logo_label = tk.Label(fondo , image=logo , bg="#a9a9a9")
            #logo_label.place(x=100 , y=100)
            #self.lbl_user = tk.Label(fondo , text="Usuario" , font="sans 12 bold" , bg="#FFFFFF")
            #self.lbl_user.place(x=100 , y=200)

class Registro(tk.Frame):
        def __init__(self, padre , controlador):
            super().__init__(padre)
            self.place(x=0 , y= 0 , width = 1100 , height=650)
            self.controlador = controlador
            self.widgets()

        def widgets(self):
              label = Label(self, text="Registros")
              label.pack()