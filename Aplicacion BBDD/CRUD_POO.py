from tkinter import *
from tkinter import messagebox
from Conexiones_POO import *
from FuncionesCRUD_POO import *

from tkinter import messagebox as MessageBox

class CRUD_POO(Frame):
    
    def __init__(self, raiz):
        
        # ------------------- Variables de Control --------------------
        
        self.mi_id=StringVar()
        self.mi_nombre=StringVar()
        self.mi_apellido=StringVar()
        self.mi_pass=StringVar()
        self.mi_direccion=StringVar()
        
        # ------------------- Barra de Menu ---------------------------
        
        self.barraMenu=Menu(root)
        raiz.config(menu=self.barraMenu)
        
        super().__init__(raiz, width=300, height=300)
        self.master=raiz
        self.pack()
        
        self.miFrameBotones=Frame(raiz)
        self.miFrameBotones.pack()
        
        self.crear_widgets()
        
        self.crear_barra_menu()
        
        self.ubicar_botones()
        
    def crear_barra_menu(self):

        self.bbddMenu=Menu(self.barraMenu, tearoff=0)
        self.bbddMenu.add_command(label="Conectar", command=conectarBBDD)
        self.bbddMenu.add_command(label="Salir", command=lambda: salirAplicacion(root))

        self.borrarMenu=Menu(self.barraMenu, tearoff=0)
        self.borrarMenu.add_command(label="Borrar", command=lambda: limpiarCampos(self.textoComentario, self.mi_id,
                                    self.mi_apellido, self.mi_nombre, self.mi_direccion, self.mi_pass))

        self.crudMenu=Menu(self.barraMenu, tearoff=0)
        self.crudMenu.add_command(label="Crear", command=lambda:crear(self.mi_nombre, self.mi_pass,
                                self.mi_apellido, self.mi_direccion, self.textoComentario.get(1.0, END)))
        
        self.crudMenu.add_command(label="Leer", command=lambda:leer(self.mi_id.get(), self.mi_nombre,
                                self.mi_pass, self.mi_apellido, self.mi_direccion, self.textoComentario))
        
        self.crudMenu.add_command(label="Actualizar", command=lambda:actualizar(self.mi_id.get(), self.mi_nombre,
                                self.mi_pass, self.mi_apellido, self.mi_direccion, self.textoComentario.get(1.0, END)))
        
        self.crudMenu.add_command(label="Borrar", command=lambda:eliminar(self.mi_id.get()))

        self.ayudaMenu=Menu(self.barraMenu, tearoff=0)
        self.ayudaMenu.add_command(label="Licencia", command=lambda:MessageBox.showinfo("Licencia", "BBDD tkinter 2.0"))
        self.ayudaMenu.add_command(label="Acerca de...", command=lambda:MessageBox.showinfo("Acerca de", "Macacos Industry\n"+ 
                                                                                            "Todos los bananos reservados"))

        self.barraMenu.add_cascade(label="BBDD", menu=self.bbddMenu)
        self.barraMenu.add_cascade(label="Borrar", menu=self.borrarMenu)
        self.barraMenu.add_cascade(label="CRUD", menu=self.crudMenu)
        self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)
        
        
        
    def crear_widgets(self):
        
        self.cuadroId=Entry(self, textvariable=self.mi_id)
        self.cuadroId.grid(row=0, column=1, padx=10, pady=10)

        self.cuadroNombre=Entry(self, textvariable=self.mi_nombre)
        self.cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
        self.cuadroNombre.config(fg="gray", justify="right")

        self.cuadroPass=Entry(self, textvariable=self.mi_pass)
        self.cuadroPass.grid(row=2, column=1, padx=10, pady=10)
        self.cuadroPass.config(show="*")

        self.cuadroApellido=Entry(self, textvariable=self.mi_apellido)
        self.cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

        self.cuadroDireccion=Entry(self, textvariable=self.mi_direccion)
        self.cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

        self.textoComentario=Text(self, width=16, height=5)
        self.textoComentario.grid(row=5, column=1, padx=10, pady=10)
        scrollVert=Scrollbar(self, command=self.textoComentario.yview)
        scrollVert.grid(row=5, column=2, sticky="nsew")
        self.textoComentario.config(yscrollcommand=scrollVert.set)
        
        # -------------------- Creacion de Labels ------------------------

        self.idLabel=Label(self, text="Id:")
        self.idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.nombreLabel=Label(self, text="Nombre:")
        self.nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.passLabel=Label(self, text="Password:")
        self.passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        self.apellidoLabel=Label(self, text="Apellido:")
        self.apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        self.direccionLabel=Label(self, text="Direccion:")
        self.direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

        self.comentariosLabel=Label(self, text="Comentario:")
        self.comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)
        
    def ubicar_botones(self):
        
        botonCrear=Button(self.miFrameBotones, text="Crear", command=lambda:crear(self.mi_nombre, self.mi_pass,
                                self.mi_apellido, self.mi_direccion, self.textoComentario.get(1.0, END)))
        botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        botonLeer=Button(self.miFrameBotones, text="Leer", command=lambda:leer(self.mi_id.get(), self.mi_nombre,
                                self.mi_pass, self.mi_apellido, self.mi_direccion, self.textoComentario))
        
        botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

        botonActualizar=Button(self.miFrameBotones, text="Actualizar", command=lambda:actualizar(self.mi_id.get(), self.mi_nombre,
                                self.mi_pass, self.mi_apellido, self.mi_direccion, self.textoComentario.get(1.0, END)))
        
        botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

        botonBorrar=Button(self.miFrameBotones, text="Borrar", command=lambda:eliminar(self.mi_id.get()))
        botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)
                
    
    
root=Tk()
app=CRUD_POO(root)
app.mainloop()