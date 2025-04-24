num1=float(input("Ingrese un numero: "))
num2=float(input("\nIngrese otro numero: "))
if num1>num2:
    print(f"\n{num1} es mayor que {num2}")
elif num2>num1:
    print(f"\n{num2} es mayor que {num1}")
elif num1==num2:
    print(f"\n{num1} y {num2} son iguales")
else: print("\nIngrese numeros validos")


eda=int(input("\nIngrese su edad: "))

if eda<18:
    print("\nEres menor de edad")
elif eda>=18:
    print("\nEres mayor de edad")
else: print("\nIngrese una edad valida")



cad1=str(input("\nIngrese texto: "))
cad2=str(input("\nIngrese texto 2: "))

if cad1==cad2:
    print("\nLos dos textos son iguales")
elif cad1!=cad2:
    print("\nLos textos son diferentes")
else: print("\nIngrese textos validos")