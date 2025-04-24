while True:
    try:
        bas=float(input("Ingrese la base: "))
        break
    except ValueError:
        print("\nIngrese un numero valido")
while True:
    try:
        alt=float(input("\nIngrese la altura: "))
        break
    except:
        print("\nIngrese un numero valido")

are=bas*alt

print(f"\nEl area de tu cuadrilatero es {are}")
while True:
    try:
        pre=float(input(" \nIngrese un precio: "))
        break
    except:
       print ("\nIngrese un precio valido")
while True:
    try:
        des=int(input("\nINgrese un descuento: "))
        if 0>=des>=100:
             break
        else:print("\nIngrese un descuento valido")
    except ValueError:
         print("\nIngrese un descuento valido")
prd= pre-((pre*des)/100)
print(f"\nTu precio con descuento es {prd}")

while True:
    try:
        num1=float(input("\nIngrese primer numero: "))
        break
    except ValueError:
        print("\nIngrese un numero valido")
while True:
    try:
        num2=float(input("\nIngrese segundo numero: "))
        break
    except ValueError:
        print("\nIngrese un numero valido")
      
        
res= num1 % num2
print(f"\nEl residuo de su division es {res}")

while True:
    try:
        sum=float(input("\nIngrese un numero: "))
        break
    except ValueError:
        print("\nIngrese un numero valido")
while True:
    try:
        res=float(input("\nIngrese otro numero: " ))
        break
    except ValueError:
        print("\nIngrese un numero valido")
while True:
    try:
        mult=float(input("\nIngrese otro numero: "))
        break
    except ValueError:
        print("\nIngrese un numero valido")
while True:
    try:
        div=float(input("\nIngrese otro numero: "))
        break
    except ValueError:
        print("\nIngrese un numero valido")
        
        
        
        
op= (((1+sum)-res)*mult)/div

print(f"\nEl resultado es {op}")