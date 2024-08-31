diccionario = {#tambien sirven para iterar
    "nombre" : 'john',
    "apellido" : 'nieto',
    "edad" : 38
}
#nos devuelve un objeto dict_item 
claves = diccionario.keys()

#obteniendo un elemnto con get(si no encuentra nada el programa continua)
valor_de_vergacion = diccionario.get("vergacion")
print("que se dice colega?")

#eliminando todos los datos del diccionario
#diccionario.clear()
diccionario.pop("nombre")
print(claves)