ent = int("2")
flot=float("3.5")
cad=str(4)
opc=bool(1)
print(type(ent))

print("\n", type(flot))

print("\n", type(cad))
print("\n", type(opc))

cad1="3"
cad2=int(cad1)
cads = cad2 +3
print("\n", cads)


print("")

entr=input("\nIngresa un numero: ")

entr = float(entr)
mult= entr*2
print(f"\nEl doble de tu numero es {mult}")




prueba= input("\nEscribe cualquier cosa: ")
print
try:
    prueba1 = int(prueba)
    print(f"\n{prueba} puede convertirse a numero")

except:
    print(f"\n{prueba} no puede convertirse a numero")