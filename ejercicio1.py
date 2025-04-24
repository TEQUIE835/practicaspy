nombre = str(input("Ingrese porfavor su nombre: "))
edad= int(input("\nIngrese su edad: "))
print(f"\nHola {nombre}, de {edad} años, como estas, te estaremos preguntando unas cosas")
comf=str(input("\nIngresa tu comida favorita: "))
colf=str(input("\nIngresa tu color favorito: "))
print(f"\nAsi que {nombre}, te gusta comer {comf} y te gusta el color {colf}, interesante")
while True:
    try:
        numa=float(input("\nIngresa un numero cualquiera: "))
        break
    except ValueError:
        print("\nIngrese un numero valido")
numdob= numa *2
numtri= numa*3
print(f"\n{nombre}, tu numero es {numa} y su doble es {numdob} y su triple es {numtri}")