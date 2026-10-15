"""Calcula el importe final de un pedido con IVA, descuento y gastos de envío.
Módulo 0485 Programación · UD 2 · Autor: Andrea · Fecha: 15/10/2026
"""

IVA_GENERAL = 0.21
ENVIO = 4.95
UMBRAL_ENVIO_GRATIS = 50.0

def main():
    """Solicita el artículo, el precio, las unidades y el descuento para calcular el importe final."""
    # Entradas
    articulo = input("Artículo: ")
    precio = float(input("Precio unitario sin IVA (€): "))
    unidades = int(input("Unidades: "))
    descuento = int(input("Porcentaje de descuento (%): "))

    # Proceso
    base = precio * unidades
    if descuento > 0:
        base_final = base - base * (descuento / 100) 
    else:
        base_final = base
    ahorro = base - base_final
    iva = base * IVA_GENERAL
    envio = 0.0 if base >= UMBRAL_ENVIO_GRATIS else ENVIO
    total = base_final + iva + envio

    # Salidas
    print(f"\nPresupuesto de {unidades} x {articulo}")
    print(f" Base imponible:         {base:8.2f} €")
    print(f" Base tras el descuento: {base_final:8.2f} €")
    print(f" Ahorro obtenido:        {ahorro:8.2f} €")
    print(f" IVA (21 %):             {iva:8.2f} €")
    print(f" Envío:                  {envio:8.2f} €")
    print(f" TOTAL:                  {total:8.2f} €")

if __name__ == "__main__":
    main()