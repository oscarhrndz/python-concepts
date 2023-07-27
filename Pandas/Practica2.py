import pandas as pd

#aguacates=pd.read_excel("C:\\Users\\oscar\\Desktop\\Curso_Python_PI\\excels_for_panda\\Aguacate producción.xlsx")
#aguacates1=pd.read_csv("C:\\Users\\oscar\\Desktop\\Curso_Python_PI\\excels_for_panda\\aguacate.csv")
aguacates2=pd.read_csv("C:\\Users\\oscar\\Desktop\\Curso_Python_PI\\excels_for_panda\\aguacate2.csv", sep=";")

datos_aguacates=pd.DataFrame(aguacates2)

# print(datos_aguacates)

# print(datos_aguacates["Year"].value_counts())

print(datos_aguacates.columns)
print(datos_aguacates[" County"].value_counts())

datos_aguacates.rename(columns={" County":"Ciudades"}, inplace=True)
print(datos_aguacates[" County"].value_counts())

