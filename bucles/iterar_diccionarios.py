
diccionario = {
    "nombre" : "john",
    "apellido" : "nieto",
    "edad" : 38
    
}
#recorriendo el diccionario para obtener la clave
for key  in diccionario.items():
    key
    print(f'la clave es: {key}')
    
#recorriendo diccionario para obtener la claves y los valores
for datos  in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es: {value}')