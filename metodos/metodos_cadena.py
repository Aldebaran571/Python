cadena1 = "mereuetengue"
cadena2 = "MODO BEstiA"
#CONVIERTE A MAYUSCULAS
mayus = cadena1.upper()#dato.nombredelmetodo()

#CONVIERTE A MINUSCULAS
minus = cadena2.lower()
print(mayus, minus)

#cambia la primera letra a mayuscula
primer_letra_mayus = cadena1.capitalize()

#busca una cadena en otra cadena, si no hay coincidencias pone -1 , recordar que distingue mayusculas de minusculas
busqueda_find = cadena1.find("e")

#busca una cadena dentro de otra cadena, si no hay coincidencias, arroja error de execpción
busqueda_index = cadena1.index("e")


#si es numerico devuelve True caso contrario devuelve False
es_numerico = cadena1.isnumeric()


#si es alfanumerico y no hay espacios ni otros caracteres especiales, determina si hay letras
es_alfa = cadena1.isalpha()

#busca una cadena en otra cadena, busca la cantidad de letras que hay en el texto de la variable
contar_coincidencia = cadena1.count("e")

#la funion len nos cuenta la cantidad de caracteres en una cadena
contar_caracteres = len(cadena1)


#verifica si la cadena empieza con el caracter ingresado, si es verdad, devuelve True 
empieza_con = cadena1.startswith("m")

#verifica si la cadena termina con  el caracter ingresado, si es verdad devuelve true
termina_con = cadena1.endswith("g")

print(termina_con)