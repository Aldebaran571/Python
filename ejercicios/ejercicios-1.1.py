#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_chimbo = 1.5

#diferencia de duracion
diferencia_con_min = 100 - curso_chimbo / otros_cursos_min *100
diferencia_con_max = 100 - curso_chimbo  *1000 // otros_cursos_max /10
diferencia_con_promedio = 100 - curso_chimbo / otros_cursos_promedio *100

print(f'este curso chimbo tarda un {diferencia_con_min}% menos que el mas rapido')
print(f'este curso chimbo tarda un {diferencia_con_max}% menos que el mas lento')
print(f'este curso chimbo tarda un {diferencia_con_promedio}% menos que el mas promedio')