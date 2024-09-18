#Lista de la compra
lista_compra = ["Manzanas", "Leche", "Pan"]

print("Lista de la comrpa inicial", lista_compra)

nuevo_item = input("Que mas nesecita comprar? ")
lista_compra.append(nuevo_item)

print("Lista de la compra actualizada", lista_compra)

item_eliminar = input("Que item quieres eliminar?")
if item_eliminar in lista_compra:
    lista_compra.remove(item_eliminar)
    print("Lista de la compra despues de eliminar:", lista_compra)
else:
    print("Ese item no esta en la lista")                                
