import pandas as pd
import numpy as np

# Función para limpiar datos
def limpiar_datos(df):
    # Verificar valores faltantes
    if df.isnull().values.any():
        df.fillna(df.mean(), inplace=True)

    # Verificar filas repetidas
    df.drop_duplicates(inplace=True)

    # Verificar y eliminar valores atípicos
    q1 = df['Cantidad'].quantile(0.25)
    q3 = df['Cantidad'].quantile(0.75)
    iqr = q3 - q1
    df = df[~((df['Cantidad'] < q1 - 1.5 * iqr) | (df['Cantidad'] > q3 + 1.5 * iqr))]

    q1 = df['Precio'].quantile(0.25)
    q3 = df['Precio'].quantile(0.75)
    iqr = q3 - q1
    df = df[~((df['Precio'] < q1 - 1.5 * iqr) | (df['Precio'] > q3 + 1.5 * iqr))]

    # Crear columna que categorice por edades
    bins = [0, 12, 19, 39, 59, np.inf]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['Categoria Edad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)

    return df

# Llamar a la función para limpiar los datos
df_limpio = limpiar_datos(df)