#usando "open" para abrir un archivo con codificacion universal 
archivo = open("archivos\\texto_prueba.txt", encoding="UTF-8")

#leer el archivo completo
#archivo =archivo.read()

#leer una sola linea
linea =archivo.readline()

#leer linea por linea
#lineas= archivo.readline()

#cerrar archivo
archivo.close()


print(archivo)