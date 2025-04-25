def tryfloat():
    while True:
        try:
            a=float(input("Ingrese la base: "))
            return a
            
        except ValueError:
            print("\nIngrese un numero valido")


bas=tryfloat()
alt=tryfloat()

are=bas*alt

print(f"\nEl area de tu cuadrilatero es {are}")
pre=tryfloat()
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

num1=tryfloat()
num2=tryfloat()
      
        
res= num1 % num2
print(f"\nEl residuo de su division es {res}")

sum=tryfloat()
res=tryfloat()
mult=tryfloat()
div=tryfloat
        
        
        
        
op= (((1+sum)-res)*mult)/div

print(f"\nEl resultado es {op}")