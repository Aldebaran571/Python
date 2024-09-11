import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("resolviendo_problemas_graficos\\dispersion.csv")
#creando un grafico con los datos propuestos
sns.scatterplot(x="tiempo", y="dinero", data=df)



#mostrando el grafico
plt.show()