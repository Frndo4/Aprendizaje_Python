#Bucle While

numero=0
while numero<20:
    print(numero)
    numero+=1
    
import math
num=int(input("Escriba un número: "))
while num<0:
    print("Por favor ingrese un número positivo")
    num=int(input("Vuelva a ingresar un número positivo: "))
print(f"El resultado de la raíz cuadrada es: {math.sqrt(num):.4f}")