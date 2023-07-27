from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()


# --------------------- Conexion/creacion BBDD -----------------------------

def conectarBBDD():
    
    miConexion=sqlite3.connect("NegocioUsuarios")
    
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
        
def salirAplicacion():
        
    valor_salir=messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")
    
    if valor_salir=="yes":
        root.destroy()
        
def limpiarCampos():
    
    mi_Id.set("")
    mi_nombre.set("")
    mi_apellido.set("")
    mi_direccion.set("")
    mi_pass.set("")
    textoComentario.delete(1.0, END)
    
def crear():
    
    mi_conexion=sqlite3.connect("NegocioUsuarios")
    
    mi_cursor=mi_conexion.cursor()
    
    '''mi_cursor.execute("INSERT INTO DATOsUSUARIOS VALUES(NULL, '" + mi_nombre.get() +
                      "','" + mi_pass.get() +
                      "','" + mi_apellido.get() +
                      "','" + mi_direccion.get() +
                      "','" + textoComentario.get("1.0", END) + "')")'''
    
    los_datos=mi_nombre.get(), mi_pass.get(), mi_apellido.get(), mi_direccion.get(), textoComentario.get("1.0", END)
    
    mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (los_datos))
    
    mi_conexion.commit()
    
    messagebox.showinfo("CRUD", "Registro insertado")
    
def leer():
    
    mi_conexion=sqlite3.connect("NegocioUsuarios")
    
    mi_cursor=mi_conexion.cursor()
    
    mi_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + mi_Id.get())
    
    datos_usuario=mi_cursor.fetchall()
    
    for usuario in datos_usuario:
        
        mi_Id.set(usuario[0])
        mi_nombre.set(usuario[1])
        mi_pass.set(usuario[2])
        mi_apellido.set(usuario[3])
        mi_direccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])
        
    mi_conexion.commit()
    
def actualizar():
    
    mi_conexion=sqlite3.connect("NegocioUsuarios")
    
    mi_cursor=mi_conexion.cursor()
    
    '''mi_cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='" + mi_nombre.get() + 
                      "', PASSWORD='" + mi_pass.get() + 
                      "', APELLIDO='" + mi_apellido.get() + 
                      "', DIRECCION='" + mi_direccion.get() + 
                      "', COMENTARIOS='" + textoComentario.get("1.0", END) + 
                      "'WHERE ID=" + mi_Id.get())'''
    
    los_datos=mi_nombre.get(), mi_pass.get(), mi_apellido.get(), mi_direccion.get("1.0", END)
    
    mi_cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION?, COMENTARIOS=? WHERE ID=" +
                      mi_Id.get(), (los_datos))
    
    mi_conexion.commit()
    
    messagebox.showinfo("CRUD", "Registro actualizado")
    
def eliminar():
    
    mi_conexion=sqlite3.connect("NegocioUsuarios")
    
    mi_cursor=mi_conexion.cursor()
    
    mi_cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + mi_Id.get())
    
    mi_conexion.commit()
    
    messagebox.showinfo("CRUD", "Registro borrado")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


# ----------------- Variables de Control -----------------------

mi_Id=StringVar()
mi_nombre=StringVar()
mi_apellido=StringVar()
mi_pass=StringVar()
mi_direccion=StringVar()

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conectarBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


# ---------------------------- Construccion de Campos grid -------------------------------

miFrame=Frame(root)
miFrame.pack()

cuadroId=Entry(miFrame, textvariable=mi_Id)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=mi_nombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="gray", justify="right")

cuadroPass=Entry(miFrame, textvariable=mi_pass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=mi_apellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=mi_direccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)


# -------------------- Creacion de Labels ------------------------

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentario:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)


# -------------------------- Colocacion Botones ------------------------

miFrameBotones=Frame(root)
miFrameBotones.pack()

botonCrear=Button(miFrameBotones, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrameBotones, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrameBotones, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrameBotones, text="Borrar", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)








root.mainloop()