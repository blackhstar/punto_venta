import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from container import Container
from PIL import Image, ImageTk

class Login(tk.Frame):
        db_name = "DBPOS.db"

        def __init__(self, padre , controlador):
            super().__init__(padre)
            self.place(x=0 , y= 0 , width = 1100 , height=650)
            self.controlador = controlador
            self.logged_user = None
            self.widgets()

        def validacion(self, user, pas):
            return len(user) > 0 and len(pas) > 0
        
        def login(self):
            user = self.username.get()
            pas = self.password.get()
            if self.validacion(user, pas):
                consulta = f"SELECT * FROM DBUSER WHERE USRNICKNAME = ? AND USRPASSWORD = ?"
                parametros = (user, pas)
                try:
                    with sqlite3.connect(self.db_name) as conn:
                        cursor = conn.cursor()
                        cursor.execute(consulta, parametros)
                        resultado = cursor.fetchall()
                    if resultado:
                        self.logged_user = user
                        self.control(user)
                        messagebox.showinfo("Bienvenido", f"Bienvenido, {user}")
                    else:
                        self.username.delete(0, END)
                        self.password.delete(0, END)
                        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
                except sqlite3.Error as e:
                    messagebox.showerror("Error", "Error al conectar a la base de datos: {}".format(e))
            else:
                messagebox.showerror("Error", "Llene todos los campos")

        def control(self , user):
             self.controlador.show_frame(Container , user )

        def control2(self):
            self.controlador.show_frame(Registro )

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

            password = tk.Label(frame1 , text="Contraseña" , font="sans 16 bold" , background="#FFFFFF")
            password.place(x=100, y=340)
            self.password = ttk.Entry( frame1 , font="sans 16 bold" , background="#FFFFFF",show="*")
            self.password.place(x=100, y=380, width=240 , height=40)

            btn1 = tk.Button(frame1 , text="Iniciar" , font="sans 16 bold" , background="#87fd7d", command=self.login)
            btn1.place(x=100, y=440, width=240 , height=40)

            btn2 = tk.Button(frame1 , text="Registrar" , font="sans 16 bold" , background="#ff4e2a", command=self.control2)
            btn2.place(x=100, y=500, width=240 , height=40)


class Registro(tk.Frame):
        db_name = "DBPOS.db"

        def __init__(self, padre , controlador):
            super().__init__(padre)
            self.place(x=0 , y= 0 , width = 1100 , height=650)
            self.controlador = controlador
            self.widgets()

        def validacion(self, user, pas):
            return len(user) > 0 and len(pas) > 0
        
        def eje_consulta(self , consulta , parametros = ()):
            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros)
                    conn.commit()
            except sqlite3.Error as e:
                messagebox.showerror("Error", "Error al conectar a la base de datos: {}".format(e))
                return None
            
        def registro(self):
            user = self.username.get()
            pas = self.password.get()
            key = self.key.get()
            if self.validacion(user, pas):
                if len(pas) > 6:
                    consulta = "INSERT INTO DBUSER (USRNICKNAME, USRNAME, USRPASSWORD) VALUES (?, ?, ?)"
                    parametros = (user, user, pas)
                    self.eje_consulta(consulta, parametros)
                    messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente")
                    self.username.delete(0, END)
                    self.password.delete(0, END)
                    self.key.delete(0, END)
                    self.control2()
                else:
                    messagebox.showerror("Error", "La contraseña debe tener mas de 6 caracteres")
            else:
                messagebox.showerror("Error", "Llene todos los campos")

        def control(self ):
            self.controlador.show_frame(Container)

        def control2(self):
            self.controlador.show_frame(Login )

        def widgets(self):
            fondo = tk.Frame(self , bg="#a9a9a9", highlightbackground="gray", highlightthickness=1)
            fondo.place(x=0 , y=0 , width=1100 , height=650)
  
            frame1 = tk.Frame(self , bg="#FFFFFF", highlightbackground="black", highlightthickness=1)
            frame1.place(x=350 , y=10 , width=400 , height=630)

            self.logo_image = Image.open("imagenes/logo.png")
            self.logo_image = self.logo_image.resize((200, 200), Image.Resampling.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = tk.Label(frame1 , image=self.logo_image , bg="#ffffff")
            self.logo_label.place(x=100, y=20)
            
            user = tk.Label(frame1 , text="Nombre de usuario" , font="sans 16 bold" , background="#FFFFFF")
            user.place(x=100, y=250)
            self.username = ttk.Entry( frame1 , font="sans 16 bold" , background="#FFFFFF")
            self.username.place(x=100, y=290, width=240 , height=40)

            password = tk.Label(frame1 , text="Contraseña" , font="sans 16 bold" , background="#FFFFFF")
            password.place(x=100, y=340)
            self.password = ttk.Entry( frame1 , font="sans 16 bold" , background="#FFFFFF",show="*")
            self.password.place(x=100, y=380, width=240 , height=40)

            key = tk.Label(frame1 , text="Codigo de acceso" , font="sans 16 bold" , background="#FFFFFF")
            key.place(x=100, y=430)
            self.key = ttk.Entry( frame1 , font="sans 16 bold" , background="#FFFFFF",show="*")
            self.key.place(x=100, y=470, width=240 , height=40)

            btn3 = tk.Button(frame1 , text="Registrarse" , font="sans 16 bold" , background="#87fd7d" , command=self.registro)
            btn3.place(x=100, y=520, width=240 , height=40)

            btn4 = tk.Button(frame1 , text="Regresar" , font="sans 16 bold" , background="#ff4e2a" , command=self.control2)
            btn4.place(x=100, y=570, width=240 , height=40)