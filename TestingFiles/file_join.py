import os
import pandas as pd

carpeta_csv = './static/others'

dataframes_por_archivo = {}
names = []

# Recorre cada archivo en la carpeta
for i, archivo in enumerate(os.listdir(carpeta_csv)):
    if archivo.endswith('.csv'):
        # Construye la ruta completa al archivo
        names.append(os.path.join(carpeta_csv, archivo))
        print(archivo)


print(len(names))

df_1 =pd.read_csv(names[0])
df_2 = pd.read_csv(names[1])
df_3 = pd.read_csv(names[2])
df_4 = pd.read_csv(names[3])
df_5 = pd.read_csv(names[4])
df_6 = pd.read_csv(names[5])
df_7 = pd.read_csv(names[6])
df_8 = pd.read_csv(names[7])
df_9 = pd.read_csv(names[8])
df_10 = pd.read_csv(names[9])
df_11 = pd.read_csv(names[10])
df_12 = pd.read_csv(names[11])
df_13 = pd.read_csv(names[12])
df_14 = pd.read_csv(names[13])
df_15 = pd.read_csv(names[14])
df_16 = pd.read_csv(names[15])
df_17 = pd.read_csv(names[16])
df_18 = pd.read_csv(names[17])

dataframes = [df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18]

for i, element in enumerate(dataframes):
    dataframes[i] = element = element[['ALIMENTOS', 'Cantidad sugerida', 'Unidad', 'Peso bruto redondeado (g)', 'Peso neto (g)', 'Energia (Kcal)', 'Hidratos de carbono (g)']]
    dataframes[i].columns = ['Alimento', 'Porción', 'Unidad', 'Peso Bruto (g)', 'Peso Neto (g)', 'Energia (Kcal)', 'Carbohidratos (g)']

dataframes[0]['Clasificación'] = 'A.O.A MUY BAJOS EN GRASA'
dataframes[1]['Clasificación'] = 'A.O.A.ALTO EN GRASA'
dataframes[2]['Clasificación'] = 'A.O.A.MODERADOS EN GRASA'
dataframes[3]['Clasificación'] = 'ACEITES Y GRASAS CON PROTEINAS'
dataframes[4]['Clasificación'] = 'ACEITES Y GRASAS'
dataframes[5]['Clasificación'] = 'ALIMENTOS LIBRES EN ENERGIA'
dataframes[6]['Clasificación'] = 'AZUCARES CON GRASA'
dataframes[7]['Clasificación'] = 'AZUCARES SIN GRASA'
dataframes[8]['Clasificación'] = 'BEBIDAS ALCOHOLICAS'
dataframes[9]['Clasificación'] = 'CEREALES CON GRASA'
dataframes[10]['Clasificación'] = 'CEREALES SIN GRASA'
dataframes[11]['Clasificación'] = 'FRUTAS'
dataframes[12]['Clasificación'] = 'LECHE CON AZUCAR'
dataframes[13]['Clasificación'] = 'LECHE DESCREMADA'
dataframes[14]['Clasificación'] = 'LECHE ENTERA'
dataframes[15]['Clasificación'] = 'LECHE SEMIDESCREMADA'
dataframes[16]['Clasificación'] = 'LEGUMINOSAS'
dataframes[17]['Clasificación'] = 'VERDURAS'

big_df = pd.concat(dataframes, ignore_index=True)

big_df.to_csv('SMAE.csv', index=False)