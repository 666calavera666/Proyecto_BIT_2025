from matplotlib import pyplot as plt
import pandas as pd
import os
import warnings
import seaborn as sns
import plotly.express as px
from plotly.offline import plot

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

vacunados = pd.read_csv("Asignacion_vacuna_contra_COVID-19.csv", sep=",")
#vacunas_lab = vacunados['Laboratorio_Vacuna'].value_counts()
#print(vacunas_lab)
"""""
plt.figure(figsize=(8, 8))  
plt.pie(
    vacunas_lab, 
    labels=vacunas_lab.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    textprops={'fontsize': 10}
)
plt.title("Distribución de Vacunas Aplicadas por Laboratorio")
plt.axis('equal')  
plt.show() # Pie Chart porcentaje de vacunas apliacadas por laboratorio de vacuna
"""
sns.histplot(data=vacunados,x="Laboratorio_Vacuna", bins=10)
plt.title("Frecuencia de Vacunas Aplicadas")
plt.xlabel("Laboratorio Vacuna")
plt.ylabel("Frecuencia")
plt.show() # Histograma "Frecuncia de Vacunas Aplicadas" con Seaborn

data_plotly = pd.DataFrame({
    'Municipio': frecuencia_municipios.index,
    'Frecuencia': frecuencia_municipios.values
})
fig = px.bar(data_plotly, 
             x='Municipio', 
             y='Frecuencia', 
             title='Frecuencia de Fallecidos por Municipio (Top 10)',
             labels={'Frecuencia': 'Número de Fallecidos', 'Municipio': 'Nombre Municipio'})
fig.update_layout(xaxis_title="Municipios",
                  yaxis_title="Frecuencia de Fallecidos",
                  xaxis_tickangle=45)
plot(fig)
