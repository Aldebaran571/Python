#creando una funcion lambda para multiplicar por 2
numeros =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20]
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))

#creando una funcionm comun que diga si el numero es par o impar
"""def es_par(num):
    if (num%2==1):
        return True
#usando filter con una fucnion comun 
#numeros_pares = filter(es_par, numeros)"""

#aplicando lo mismo pero con la funcion lambda
numeros_pares = filter(lambda numero: numero%2 == 0,numeros)
print(list(numeros_pares))