numeros=[1,2,3,4,5]

numero= int(input("numero a ingresar: "))
posicion=int(input("en cual posicion(0 a 4):  "))

numeros.insert(posicion,numeros)
print("Lista actualizada",numeros)