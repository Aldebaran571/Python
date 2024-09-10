#creando un modulo  y asignandole el valor  m_saludar
#import modulo_saludar as m_saludar

#desde ese modulo importamos 2 funciones
from modulo_saludar import saludar, saludar_raro


#creamos las variables con los saludos
saludo =saludar("john")
saludar_raro = saludar_raro ("fredy")

#mostramos los resultados
print(saludo)
print(saludar_raro)
