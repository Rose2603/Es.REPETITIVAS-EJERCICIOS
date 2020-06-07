#ALUMNOS EN LA ESCUELA
#DATOS DE ENTRADA
M = int(input("Ingrese cantidad total de salones: "))
sum_prom = 0
#PROCESO
for m in range(1,M+1):
    N = int(input("Ingrese cantidad de alumnos del salón {}:".format(m)))
    edad_total = 0
    for n in range(1,N+1):
        edad = int(input("Ingrese edad del alumno {}:".format(n)))
        edad_total = edad_total+edad
    prom = edad_total/N
    sum_prom = sum_prom+prom
    print("LA EDAD PROMEDIO EN EL SALÓN {} ES: {}".format(m,prom))
#DATOS DE SALIDA
    prom_total =sum_prom/M
    print("LA EDAD PROMEDIO EN TODO LA ESCUELA ES: {}".format(prom_total))