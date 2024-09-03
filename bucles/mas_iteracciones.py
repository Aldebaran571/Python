
frutas = ["manzana", "banano", "pera", "ciruela", "coco", "uva"]
cadena = "##  HOLA JOHN  ##"
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
