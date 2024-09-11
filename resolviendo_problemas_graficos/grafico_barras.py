import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("resolviendo_problemas_graficos\\ingresos_chimbos.csv")
#creando un grafico con los datos propuestos
sns.barplot(x="fuente", y="ingresos", data=df)

#obteniendo el total
total_ingresos=df["ingresos"].sum()

#mostrando el total
print(f'el total de los ingresos son: ${total_ingresos} COP')

#mostrando el grafico
plt.show()