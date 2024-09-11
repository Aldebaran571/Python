import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("resolviendo_problemas_graficos\\gas.csv")
#creando un grafico con los datos propuestos
sns.lineplot(x="fecha", y="gases", data=df)

#creanmdo un puntop en la grafica donde esta el indicador mas alto
plt.plot("01-10", 33, "o")

#mostrando el grafico
plt.show()
