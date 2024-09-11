#2 listas una con nombres y otra con apellidos
nombres = ["john ", "fredy", "lucely", "luisa"]
apellidos =["martinez", "nieto", "piñeros", "garcia"]

#registrar esta informacion en un archivo txt de forma optima

with open("nombres_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n-----------------\n')for n, a in zip(nombres,apellidos)] 