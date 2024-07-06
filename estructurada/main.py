def agregar_item(inventario, nombre, descripcion, precio, cantidad):
    item = {"nombre": nombre, "descripcion": descripcion, "precio": precio, "cantidad": cantidad}
    inventario.append(item)
    print(f"{nombre} agregado al inventario.")

def ver_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        for item in inventario:
            print(f"- {item['nombre']}: {item['descripcion']} (${item['precio']}, {item['cantidad']} disponibles)")

def simular_compra(inventario, nombre_item, cantidad):
    for item in inventario:
        if item['nombre'] == nombre_item:
            if item['cantidad'] >= cantidad:
                print(f"Compra simulada de {cantidad} {nombre_item} por ${item['precio'] * cantidad}")
                return True 
    return False  


def main():
    inventario = []

    while True:
        print("Menú:")
        print("1. Agregar item")
        print("2. Ver inventario")
        print("3. Simular compra")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del item: ")
            descripcion = input("Descripción del item: ")
            precio = float(input("Precio del item: "))
            cantidad = int(input("Cantidad del item: "))
            agregar_item(inventario, nombre, descripcion, precio, cantidad)
        elif opcion == "2":
            ver_inventario(inventario)
        elif opcion == "3":
            nombre_item = input("Nombre del item a comprar: ")
            cantidad = int(input("Cantidad a comprar: "))
            if simular_compra(inventario, nombre_item, cantidad):
                print("Compra simulada con éxito.")
            else:
                print("No hay suficiente stock del item seleccionado.")
        elif opcion == "4":
            break
    else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
