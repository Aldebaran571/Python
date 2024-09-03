
animales = { "perro", "gato", "loro", "cocodrilo" }
numeros = {16,25,38,158 }
#recorriendo la conjunto de los animales
for animal in animales:
    print(f'ahora el animal es: {animal}')

#recorriendo la conjunto numeros y multiplicando por 10    
for numero in numeros:
    resultado = numero * 10
    print(f'el resultado multiplicado por 10 de los numeros es {resultado}')    
    
#iterando dos listas al mismo tiempo del mismo tamaño    
for numero, animal in zip(animales, numeros):
    print(f'recorriendolista 1{animal}')
    print(f'recorriendolista 2 {numero}')    



#forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num [1]
    print(f' el indice es {indice} y el valor es {valor}')

#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("termina el bucle")