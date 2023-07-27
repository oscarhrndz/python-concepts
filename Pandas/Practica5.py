# import pandas as pd

# momento=pd.to_datetime("27\02\2023")

# print(momento.month)

# print(momento.strftime("%d-%m-%Y"))

import pandas as pd

datos=pd.read_csv("C:\\Users\\oscar\\Desktop\\Curso_Python_PI\\excels_for_panda\\consumo_electrico_aleman.csv", sep=",")

datos_electricos=pd.DataFrame(datos)

datos_electricos.index=datos_electricos["Date"]

# datos_electricos=datos_electricos.loc["2014-03":"2016-02"]

datos_electricos=datos_electricos[datos_electricos["Date"]>"2016"]

print(type(datos_electricos.index[0]))
