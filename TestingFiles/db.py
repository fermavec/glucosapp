import os
import django

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glucosapp.settings')
django.setup()
import csv
from food_specs.models import FoodInformation

# Ruta al archivo CSV
ruta_csv = r'C:\Users\Fernando\Documents\FMG App\app\glucosapp\SMAE.csv'

# Abrir el archivo CSV y crear un lector CSV
with open(ruta_csv, 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    # Leer la primera fila para obtener los nombres de las columnas
    columnas = next(lector_csv)

    # Iterar sobre las filas restantes del archivo CSV
    for fila in lector_csv:
        # Crear un diccionario con los datos de la fila
        datos_fila = dict(zip(columnas, fila))

        # Crear una instancia de FoodInformation con los datos de la fila
        food_info = FoodInformation(**datos_fila)

        # Guardar la instancia en la base de datos
        food_info.save()

print("Datos del CSV cargados exitosamente en la base de datos.")
