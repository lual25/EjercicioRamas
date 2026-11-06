def calcular_total(precio: float, cantidad: int) -> float:
    """Calcula el total base de una compra."""
    subtotal = precio * cantidad
    total_desc = subtotal * 0.1
    total = subtotal - total_desc
    return total


def main():
    print("=== Sistema de Cobro ===")
    precio = 100.0
    cantidad = 2
    total = calcular_total(precio, cantidad)
    print(f"total a pagar: ${total:.2f}")


if __name__ == "__main__":
    main()