#creando diccionarios con dict()
diccionario= dict (nombre ="john", apellido= "nieto")

#las listas no pueden ser claves y usamos frozenset para metrer conjuntos
diccionario = {frozenset(["john", "nieto"]):"okeypelisgha" }

#creando diccionario con fromkeys() con dos parametros cambiando el valor por defecto a  "no se"
diccionario = dict.fromkeys([ "nombre", "apellido" ], "no se")

#creando diccionario con fromkeys() valor por defecto none
diccionario = dict.fromkeys(["nombre", "apellido"])

print(diccionario)