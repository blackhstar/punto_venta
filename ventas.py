from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk

class Ventas(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.widgets()

        def widgets(self):
            label = Label(self, text="Ventas")
            label.pack()