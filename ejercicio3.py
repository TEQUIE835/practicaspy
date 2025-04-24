bas=float(input("Ingrese la base: "))
alt=float(input("\nIngrese la altura: "))

are=bas*alt

print(f"\nEl area de tu cuadrilatero es {are}")

pre=float(input(" \nIngrese un precio: "))
des=int(input("\nINgrese un descuento: "))
prd= pre-((pre*des)/100)
print(f"\nTu precio con descuento es {prd}")


num1=float(input("\nIngrese primer numero: "))
num2=float(input("\nIngrese segundo numero: "))
res= num1 % num2
print(f"\nEl residuo de su division es {res}")


sum=float(input("\nIngrese un numero: "))
res=float(input("\nIngrese otro numero: " ))
mult=float(input("\nIngrese otro numero: "))
div=float(input("\nIngrese otro numero: "))
op= (((1+sum)-res)*mult)/div

print(f"\nEl resultado es {op}")