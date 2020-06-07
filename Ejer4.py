#NUMEROS IGUALES A CERO
#DATOS DE ENTRADA
N = int(input("Ingrese cantidad de números que ingresará: "))
cero = 0
negativo = 0
positivo = 0
#PROCESO
for n in range(1,N+1):
    num = int(input("ingrese numero {}: ".format(n)))
    if num ==0:
        cero =cero+1
    elif num <0:
        negativo=negativo+1
    elif num >0:
        positivo=positivo+1
#DATOS DE SALIDA
print("Hay {} numeros iguales a cero".format(cero))
print("Hay {} numeros menores a cero".format(negativo))
print("Hay {} numeros mayores a cero".format(positivo))
