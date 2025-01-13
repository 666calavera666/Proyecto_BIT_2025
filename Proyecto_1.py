import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")

path = os.getcwd()

file_names=[x for x in os.listdir() if 'COVID' in x]
print(file_names)

#Data Extraction ---

dataframes = {}

for file_name in file_names:
    full_path = f"{path}/{file_name}"
    print(f"Data Frame: {file_name}")
    try:
        df = pd.read_csv(full_path, sep=",", encoding='utf-8')
        dataframes[file_name.split('.')[0]] = df
    except Exception as e:
        print(f"Error al procesar {file_name}: {e}")
    print(df)
    print("-" * 40)

#Variables de Interes ---

first_key = list(dataframes.keys())[0]
vacunados = dataframes[first_key]
Vacunados_Variable = "Nom_Territorio" #interesa saber los territorios con mas aplicacion de vacunas

if Vacunados_Variable in vacunados.columns:
    print(f"Conteo de valores para '{Vacunados_Variable}' en Vacunados:")
    print(vacunados[Vacunados_Variable].value_counts())
else:
    print("No se encentra la variable")

second_key = list(dataframes.keys())[1]
fallecidos = dataframes[second_key]
Fallecidos_Variable = "Nombre departamento" #interesa saber los territorios con mas fallecidos

if Fallecidos_Variable in fallecidos.columns:
    print(f"Conteo de valores para '{Fallecidos_Variable}'en Fallecidos:")
    print(fallecidos[Fallecidos_Variable].value_counts())
else:
    print("No se encentra la variable")

third_key = list(dataframes.keys())[1]
sexo_fallecidos = dataframes[second_key]
Sexo_Fallecidos = "Sexo" #interesa el sexo de los fallecidos

if Sexo_Fallecidos in sexo_fallecidos.columns:
    print(f"Conteo de valores para '{Sexo_Fallecidos}'en Fallecidos:")
    print(sexo_fallecidos[Sexo_Fallecidos].value_counts())
else:
    print("No se encentra la variable")
