#creando un conjutno con set
conjunto = set(["dato1"])


#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

#teoria de conjunto

#verificando si es un subconjunto
conjunto1 = {2,4,6,8}
conjunto2 = {1,3,5}
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado =conjunto1.issuperset(conjunto2)
resultado = conjunto1 <= conjunto2

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print (resultado)


print("hagale que si puede john")
