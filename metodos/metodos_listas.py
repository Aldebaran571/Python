#creando una lista con list
lista = list(["hola", "john", "nieto", 37, 554, 10])

#devuelve la cantidad dde elementos de la lista
cantidad_elementos = len(lista)  

#agregando elemento a la lista
agregando_con_append = lista.append("jajajaja")

#agregando con insert
lista.insert(2, "jelou, perra ")

#agregando varios elementos a la lista
lista.extend([True, 5050])

#eliminando un elemento de la lista por su indice, con -1 se elimina el ultimo elemento de la lista, -2 para eliminar el penultimo y asi sucesivaente
lista.pop(-1)

#removiendo un elemento de la lista por su valor.

print(lista)