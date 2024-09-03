#creando las listas
frutas = ["manzana", "banano", "pera", "ciruela", "coco", "uva"]
cadena = "##  HOLA JOHN  ##"
numeros = [2,4,8,16,32]
#evitando comer una pera con la sentencia continue 
for fruta in frutas:
    if fruta == 'pera':
        continue

#evitar comer mas fruta despues de ciruela, el else no se ejecuta despues del break
    print(f'me voy a comer una: {fruta}')
for fruta in frutas:
    if fruta == 'ciruela':
        break
    print(f'no puedo comer mas, quede en {fruta}')
else:
    print("terminado")

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una linea de codigo(duplicando numeros )
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)