from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk

class Login(tk.Frame):
        def __init__(self, padre , controlador):
            super().__init__(padre)
            self.place(x=0 , y= 0 , width = 1100 , height=650)
            self.controlador = controlador
            self.logged_user = None
            self.widgets()

        def widgets(self):
              label = Label(self, text="Login")
              label.pack()

class Registro(tk.Frame):
        def __init__(self, padre , controlador):
            super().__init__(padre)
            self.place(x=0 , y= 0 , width = 1100 , height=650)
            self.controlador = controlador
            self.widgets()

        def widgets(self):
              label = Label(self, text="Registros")
              label.pack()