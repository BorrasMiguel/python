###
# Trabajando con fechas y horas en Python
###

import os
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
os.system('cls')

from datetime import datetime, timedelta

# 1. Obtener la fecha y la hora actual
now = datetime.now()
print(f'Fecha y hora actual: {now}')

# 2. Crear una fecha y una hora específica
specific_date = datetime(1994, 3, 16)
print(specific_date)

# 3. Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato:
format_date = now.strftime("%d/%m/%y %H:%M:%S")
format_date2 = now.strftime("%A %B %Y %H:%M:%S") # Nombre dia mes
print(f'Fecha formateada: {format_date}')
print(f'Fecha formateada: {format_date2}')

# 4. Operaciones con fechas
yesterday = datetime.now() - timedelta(days=1)
print(f'Ayer: {yesterday}')

tomorrow = datetime.now() + timedelta(days=1)
print(f'Mañana: {tomorrow}')

one_hour_after = datetime.now() + timedelta(hours=1)
print(f'Una hora después: {one_hour_after}')

# 5. Obtener componentes individuales de una fecha
year = now.year
print(yesterday)

month = now.month
print(month)

# 6. Calcular la diferencia entre dos fechas
date1 = datetime.now()
date2 = datetime(2025, 2, 13, 15, 30, 0)
difference = date2 - date1
print(f'Diferencia entre las fechas: {difference}')

