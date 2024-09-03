numeros = [4,2,8,75,38]

#encontrar el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrar el numero mas bajo de la lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando un numero 
numero = round(12.8614546, 2)# se coloca la coma segun cuantos numeros decimales se requiera
print(numero)

#retorna False ->0, vacio , False, none \ True -> distinto a 0, True, cadena
resultado_bool = bool(1)
print(resultado_bool)

#retorna True solo si todos los elementos son verdaderos, en caso de tener un valor nulo regresa False
resultado_all =all([12,25, False, "uyrdfgbyd"])
print(resultado_all)

#suma todos los valores de un itinerable
suma_total = sum(numeros)
print(suma_total)