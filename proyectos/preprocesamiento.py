# preprocesamiento.py
def limpiar_datos(df):
    # Función para limpiar datos
    return df.dropna()

def estandarizar_datos(df):
    # Función para estandarizar datos
    return (df - df.mean()) / df.std()