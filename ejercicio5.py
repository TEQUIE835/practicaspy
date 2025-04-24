edad=int(input("Ingrese su edad: "))
lic=str(input("\nTienes licencia de conduccion? Y/N "))
if edad >= 18 and lic=="y" or lic=="Y":
    print("\nPuedes conducir")
else:print("\nNo puedes conducir")

tit=str(input("\nTienes titulo universitario? Y/N "))

if tit=="Y" or tit=="y":
    exp1=str(input("\nTienes experiencia de trabajo? Y/N "))
    if exp1 == "Y" or exp1 == "y":
        print("\nEres facilmente empleable")
    elif exp1 == "n" or exp1 == "N":
        print("\nEres empleable")
    else: print("\nIngrese una opcion valida")
elif tit=="n" or tit=="N":
    exp1=str("\nTienes experiencia de trabajo? Y/N ")
    if exp1 == "Y" or exp1 == "y":
        print("\nEres empleable")
    elif exp1 == "n" or exp1 == "N":
        print("\nEres No eres empleable")
    else: print("\nIngrese una opcion valida")
else: print("\nIngrese una opcion valida")
while True:
    try:
        num=float(input("\nIngresa un numero: "))
        break
    except ValueError:
        print("\nIngrese un numero valido")

if 10<=num<=50:
    print(f"\n{num} esta entre 10 y 50")
elif num<10 or num>50:
    print(f"\n{num} no esta entre 10 y 50 :c")
else: print("\npon un numero correcto")