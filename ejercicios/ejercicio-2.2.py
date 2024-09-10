"""creando una programa que nos ponga en pantalla los numeros primos hasta el numero que le indiquemos"""

#creando una funcion que nos devuelva los numeros primos entre 0 y el numero que elijamos
def es_primo(num):
    #verificamos que el numero ingresado no sea divisible por ningun numero entre 2 y el mismo numero
    for i in range(2,num-1):
        #si es divisible da como resultado False y termina el bucle
        if num%i==0: return False
        #si termina el bucle significa que no fue divisible entonces es primo
    return True

#creando una funcion que retome una lista con todos los numeros primos
def primos_hasta(num):
    
    #creando la lista
    primos = []
    for i in range(3, num+1):
        #verificamos que el valor sea primo
        resultado = es_primo(i)
        
        #en caso de que lo sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        
    #devolvemos la lista    
    return primos

#creamos el resultado  llamando a la funcion y lo mostramos
resultado = primos_hasta(98)
print(resultado) 