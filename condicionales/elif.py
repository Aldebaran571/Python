ingreso_mensual = 81000
gasto_mensual = 80000
#if anidados y else if (elif)
if ingreso_mensual >10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("esta en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("esta gastando lo permitido")
    else:
        print("esta gastando demasiado")
        
    
    
elif ingreso_mensual >1000:
    print("esta bien en latam")
    
elif ingreso_mensual >100:
    print("esta bien en col")
    
elif ingreso_mensual >10:
    print("esta bien  jodido")    

else:
    print("estamos en la olla papá")