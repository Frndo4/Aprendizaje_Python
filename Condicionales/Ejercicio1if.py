#Ejercicio 1 If

a=int(input("Digita tu primer número: "))
b=int(input("Digita tu segundo número: "))

if a%2==0 and b%2==0:
    print("Ambos son números pares")
elif a%2==0 and b%2!=0:
    print(f"{a} es un número par")
elif a%2!=0 and b%2==0:
    print(f"{b} es un número par")
else:
    print("Ambos son impares")
