#Operadores lógicos

#AND
a=30
b=40
c=50
r=((a<b) and (b<c))
print(r)

#OR
a=30
b=40
c=50
r=((a>b) or (b<c))
print(r)

#NEGACIÓN
a=30
b=40
c=50
r= not((a>b) or (b<c))
print(r)
