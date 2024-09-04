def frase(nombre, apellido, adjetivo):
    return f'hola {nombre}{apellido} ud lo va a conseguir{adjetivo}'
frase_resultante = frase(adjetivo=" mostro", apellido="nieto ", nombre="john ")

#creando la misma funcion con un parametro  opcional y un valor por defecto
def frase (nombre, apellido, adjetivo="abeja"):#aqui se crea el parametro "abeja " y este es opcional 
    return f'hola {nombre } {apellido}, ud es una {adjetivo}'
frase_resultante = frase("john ", "nieto ","ud es una mostro" )#aqui se cambia el parametro y continua con el parametro que coplocamos omitiendo el opcional 
print(frase_resultante)