#cambiar el tipo de dato de una columna
import pandas as pd
df =pd.read_csv("archivos\\prueba2.csv")

#convertir los datos de una columna a string
df['edad']= df['edad'].astype(str)

#mostrar l tipo de dato del primer elemento  de la columna edad
print(type(df['edad'][0]))

#reemplazando  las palabras nieto por idoolo 
df['apellido'].replace("nieto", "idolo", inplace=True)

#eliminando  las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df =df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos\\prueba2.csv\\datos_limpios.csv")