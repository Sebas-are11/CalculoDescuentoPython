def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra en dólares.

    Args:
    monto_total (float): Monto total de la compra en dólares.
    porcentaje_descuento (float, optional): Porcentaje de descuento. Por defecto es 10%.

    Returns:
    float: Monto del descuento calculado en dólares.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada a la función calcular_descuento
monto1 = 1000  # Monto total de la primera compra en dólares
descuento1 = calcular_descuento(monto1)  # Calcula el descuento con el porcentaje predeterminado
print(f"El descuento aplicado es de ${descuento1} dólares")

monto2 = 2000  # Monto total de la segunda compra en dólares
porcentaje_descuento2 = 15  # Porcentaje de descuento personalizado
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)  # Calcula el descuento con un porcentaje personalizado
print(f"El descuento aplicado es de ${descuento2} dólares")
