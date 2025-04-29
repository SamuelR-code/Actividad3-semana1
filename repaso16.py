numeros=[7,9,3,20,18]

buscado=int(input("ingresa un numero:  "))

if buscado in numeros:
    posicion=numeros.index(buscado)
    print(f"el numero {buscado} esta en la posicion {posicion}.")
else:
    print(f"el numero {buscado} no esta en la lista")