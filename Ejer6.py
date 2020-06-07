#CALCULANDO PESOS
#DATOS DE ENTRADA
x = int(input("Ingrese cantidad de pesos que deposita cada mes: "))
monto = 12*x
N = int(input("Ingrese cantidad de años: "))
#PROCESO
for n in range(1,N+1):
    monto = monto+monto*10/100
#DATOS DE SALIDA
    print("El monto total en el año {} es: {}".format(n,monto))