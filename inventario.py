from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk 
import sqlite3

class Inventario(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            self.registros_por_pagina = 18 
            self.pagina_actual  = 0
            self.total_registros = 0
            self.widgets()
            self.mostrar()

        def widgets(self):

            opciones = LabelFrame(self, text="Opciones" , bg="#dddddd", font=("sans", 14,"bold"))
            opciones.place(x=20, y=500, width=260, height=90)

            boton_agregar = tk.Button(opciones, text="Registrar",  bg="#ffffff", font=("sans", 10,"bold") , command=self.ventana_agregar)
            boton_agregar.place(x=10, y=10, width=70, height=40)

            boton_editar = tk.Button(opciones, text="Editar",  bg="#ffffff", font=("sans", 10,"bold"), command=self.editar_producto)
            boton_editar.place(x=90, y=10, width=70, height=40)

            boton_eliminar = tk.Button(opciones, text="Eliminar",  bg="#ffffff", font=("sans", 10,"bold") , command=self.eliminar_producto)
            boton_eliminar.place(x=170, y=10, width=70, height=40)

            frame_buscar = Frame(self, bg="#dcdcdc")
            frame_buscar.place(x=0, y=0, width=400, height=50)

            entry_producto = ttk.Entry(frame_buscar ,font="sans 14 bold")
            entry_producto.place(x=20 , y=10 ,width=200 , height=40)

            buscar = tk.Button(frame_buscar , text="Buscar" , font="sans 10 bold", bg="#ffffff")
            buscar.place(x=230, y=10, width=100, height=40)

            label_buscar = Label(frame_buscar, text="Buscar", bg="#dcdcdc", font=("sans", 10,"bold"))
            label_buscar.place(x=10, y=10, width=70, height=40)

            entry_buscar = Entry(frame_buscar, bg="#ffffff", font=("sans", 10,"bold"))

            treeframe = Frame(self, bg="#ffffff")
            treeframe.place(x=20, y=70, width=850, height=420)

            scroll_y = ttk.Scrollbar(treeframe, orient=VERTICAL)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x = ttk.Scrollbar(treeframe, orient=HORIZONTAL)
            scroll_x.pack(side=BOTTOM, fill=X)

            self.tree = ttk.Treeview(treeframe, columns=("ID", "Producto", "Precio", "Cantidad" , "Costo"), show="headings", selectmode="browse", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set, height=40)
            self.tree.pack(fill=BOTH, expand=True)

            scroll_y.config(command=self.tree.yview)
            scroll_x.config(command=self.tree.xview)

            self.tree.heading("ID", text="ID", anchor=CENTER)
            self.tree.heading("Producto", text="Producto", anchor=CENTER)
            self.tree.heading("Precio", text="Precio", anchor=CENTER)
            self.tree.heading("Cantidad", text="Cantidad", anchor=CENTER)
            self.tree.heading("Costo", text="Costo", anchor=CENTER)

            self.tree.column("ID", width=50)
            self.tree.column("Producto", width=250)
            self.tree.column("Precio", width=100)
            self.tree.column("Cantidad", width=100)
            self.tree.column("Costo", width=100)

        def ventana_agregar(self):
            self.ventana = tk.Toplevel(self)
            self.ventana.title("Registrar producto")
            self.ventana.geometry("450x570+450+70")
            self.ventana.config(bg="#dcdcdc")
            self.ventana.resizable(False, False)
            self.ventana.transient(self.master)
            self.ventana.grab_set()
            self.ventana.focus_set()
            self.ventana.lift()

            labelframe = LabelFrame(self.ventana , text="Registrar producto" , font="sans 22 bold" , bg="#dcdcdc")
            labelframe.place(x=25 ,   y=25 , width=400 , height=520)

            labelnombre = Label(labelframe , text="Nombre", bg="#dcdcdc" , font="sans 14 bold")
            labelnombre.place(x=10 , y=20)
            self.nombre = ttk.Entry(labelframe , font="sans 14 bold")
            self.nombre.place(x=140, y=20, width=240 , height=40)

            labelPrecio = Label(labelframe , text="Precio", bg="#dcdcdc" , font="sans 14 bold")
            labelPrecio.place(x=10 , y=80)
            self.precio = ttk.Entry(labelframe , font="sans 14 bold")
            self.precio.place(x=140, y=80, width=240 , height=40)

            labelcosto = Label(labelframe , text="Costo", bg="#dcdcdc" , font="sans 14 bold")
            labelcosto.place(x=10 , y=140)
            self.costo = ttk.Entry(labelframe , font="sans 14 bold")
            self.costo.place(x=140, y=140, width=240 , height=40)

            labelstock = Label(labelframe , text="Stock", bg="#dcdcdc" , font="sans 14 bold")
            labelstock.place(x=10 , y=200)
            self.stock = ttk.Entry(labelframe , font="sans 14 bold")
            self.stock.place(x=140, y=200, width=240 , height=40)

            boton_agregar = Button(labelframe , text="Ingresar" , font="sans 14 bold" , bg="#dddddd", command=self.registrar_producto)
            boton_agregar.place(x=80, y=380 , width=240 , height=40)
             
        def registrar_producto(self):
            nombre = self.nombre.get()
            precio = self.precio.get()
            costo = self.costo.get()
            stock = self.stock.get()

            result = self.tree.get_children()
            for i in result:
                 self.tree.delete(i)

            try:
                precio = float(precio)
                costo = float(costo)
                stock = int(stock)
            except:
                 messagebox.showerror("Error" , "Precio , Costo y Stock deben ser numeros validos")
                 return

            if all([nombre]) and precio >= 0 and costo >= 0 and stock >= 0:
                try:
                    conn = sqlite3.connect("DBPOS.db")
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO DBPRODUCTO (PRODNAME , PRODCOSTO , PRODPRECIO , PRDSTOCK ) VALUES(  ? ,? ,? ,? )",
                    (nombre, costo ,precio , stock) )
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(title="Exito" , message="Producto agregado al inventario correctamente")

                    self.ventana.destroy
                    self.motrar()
                except Exception as e:
                    messagebox.showerror("Error" , "Error al registrar el producto {}".format(e))
            else:
                messagebox.showwarning(title="Error" , message="Rellene todos los campos correctamente")

                self.nombre.delete( 0 , tk.END)
                self.precio.delete( 0 , tk.END)
                self.costo.delete( 0 , tk.END)
                self.stock.delete( 0 , tk.END)

        def editar_producto(self):
            seleccion = self.tree.selection();
            if not seleccion:
                messagebox.showwarning("Editar producto" , "Seleccione un producto para editar.")
                return

            item_id = self.tree.item(seleccion)["values"][0]

            try:
                with sqlite3.connect("DBPOS.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT PRODNAME, PRODPRECIO , PRODCOSTO, PRDSTOCK FROM DBPRODUCTO WHERE id = ?" , (item_id,))
                    producto = cursor.fetchone()
                
                if not producto:
                    messagebox.showerror("Error" , "No se pudo obtener los datos del producto")
                    return
            except sqlite3.Error as e:
                messagebox.showerror("Error" , f"Error al consultar la base de datos: {e} , {item_id}")
                return
                
            nombre, precio, costo, stock = producto

            self.editar = tk.Toplevel(self)
            self.editar.title("Editar producto")
            self.editar.geometry("450x570+450+70")
            self.editar.config(bg="#dcdcdc")
            self.editar.resizable(False, False)
            self.editar.transient(self.master)
            self.editar.grab_set()
            self.editar.focus_set()
            self.editar.lift()

            labelframe1 = LabelFrame(self.editar , text="Editar producto" , font="sans 22 bold" , bg="#dcdcdc")
            labelframe1.place(x=25 ,   y=25 , width=400 , height=520)

            labelnombre = Label(labelframe1 , text="Nombre", bg="#dcdcdc" , font="sans 14 bold")
            labelnombre.place(x=10 , y=20)
            entry_nombre = ttk.Entry(labelframe1 , font="sans 14 bold")
            entry_nombre.place(x=140, y=20, width=240 , height=40)
            entry_nombre.insert( 0 , nombre)

            labelPrecio = Label(labelframe1 , text="Precio", bg="#dcdcdc" , font="sans 14 bold")
            labelPrecio.place(x=10 , y=80)
            entry_precio = ttk.Entry(labelframe1 , font="sans 14 bold")
            entry_precio.place(x=140, y=80, width=240 , height=40)
            entry_precio.insert( 0 , precio)

            labelcosto = Label(labelframe1 , text="Costo", bg="#dcdcdc" , font="sans 14 bold")
            labelcosto.place(x=10 , y=140)
            entry_costo = ttk.Entry(labelframe1 , font="sans 14 bold")
            entry_costo.place(x=140, y=140, width=240 , height=40)
            entry_costo.insert( 0 , costo)

            labelstock = Label(labelframe1 , text="Stock", bg="#dcdcdc" , font="sans 14 bold")
            labelstock.place(x=10 , y=200)
            entry_stock = ttk.Entry(labelframe1 , font="sans 14 bold")
            entry_stock.place(x=140, y=200, width=240 , height=40)
            entry_stock.insert( 0 , stock)

            def guardar_cambios():

                nombre = entry_nombre.get()
                precio = entry_precio.get()
                costo = entry_costo.get()
                stock = entry_stock.get()

                if not (nombre and precio and costo and stock):
                    messagebox.showerror("Error" , "Todos los campos deben ser completados")
                    return
                
                try:
                    with sqlite3.connect("DBPOS.db") as conn:
                        cursor = conn.cursor()
                        cursor.execute("UPDATE DBPRODUCTO SET PRODNAME = ?, PRODPRECIO = ?, PRODCOSTO = ?, PRDSTOCK = ? WHERE id = ? " , 
                                    (nombre, precio, costo, stock , item_id) )
                        conn.commit()
                        #conn.close()

                        messagebox.showinfo("Exito" , "Producto editado correctametne.")
                        self.editar.destroy()
                        self.mostrar()
                except sqlite3.Error as e:
                    messagebox.showerror("Error" , f"No se pudo guardar los cambios: {e}")

 
            boton_guardar = Button(labelframe1 , text="Guardar cambios" , font="sans 14 bold" , bg="#dddddd", command=guardar_cambios)
            boton_guardar.place(x=140, y=380 , width=240 , height=40)

        def eliminar_producto(self):
            item = self.tree.selection()

            if not item:
                messagebox.showwarning("Editar producto" , "Seleccione un producto para editar.")
                return
            
            producto_id = self.tree.item(item)["values"][0]

            confirmacion = messagebox.askyesno("Confirmar eliminacion" , f"Estas seguro de que deseas eliminar el producto con id {producto_id}?")

            if confirmacion:
                try:
                    with sqlite3.connect("DBPOS.db") as conn:
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM DBPRODUCTO WHERE id = ? " , ( producto_id, ))
                        conn.commit()

                        self.tree.delete(item)

                        messagebox.showinfo("Eliminacion exitosa" , "Producto eliminado correctamente")
                except sqlite3.Error as e:
                    messagebox.showerror("Error" , f"No se pudo eliminar el producto: {e}")
                    self.mostrar()

        def mostrar(self):
            try:

                conn = sqlite3.connect("DBPOS.db")
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM DBPRODUCTO")
                self.total_registros = cursor.fetchone()[0]

                cursor.execute("SELECT id,PRODNAME, PRODPRECIO , PRODCOSTO, PRDSTOCK FROM DBPRODUCTO LIMIT ? OFFSET ? " , (self.registros_por_pagina , self.pagina_actual * self.registros_por_pagina))
                rows = cursor.fetchall()

                self.tree.delete(*self.tree.get_children())

                for row in rows: 
                    precio_formateado = f"{row[3]:,.2f}" if row[3] is not None else "0.00"
                    costo_formateado = f"{row[4]:,.2f}" if row[3] is not None else "0.00"

                    row_formateado = list(row)
                    row_formateado[3] = precio_formateado
                    row_formateado[4] = costo_formateado

                    self.tree.insert("" , "end", values=row_formateado)

                conn.close()
                self.botones_actualizar_navegacion()
            except sqlite3.Error as e:
                messagebox.showerror("Error" , f"No se pudo cargar los registros: {e} ")

        def botones_actualizar_navegacion(self):
            self.total_paginas = ( self.total_registros * self.registros_por_pagina - 1 ) //self.registros_por_pagina

            for widget in self.winfo_children():
                if isinstance(widget , tk.Button ):
                    widget.destroy()

            imagen_anterior = Image.open("src/img/izquierda.png")
            imagen_anterior = imagen_anterior.resize((20, 20), resample=Image.Resampling.LANCZOS)
            imagen_anterior_tk = ImageTk.PhotoImage( imagen_anterior ) 

            imagen_siguiente = Image.open("src/img/derecha.png")
            imagen_siguiente = imagen_siguiente.resize((20, 20), resample=Image.Resampling.LANCZOS)
            imagen_siguiente_tk = ImageTk.PhotoImage( imagen_siguiente ) 

            if self.pagina_actual > 0:
                btn_anterior = tk.Button(self, command=self.pagina_anterior , image=imagen_anterior_tk , compound=LEFT, background="#ffffff")
                btn_anterior.imahe = imagen_anterior_tk
                btn_anterior.place( x=700 , y=10 )
            else:
                btn_anterior = tk.Button(self, command=self.pagina_anterior , image=imagen_anterior_tk , compound=LEFT, background="#ffffff", state=DISABLED)
                btn_anterior.imahe = imagen_anterior_tk
                btn_anterior.place( x=700 , y=10 )  

            if self.pagina_actual < self.total_paginas - 1:
                btn_siguiente = tk.Button(self, command=self.pagina_siguiente , image=imagen_siguiente_tk , compound=LEFT, background="#ffffff")
                btn_siguiente.imahe = imagen_siguiente_tk
                btn_siguiente.place( x=730 , y=10 )
            else:
                btn_siguiente = tk.Button(self, command=self.pagina_siguiente , image=imagen_siguiente_tk , compound=LEFT, background="#ffffff", state=DISABLED)
                btn_siguiente.imahe = imagen_siguiente_tk
                btn_siguiente.place( x=730 , y=10 )  

            label_pagina = tk.Label(self, text=f"Pagina {self.pagina_actual + 1 } de {self.total_paginas} " , font="sans 12 bold" , bg="#dcdcdc")
            label_pagina.place(x=770 , y= 10)

        def pagina_anterior(self):
            if self.pagina_actual > 0:
                self.pagina_actual -= 1
            self.mostrar()
        
        def pagina_siguiente(self):
            if (self.pagina_actual + 1 ) * self.registros_por_pagina < self.total_registros:
                self.pagina_actual += 1
            self.mostrar()