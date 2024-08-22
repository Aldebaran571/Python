#creando una lista(modificable)
lista = ["john f ", "martinez ", True, 1.80]

#creando una tupla(inmodificable)
tupla = ("john f ", "martinez ", True, 1.80)
print(lista[3])

#valido
lista[3]= "pro"
print(lista[3])
#no valido
#tupla[3] = "pro"
#creadno un conjunto (set)  en los conjuntos no se permiten datos duplicados, datos sin orden especifico
conjunto = {"john f ", "martinez ", True, 1.80}
print(conjunto)

