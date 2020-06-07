#HAMBURGUESAS
#DATOS DE ENTRADA
N = int(input("¿CUÁNTAS HAMBURGUESAS DESEA?"))
costo = 0
#PROCESO
for n in range(1,N+1):
    H = input("selecione el tipo de hamburguesa: Simple(S), Doble(D), Triple(T):")
    if H == "S":
        costo=costo+20
    elif H == "D":
        costo=costo+25
    elif H == "T":
        costo=costo+28
#PROCESO 
P = input("SELECCIONE EL MEDIO DE PAGO: Efectivo(E), Tarjeta(T):")
if P == "E":
    costo= costo
elif P == "T":
    costo=costo*1.05
#DATOS DE SALIDA
print("El costo total de su pedido es: {}".format(costo))