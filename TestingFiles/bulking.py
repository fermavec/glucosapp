import pandas as pd

# Lee el archivo CSV
df = pd.read_csv(r'C:\Users\Fernando\Documents\FMG App\app\glucosapp\SMAE.csv')
df.columns = ['food', 'portion', 'units', 'gross_weight', 'net_weight', 'energy', 'carbs', 'clasification']
# Convierte el DataFrame a JSON
json_data = df.to_json(orient='records')

# Guarda el JSON en un archivo si es necesario
with open(r'C:\Users\Fernando\Documents\FMG App\app\glucosapp\SMAE.json', 'w') as json_file:
    json_file.write(json_data)
