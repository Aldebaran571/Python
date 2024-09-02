
frase = input("esto es un contador de palabras y el tiempo que tardaria en decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'comento {cantidad_de_palabras} palabras y tardo {cantidad_de_palabras/2} segundos en decirlas')
if cantidad_de_palabras < 120:
    print("demasiado texto, que aburrido")