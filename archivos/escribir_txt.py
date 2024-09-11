with open('archivos\\texto_prueba.txt','w', encoding="utf-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
    archivo.writelines(["hola compa como va la causa\n", "en el nombre de dios un trabajo por favor"])
    #agregando dos lineas con el comando writelines
    archivo.writelines(["hola en ek bisqyue de ka cghube\n ka chinbeta  se perdio\n", "en el nombre de dios"])