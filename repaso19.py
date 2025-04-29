numeros_pares=[]

for i in range(5):
    numero=int(input(f"Ingresa el numero {i+1}:  "))
    if numero % 2 ==0:
        numeros_pares.append(numero)

print("Numeros pares ingresados: ",numeros_pares)