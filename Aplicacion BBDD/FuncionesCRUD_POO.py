import sqlite3
from tkinter import Text, messagebox

nombre_BBDD=""

def almacena(nom_BD):
    
    global nombre_BBDD
    nombre_BBDD=nom_BD
    
def leer(Id, *args):
    
    global nombre_BBDD
    
    mi_conexion=sqlite3.connect(nombre_BBDD)
    
    mi_cursor=mi_conexion.cursor()
    
    mi_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + Id)
    
    datos_usuario=mi_cursor.fetchall()

    pos_array=1
    
    for campo in args:
        for valor_campo in datos_usuario:
            
            if type(campo)==Text:
                campo.insert(1.0, valor_campo[pos_array])
            else:
                campo.set(valor_campo[pos_array])
            pos_array+=1
        
        

    mi_conexion.commit()

def crear(*args):
    
    mi_conexion=sqlite3.connect(nombre_BBDD)
    
    mi_cursor=mi_conexion.cursor()
    
    '''mi_cursor.execute("INSERT INTO DATOsUSUARIOS VALUES(NULL, '" + mi_nombre.get() +
                      "','" + mi_pass.get() +
                      "','" + mi_apellido.get() +
                      "','" + mi_direccion.get() +
                      "','" + textoComentario.get("1.0", END) + "')")'''
    
    #los_datos=mi_nombre.get(), mi_pass.get(), mi_apellido.get(), mi_direccion.get("1.0", END)
    
    los_datos_lista=[]
    
    for campo in args:
        
        if type(campo)==str:
            
            los_datos_lista.append(campo)
            
        else: 
            
            los_datos_lista.append(campo.get())
        
    los_datos=tuple(los_datos_lista)
    
    mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (los_datos))
    
    mi_conexion.commit()
    
    messagebox.showinfo("CRUD", "Registro insertado")
    
def actualizar(Id, *args):
    
    global nombre_BBDD
    
    mi_conexion=sqlite3.connect(nombre_BBDD)
    
    mi_cursor=mi_conexion.cursor()
    
    '''mi_cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='" + mi_nombre.get() + 
                      "', PASSWORD='" + mi_pass.get() + 
                      "', APELLIDO='" + mi_apellido.get() + 
                      "', DIRECCION='" + mi_direccion.get() + 
                      "', COMENTARIOS='" + textoComentario.get("1.0", END) + 
                      "'WHERE ID=" + mi_Id.get())'''
    
    # los_datos=mi_nombre.get(), mi_pass.get(), mi_apellido.get(), mi_direccion.get("1.0", END)
    
    los_datos_lista=[]
    
    for campo in args:
        
        if type(campo)==str:
            
            los_datos_lista.append(campo)
            
        else: 
            
            los_datos_lista.append(campo.get())
            
    los_datos=tuple(los_datos_lista)
    
    mi_cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID=" + 
                        Id, (los_datos))
    
    mi_conexion.commit()
    
    messagebox.showinfo("CRUD", "Registro actualizado")
    
def eliminar(Id):
    
    global nombre_BBDD
    
    mi_conexion=sqlite3.connect(nombre_BBDD)
    
    mi_cursor=mi_conexion.cursor()
    
    mi_cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + Id)
    
    mi_conexion.commit()
    
    messagebox.showinfo("CRUD", "Registro borrado")