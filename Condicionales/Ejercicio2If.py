#Ejercicio 2 if

a=int(input("Digita tu primer número: "))
b=int(input("Digita tu segundo número: "))
c=int(input("Digita tu tercer número: "))

if a>=b and a>=c:
    print(f"El número mayor es: {a}")
elif b>=a and b>=c:
    print(f"El número mayor es: {b}")
elif c>=a and c>=b:
    print(f"El número mayor es: {c}")

