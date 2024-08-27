#creando una lista con list
lista = list([ 37, 554, 10, False])

#devuelve la cantidad dde elementos de la lista
cantidad_elementos = len(lista)  

#agregando elemento a la lista
agregando_con_append = lista.append(19854)

#agregando con insert
lista.insert(2, 7)

#agregando varios elementos a la lista
lista.extend([True, 5050])

#eliminando un elemento de la lista por su indice, con -1 se elimina el ultimo elemento de la lista, -2 para eliminar el penultimo y asi sucesivaente
lista.pop(-1)

#removiendo un elemento de la lista por su valor.
#lista.remove("hola")

#eliminando todos los elementos de la lista
#lista.clear()
#ordenando la lista, si se usa con el parametro reverse=True los ordena al reves
lista.sort()#(reverse=True)

#invirtiendo los parametros de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(37)


print(elemento_encontrado)