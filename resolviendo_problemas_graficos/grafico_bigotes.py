import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("resolviendo_problemas_graficos\\bigotes.csv")
#creando un grafico con los datos propuestos
sns.boxenplot(x="categoria", y="valor", data=df)


#mostrando el grafico
plt.show()