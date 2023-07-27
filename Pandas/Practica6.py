import pandas as pd

datos=pd.read_csv("C:\\Users\\oscar\\Desktop\\Curso_Python_PI\\excels_for_panda\\consumo_electrico_aleman.csv", sep=",", encoding="")

# print(datos.info())

#print(datos.isna().sum())

# datos_ventas=pd.DataFrame(datos)

datos_ventas=datos.sample(3000)

print(datos_ventas.describe())