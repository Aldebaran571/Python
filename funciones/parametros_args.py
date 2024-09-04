#forma no optima de sumar valores
"""def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados =numeros_sumados + numero
    return numeros_sumados
resultado = suma([5,3,9,20,10,3])"""
#utilizando el operador * como argumento (args) parametro args
def suma (nombre, *numeros):
    return f'{nombre}, la suma de tus numeros es: {sum (numeros) }'
resultado = suma ("john", 5,3,9,20,10,3)

print(resultado)