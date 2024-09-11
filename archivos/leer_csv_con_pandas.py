import pandas as pd

#usando la funcion read_csv para leer el archivo  CSV
df= pd.read_csv("archivos\\prueba2.csv")
df2 = pd.read_csv("archivos\\prueba2.csv")

#obteniendo los dats de la columna nombre
nombres =df["nombre"]

#ordenando el dataframe por la edad
ascendente = df.sort_values("edad")

#ordenando de forma descendente
df_descendente = df.sort_values("edad", ascending=False)


#concatenando los dos dataframes
df_concatenado = pd.concat([df, df2])


#accediendo a la primera fila con head()
primera_fila = df.head(2)


#accediendo a la ultima fila con tail()
ultima_fila =df.tail(1)

#accedendo a la cantidad de filas y de columnas con shape
filas_columnas_totales = df.shape

#obteniendo las estadoisticas  del dataframe con describe

df_info = df.describe()

#accediendo  a un elemento especifico del dataframe con loc. accediendo a la edad
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a elemeto especifico del dataframe con iloc, accediendo a la edad
elemento_especifico_iloc= df.iloc[2,2]

#accediendo a la fila  con edad mayor de 30
mayor_30 = df.loc[df["edad"]<30,:]


print(mayor_30)

