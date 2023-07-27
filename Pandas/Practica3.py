import pandas as pd

import requests

import numpy as np

datos_covid=requests.get("https://api.covid19api.com/summary").json()

covid19=pd.DataFrame.from_dict(datos_covid["Countries"])

covid19.ID=covid19["Country"]

#print(covid19.info())

#print(covid19.TotalDeaths.describe())

# print(covid19.describe(include=[object]))

# print(covid19.describe(include=[np.number], percentiles=[.1,.9]))

# print(covid19.head())
# print(covid19.head(9))

# print(covid19.tail())
# print(covid19.tail(8))

# print(covid19.shape)

# print(covid19.columns)

# print(covid19["Country"])

# print(covid19.Country)

# print(list(covid19.Country))

# covid19.ID=covid19["Country"]
# print(covid19)

# covid19.ID=covid19["Country"]
# covid19.drop(["ID"], axis=1, inplace=True)
# print(covid19)

# covid19filtrado=list(covid19.columns)
# print(covid19filtrado)

# covid19filtrado=list(covid19.columns)
# covid19filtrado.remove("ID")
# print(covid19filtrado)

# covid19filtrado=list(covid19.columns)
# covid19filtrado.remove("ID")
# covid=covid19[covid19filtrado]
# print(covid19)

covid19filtrado=list(covid19.columns)
covid19filtrado.remove("ID")
covid=covid19[covid19filtrado]
print(covid19.mean())
print(covid19.std())

