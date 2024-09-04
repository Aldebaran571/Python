#falto el docente y los alumnos van a hacer la clase
#se pide el nombre y la edad de los estudiantes que asistieron a la clase
def obtener_compañeros(cantidad_de_compañeros):
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir los datos de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = input("ingrese la edad del compañero: ")
        compañero =(nombre, edad)
        
    #agregando la informacion a la lista    
        compañeros.append(compañero)
        
    #organizando de menor a mayor segun la edad    
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros [x]devuelve la tupla con nombre{nombne, edad }y despues accedemos al nombre para acceder al nombre y despues al profesor
    asistente = compañeros [0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente, profesor

#desempaquetamos lo que nos retorna la funcion 
asistente, profesor =obtener_compañeros(5)

#mostrando el resultado
print(f' el profesor es:{profesor}, y sus asistente es: {asistente}')