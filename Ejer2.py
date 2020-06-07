#CALCULAR CALIFICACIONES
#DATOS DE ENTRADA
N = int(input("Ingrese cantidad de alumnos: "))
aprobado = 0
desaprobado = 0
for n in range(1,N+1):
    nota = int(input("Ingrese nota de alumno {}: ".format(n))) 
#PROCESO
if nota >= 10.5:
    aprobado = aprobado+1
elif nota < 10.5:
    desaprobado = desaprobado+1
#DATOS DE SALIDA
print("El número de aprobados es:{}".format(aprobado))
print("El número de desaprobados es: {}".format(desaprobado))