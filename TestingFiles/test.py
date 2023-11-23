import os
import pandas as pd

# Ruta de la carpeta que contiene los archivos CSV
carpeta_csv = './static/others'

# Lista para almacenar los encabezados de cada archivo CSV
encabezados_por_archivo = []

# Recorre cada archivo en la carpeta
for archivo in os.listdir(carpeta_csv):
    if archivo.endswith('.csv'):
        # Construye la ruta completa al archivo
        ruta_completa = os.path.join(carpeta_csv, archivo)

        # Lee solo la primera fila del archivo CSV (encabezados)
        encabezados = pd.read_csv(ruta_completa, nrows=1).columns.tolist()

        # Agrega los encabezados a la lista
        encabezados_por_archivo.append((archivo, encabezados))

# Verifica si todos los archivos tienen los mismos encabezados
encabezados_iguales = all(encabezados == encabezados_por_archivo[0][1] for _, encabezados in encabezados_por_archivo)

if encabezados_iguales:
    print("Todos los archivos tienen los mismos encabezados.")
    # Crea un DataFrame con los encabezados del primer archivo (puedes leer todos los archivos si es necesario)
    df = pd.read_csv(os.path.join(carpeta_csv, encabezados_por_archivo[0][0]))
    print(df)
else:
    print("Los encabezados de los archivos no son iguales.")
    for archivo, encabezados in encabezados_por_archivo:
        print(f"Encabezados en {archivo}: {encabezados}")
