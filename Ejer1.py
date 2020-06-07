#calcular salario seis años 
#DATOS DE ENTRADA 
salario = 1500
for n in [1,2,3,4,5,6]:
#PROCESO
    salario=salario+salario*10/100
#DATOS DE SALIDA
    print("El salario en el año {} es: {}".format(n, salario))