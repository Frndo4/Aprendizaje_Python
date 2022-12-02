#Ejercicio 4 if

saldo=2000
print("1. Ingreso de dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. Salir")

seleccion=int(input("Elija una opción: "))

if seleccion == 1:
    ingreso = float(input("Dinero a ingresar: $"))
    saldo+=ingreso
    print(f"Su nuevo saldo en la cuenta es de: ${saldo}")
elif seleccion == 2:
    salida=float(input("Dinero a retirar: $"))
    if salida > saldo:
        print("Saldo insuficiente")
    else:
        saldo-=salida
        print(f"Nuevo saldo disponible: ${saldo}")
elif seleccion == 3:
    print(f"Saldo disponible: ${saldo}")
elif seleccion == 4:
    print("Fin")
else:
    print("¡Error de selección!")





