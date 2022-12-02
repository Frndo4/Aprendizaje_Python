print("Ingrese su primer número")
num1=int(input())
print("Su primer número es: " + str(num1))

print("Ingrese su segundp número")
num2=int(input())
print("Su segundo número es: " + str(num2))

print("Ingrese su tercer número")
num3=int(input())
print("Su tercer número es: " + str(num3) + "\n")

def num_max_of_three():
    if num1 > num2 and num1 > num3:
        print("El número mayor es: " + str(num1))
    elif num2 > num1 and num2 > num3:
        print("El número mayor es: " + str(num2))
    elif num3 > num1 and num3 > num2:
        print("El número mayor es: " + str(num3))

num_max_of_three()