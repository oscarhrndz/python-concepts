from tkinter import messagebox
import sqlite3
from tkinter import simpledialog
from tkinter.constants import END
from FuncionesCRUD_POO import *

def conectarBBDD():
    
    nombre_BBDD=simpledialog.askstring("BBDD", "Introduce el nombre de la BBDD")
    
    almacena(nombre_BBDD)
    
    miConexion=sqlite3.connect(nombre_BBDD)
    
    miCursor=miConexion.cursor()
    
    try:
        miCursor.execute('''
                        
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR (70),
                COMENTARIOS VARCHAR (200)
            )
        ''')
    
        messagebox.showinfo("BBDD", "Base de Datos creada con exito")
    
    except:
        
        messagebox.showwarning("Cuidao", "La Base de Datos ya existe")
        
def salirAplicacion(raiz):
        
    valor_salir=messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")
    
    if valor_salir=="yes":
        raiz.destroy()
        
# def limpiarCampos(campo1, campo2, campo3, campo4, campo5):
#     campo1.set("")
#     campo2.set("")
#     campo3.set("")
#     campo4.set("")
#     campo5.set("")
    
def limpiarCampos(*args):
    
    for campo in args:
        
        campo.delete(1.0, END)
        
    else:
        
        campo.set("")
        
    
    # cuadroTexto.delete(1.0, END)