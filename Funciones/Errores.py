import numpy as np

def calcular_y_reales(tabla_valores, f):
    """
    Función que calcula los valores de y_real para una tabla de valores de un método de acuerdo con la solución exacta del PVI

    :parametros tabla_valores: DataFrame con columnas t, y_aprox y error_local, f: función que representa la solución exacta del PVI
    :return: DataFrame, tabla de valores de t, y_real, y_aprox y error_local
    """
    tabla_valores['y_real'] = f(tabla_valores['t'])

def calcular_error_global(tabla_valores):
    """
    Función que calcula error global de una tabla de valores y lo agrega a la tabla

    :parametros tabla_valores: DataFrame con columnas t, y_real, y_aprox y error_local
    :return: DataFrame, tabla de valores de t, y_real, y_aprox, error_global y error_local
    """
    tabla_valores['error_global'] = np.abs(tabla_valores['y_aprox'] - tabla_valores['y_real'])