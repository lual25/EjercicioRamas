def calcular_total(precio: float, cantidad: int) -> float:
    """Calcula el total base de una compra."""
    subtotal = precio * cantidad
    total_desc = subtotal * 0.1
    subtotal_con_desc = subtotal - total_desc
    subtotal_iva = subtotal_con_desc * 0.16
    subtotal_con_iva = subtotal_con_desc + subtotal_iva
    return subtotal_con_iva


def main():
    print("=== Sistema de Cobro ===")
    precio = 100.0
    cantidad = 2
    total = calcular_total(precio, cantidad)
    print(f"total a pagar: ${total:.2f}")


if __name__ == "__main__":
    main()