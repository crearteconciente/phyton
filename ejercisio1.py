#ejercicio1

print("---------1-------------")

n=5
for linea in range (1,n+1):             #este primer for crea saltos de linea de 1 a 6 (n+1)
    s="*"                               #se crea una variable para los asterisctos
    for conteo in range (1,linea+1):    #se crea una nueva lista que va incrementando segun cada interaccion
        print (s, end='')               #se imrpime los asteriscos segun el ciclo anterior
    print()                             #imprime un salto de linea
print() 