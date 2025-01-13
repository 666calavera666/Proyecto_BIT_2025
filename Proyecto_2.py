from matplotlib import pyplot as plt
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

path = os.getcwd()

#Importat Data...

fallecidos = pd.read_csv("Fallecidos_COVID_en_Colombia.csv", sep=",")
fallecidos.head()
#print(fallecidos.columns)

fig, ax = plt.subplots(figsize=(10, 10))

frecuencia_municipios = fallecidos['Nombre municipio'].value_counts().head(10)

ax.bar(frecuencia_municipios.index, frecuencia_municipios.values)

ax.set_xlabel("Municipios")
ax.set_ylabel("Frecuencia de Fallecidos")
ax.set_title("Frecuencia de Fallecidos por Municipio (Top 10)")

plt.xticks(rotation=90)

plt.show() #Diagrama de barras con frecuencia de fallecidos por municipio

