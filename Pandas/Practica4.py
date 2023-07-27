import pandas as pd

datos=pd.read_csv("C:\\Users\\oscar\\Desktop\\Curso_Python_PI\\excels_for_panda\\titanic.csv", sep=",")

datos_titanic=pd.DataFrame(datos)

datos_titanic["Supervivientes"]=datos_titanic["Survived"].map({0:"Fallecido", 1:"Superviviente"})

# print(datos_titanic["Supervivientes"].value_counts())

'''def en_mayusculas(x):
    
    # return x.upper()'''

# datos_titanic["Nombres Pasajeros"]=datos_titanic["Name"].map()

# datos_titanic=datos_titanic[["Name", "Supervivientes"]].applymap(en_mayusculas)

    
en_mayusculas=lambda x: x.upper() if type(x)==str else x

datos_titanic["Nombres Pasajeros"]=datos_titanic["Name"].map(en_mayusculas)

datos_titanic=datos_titanic.applymap(en_mayusculas)



print(datos_titanic)