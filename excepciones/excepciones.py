#creando funcion que sume numeros
def sumar_dos ():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("digite primer numero: ")
        b = input("digite segundo numero: ")
        #intentandoo convertirlos  a enteros y sumarlos
        try:
            resultado =int (a) + int(b)
        #si lanza una excepcion pedirle que ingresde los datos
        except:
            print("introduzca un numero , aguevado... ¬¬")
        #si todo sale bien termina el bucle
        else:
            break    
    return resultado
#mostrando el resultado
print(f'la suma de los numeros es: ', sumar_dos())
            
    