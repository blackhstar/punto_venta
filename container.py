from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from ventas import Ventas
from dashboard import Dashboard
from clientes import Clientes
from inventario import Inventario
from reportes import Reportes
from PIL import Image, ImageTk
import datetime
#from login import Login

class Container(tk.Frame):
      def __init__(self, padre, controlador, user=None):
            super().__init__(padre)
            self.controlador = controlador
            self.user = user
            self.pack()
            self.place( x=0 , y=0, width=1100 , height=650 )
            self.widgets()
            self.frames = {}
            self.buttons = []

            for i in (Dashboard , Ventas , Clientes , Inventario , Reportes):
                  frame = i(self)
                  self.frames[i] = frame
                  frame.pack()
                  frame.config(bg="#dcdcdc",highlightbackground="gray" , highlightthickness=1)
                  frame.place(x=200, y=50, width=900, height=600)

            self.show_frames(Dashboard)
            self.hide_all_indicators()
            self.btn_dashboard_indicator.place(x=3, y=180, width=5, height=40)
            self.label_user = None

      def set_user(self, user):
            self.user = user
            if self.label_user:
                  self.label_user.destroy()

            self.label_user = Label(self.frame1 , text=f"Bienvenido: {self.user}" , font="sans 14 bold" , bg="#a9a9a9" , padx=10 )
            self.label_user.place(x=300 , y=10)

      def show_frames(self, container):
            frame = self.frames[container]
            self.hide_all_indicators()
            frame.tkraise()

      def dashboard(self):
            self.show_frames(Dashboard)
            self.hide_all_indicators()
            self.btn_dashboard_indicator.place(x=3, y=180, width=5, height=40)

      def ventas(self):
            self.show_frames(Ventas)
            self.hide_all_indicators()
            self.btn_ventas_indicator.place(x=3, y=230, width=5, height=40)

      def clientes(self):
            self.show_frames(Clientes)
            self.hide_all_indicators()
            self.btn_clientes_indicator.place(x=3, y=280, width=5, height=40) 

      def inventario(self):
            self.show_frames(Inventario)
            self.hide_all_indicators()
            self.btn_inventario_indicator.place(x=3, y=330, width=5, height=40)

      def reportes(self):
            self.show_frames(Reportes)
            self.hide_all_indicators()
            self.btn_reportes_indicator.place(x=3, y=380, width=5, height=40)

      def widgets(self):
         
            self.frame1 = tk.Frame(self , bg="#a9a9a9" , highlightbackground="gray" , highlightthickness=1)
            self.frame1.place(x=0 , y=0, width=1100, height=50)

            label_app = Label(self.frame1 , text="Mi punto de venta" , font="sans 14 bold" , bg="#a9a9a9" )
            label_app.place(x=20 , y=10)

            self.label_fecha = Label(self.frame1 , text="" , font="sans 14 bold" , bg="#a9a9a9" )
            self.label_fecha.place(x=850 , y=10)

            self.label_hora = Label(self.frame1 , text="" , font="sans 14 bold" , bg="#a9a9a9" )
            self.label_hora.place(x=980 , y=10)

            self.actualizar_fecha_hora()

            self.frame2 = tk.Frame(self , bg="#ffffff" , highlightbackground="gray" , highlightthickness=1)
            self.frame2.place(x=0 , y=50, width=200, height=600)

            self.logo_image = Image.open("imagenes/logo.png")
            self.logo_image = self.logo_image.resize((140, 140), Image.Resampling.LANCZOS)
            self.logo_image = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = tk.Label(self.frame2 , image=self.logo_image , bg="#ffffff")
            self.logo_label.place(x=30, y=10)

            self.btn_dashboard = Button(self.frame2 , text="Dashboard" , font="sans 16 bold" , bg="white" , borderwidth=0 , highlightthickness=0 , command=self.dashboard)
            self.btn_dashboard.place(x=10, y=180, width=185, height=40)
            self.btn_dashboard_indicator = Label(self.frame2 , bg="black")

            self.btn_ventas = Button(self.frame2 , text="Ventas" , font="sans 16 bold" , bg="white" , borderwidth=0 , highlightthickness=0 , command=self.ventas)
            self.btn_ventas.place(x=10, y=230, width=185, height=40)
            self.btn_ventas_indicator = Label(self.frame2 , bg="black")

            self.btn_clientes = Button(self.frame2 , text="Clientes" , font="sans 16 bold" , bg="white" , borderwidth=0 , highlightthickness=0 , command=self.clientes)
            self.btn_clientes.place(x=10, y=280, width=185, height=40)
            self.btn_clientes_indicator = Label(self.frame2 , bg="black")

            self.btn_inventario = Button(self.frame2 , text="Inventario" , font="sans 16 bold" , bg="white" , borderwidth=0 , highlightthickness=0 , command=self.inventario)
            self.btn_inventario.place(x=10, y=330, width=185, height=40)
            self.btn_inventario_indicator = Label(self.frame2 , bg="black")      

            self.btn_reportes = Button(self.frame2 , text="Reportes" ,  font="sans 16 bold" , bg="white" , borderwidth=0 , highlightthickness=0 , command=self.reportes)
            self.btn_reportes.place(x=10, y=380, width=185, height=40)
            self.btn_reportes_indicator = Label(self.frame2 , bg="black")

            self.buttons = [self.btn_dashboard, self.btn_ventas, self.btn_clientes, self.btn_inventario, self.btn_reportes]

            lblversion = Label(self.frame2 , text="Versión 1.0" , font="sans 10 bold" , bg="#FFFFFF")
            lblversion.place(x=40, y=550)
            #self.indicators = [self.btn_dashboard_indicator, self.btn_ventas_indicator, self.btn_clientes_indicator, self.btn_inventario_indicator, self.btn_reportes_indicator]    

      def hide_all_indicators(self):
            for btn_indicator in [
                  self.btn_dashboard_indicator, 
                  self.btn_ventas_indicator, 
                  self.btn_clientes_indicator, 
                  self.btn_inventario_indicator, 
                  self.btn_reportes_indicator]:
                  btn_indicator.place_forget()

      #def show_indicator(self, btn_name):
      #      for btn_indicator in [self.btn_dashboard_indicator, self.btn_ventas_indicator, self.btn_clientes_indicator, self.btn_inventario_indicator, self.btn_reportes_indicator]:
      #            if btn_indicator["text"] == btn_name:
      #                  btn_indicator.place(x=10, y=180, width=185, height=40)
      #                  break
      
      def actualizar_fecha_hora(self):
            fecha_actual = datetime.datetime.now().strftime("%d / %m / %Y")
            hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

            self.label_fecha.config(text=fecha_actual)
            self.label_hora.config(text=hora_actual)

            if self.winfo_exists():
                  self.after(1000, self.actualizar_fecha_hora)