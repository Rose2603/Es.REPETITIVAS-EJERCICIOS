#CAJA REGISTRADORA
#DATOS DE ENTRADA
for n in range(1,7):
#PROCESO
    if n ==1:
        mon_1 = int(input("INGRESE CANTIDAD DE MONEDAS DE 1 PESO:"))
        din_1 = 1*mon_1
    elif n ==2:
        mon_5 = int(input("INGRESE CANTIDAD DE MONEDAS DE 5 PESOS:"))
        din_5 = 5*mon_5
    elif n ==3:
        mon_10 = int(input("INGRESE CANTIDAD DE MONEDAS DE 10 PESOS:"))
        din_10 = 10*mon_10
    elif n ==4:
        bill_10 = int(input("INGRESE CANTIDAD DE BILLETES DE 10 PESOS:"))
        din_10b = 10*bill_10
    elif n ==5:
        bill_20 = int(input("INGRESE CANTIDAD DE BILLETES DE 20 PESOS:"))
        din_20b = 20*bill_20
    elif n ==6:
        bill_50 = int(input("INGRESE CANTIDAD DE BILLETES DE 50 PESOS:"))
        din_50b = 50*bill_50
        dinero= din_1+din_5+din_10+din_10b+din_20b+din_50b
#DATOS DE SALIDA
print("El dinero total en la caja registradora es: {} pesos".format(dinero))
 