import requests

def obtener_tipos_cambio_2025():
    datos_totales = []

    for mes in range(1, 13):  # De enero (1) a diciembre (12)
        url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2025"
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()  # Lanza error si la respuesta es incorrecta
            datos_mes = respuesta.json()
            datos_totales.extend(datos_mes)
        except requests.RequestException as e:
            print(f"Error al obtener datos del mes {mes}: {e}")

    return datos_totales

def analizar_tipos_cambio(data):
    if not data:
        print("No hay datos disponibles.")
        return
    min_compra = min(data, key=lambda x: x['compra'])['compra']
    max_venta = max(data, key=lambda x: x['venta'])['venta']
    max_diferencia = max(data, key=lambda x: x['venta'] - x['compra'])
    diferencia_max = max_diferencia['venta'] - max_diferencia['compra']

    fechas_min_compra = [d['fecha'] for d in data if d['compra'] == min_compra]
    fechas_max_venta = [d['fecha'] for d in data if d['venta'] == max_venta]
    fechas_max_diferencia = [d['fecha'] for d in data if (d['venta'] - d['compra']) == diferencia_max]
    print(f"\nFecha con valor mínimo de compra ({min_compra}):")
    for fecha in fechas_min_compra:
        print(f"- {fecha}")

    print(f"\nFecha con valor máximo de venta ({max_venta}):")
    for fecha in fechas_max_venta:
        print(f"- {fecha}")

    print(f"\nFecha con mayor diferencia compra-venta ({diferencia_max:.4f}):")
    for fecha in fechas_max_diferencia:
        print(f"- {fecha}")

datos = obtener_tipos_cambio_2025()
analizar_tipos_cambio(datos)

