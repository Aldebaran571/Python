#creando una funcion simple
def saludo():
    print("hola mostro, como va la causa?")
saludo()

def saludar (nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif( sexo == "hombre"):
        adjetivo = "campeon"
    else:
        adjetivo= "amistad"

    print(f"hola {nombre}, mi {adjetivo}, como vamos?")
saludar ("john", "hombre")