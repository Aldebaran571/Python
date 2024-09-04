#creando una funcion simple
"""def saludo():
    print("hola mostro, como va la causa?")
saludo()
#ejecutando una funcion simple
def saludar (nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif( sexo == "hombre"):
        adjetivo = "campeon"
    else:
        adjetivo= "amistad"

    print(f"hola {nombre}, mi {adjetivo}, como vamos?")
saludar ("john", "perro")"""

#crear funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int (num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num -5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    print(contraseña)
    return contraseña, num

#desempaquetando la funcion
password, primer_numero = crear_contraseña_random(98)

#mostrando los resultados obenidos y los datos  para obtenerlo
print(f'tu contraseña es: {password}')
print(f'el primer numero usado es: {primer_numero}')