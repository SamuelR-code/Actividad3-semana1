frutas=["mango", "pera", "arroz", "manzana"]
print("Lista de frutas",frutas)
eliminar=input("Ingrese cual fruta quiere eliminar  ")

if eliminar in frutas:
    frutas.remove(eliminar)
    print("Fruta eliminada.")
else:
    print("La fruta no esta en la lista.")

print("lista actualizada", frutas)

