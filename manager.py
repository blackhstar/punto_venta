from tkinter import *
from tkinter import ttk, messagebox
from container import Container
from login import Login , Registro

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        self.title("sistema punto de venta")
        self.resizable(False,False)
        self.geometry("1100x650+120+50")

        self.container = Frame(self , bg="#dcdcdc")
        self.container.pack(fill=BOTH, expand=True)

        self.frames = {}
        for i in (Login, Registro, Container):
            frame = i(self.container , self)
            self.frames[i] = frame

        self.show_frame(Container)

    def show_frame(self , frame_class, user=None):
        frame = self.frames[frame_class]

        if user is not None:
            frame.set_user(user)

        frame.tkraise()

def main():
    app = Manager()
    app.mainloop()

    if __name__ == "__main__":
        main()
