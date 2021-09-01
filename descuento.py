producto1 = float(input("Producto 1: "))
producto2 = float(input("Producto 2: "))
producto3 = float(input("Producto 3: "))
producto4 = float(input("Producto 4: "))

descuento = 15

subtotal = producto1 + producto2 + producto3 + producto4

total = subtotal - ((subtotal * 15) / 100)

print("Su total a pagar es: ", total)