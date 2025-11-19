import matplotlib.pyplot as plt
import numpy as np

def crear_figura_comparacion_paso_adaptativo(valores_t, valores_solucion_exacta,
                                             tabla_valores_1_rk45, tabla_valores_1_rk23,
                                             tabla_valores_1_dop853, tabla_valores_1_radau,
                                             tabla_valores_1_bdf, tabla_valores_1_lsoda):
    """
    Crea una figura completa con comparaciones de métodos con paso adaptativo
    
    :param valores_t: array, valores de t para la solución exacta
    :param valores_solucion_exacta: array, valores de y para la solución exacta
    :param tabla_valores_1_rk45: DataFrame con resultados de RK45 (scipy)
    :param tabla_valores_1_rk23: DataFrame con resultados de RK23 (scipy)
    :param tabla_valores_1_dop853: DataFrame con resultados de DOP853 (scipy)
    :param tabla_valores_1_radau: DataFrame con resultados de Radau (scipy)
    :param tabla_valores_1_bdf: DataFrame con resultados de BDF (scipy)
    :param tabla_valores_1_lsoda: DataFrame con resultados de LSODA (scipy)
    :return: figura de matplotlib
    """
    figura = plt.figure(figsize=(24,18),facecolor='w')
    gs = figura.add_gridspec(4,3)
    
    # Subplots que muestran la gráfica de la solución exacta y las aproximaciones de cada método
    ax11 = figura.add_subplot(gs[0,0])
    ax11.set_title("Comparativa de valores reales \n con aproximados RK45")
    ax11.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax11.plot(tabla_valores_1_rk45['t'], tabla_valores_1_rk45['y_aprox'], label="RK45",marker='o',color='red')
    ax11.grid()
    ax11.legend()
    
    ax12 = figura.add_subplot(gs[0,1])
    ax12.set_title("Comparativa de valores reales \n con aproximados RK23")
    ax12.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax12.plot(tabla_valores_1_rk23['t'], tabla_valores_1_rk23['y_aprox'], label="RK23",marker='o',color='blue')
    ax12.grid()
    ax12.legend()
    
    ax13 = figura.add_subplot(gs[0,2])
    ax13.set_title("Comparativa de valores reales \n con aproximados DOP853")
    ax13.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax13.plot(tabla_valores_1_dop853['t'], tabla_valores_1_dop853['y_aprox'], label="DOP853",marker='o',color='green')
    ax13.grid()
    ax13.legend()
    
    ax14 = figura.add_subplot(gs[1,0])
    ax14.set_title("Comparativa de valores reales \ncon aproximados Radau")
    ax14.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax14.plot(tabla_valores_1_radau['t'], tabla_valores_1_radau['y_aprox'], label="Radau",marker='o',color='purple')
    ax14.grid()
    ax14.legend()
    
    ax15 = figura.add_subplot(gs[1,1])
    ax15.set_title("Comparativa de valores reales \ncon aproximados BDF")
    ax15.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax15.plot(tabla_valores_1_bdf['t'], tabla_valores_1_bdf['y_aprox'], label="BDF",marker='o',color='orange')
    ax15.grid()
    ax15.legend()
    
    ax16 = figura.add_subplot(gs[1,2])
    ax16.set_title("Comparativa de valores reales \ncon aproximados LSODA")
    ax16.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax16.plot(tabla_valores_1_lsoda['t'], tabla_valores_1_lsoda['y_aprox'], label="LSODA",marker='o',color='cyan')
    ax16.grid()
    ax16.legend()
    
    # Subplots que muestran los errores globales de cada método (escala lineal y log)
    ax21 = figura.add_subplot(gs[2,:])
    ax21.set_title("Comparativa de errores globales (escala lineal)")
    ax21.grid()
    ax21.plot(tabla_valores_1_rk45['t'], tabla_valores_1_rk45['error_global'], label="RK45",marker='o',color='red')
    ax21.plot(tabla_valores_1_rk23['t'], tabla_valores_1_rk23['error_global'], label="RK23",marker='o',color='blue')
    ax21.plot(tabla_valores_1_dop853['t'], tabla_valores_1_dop853['error_global'], label="DOP853",marker='o',color='green')
    ax21.plot(tabla_valores_1_radau['t'], tabla_valores_1_radau['error_global'], label="Radau",marker='o',color='purple')
    ax21.plot(tabla_valores_1_bdf['t'], tabla_valores_1_bdf['error_global'], label="BDF",marker='o',color='orange')
    ax21.plot(tabla_valores_1_lsoda['t'], tabla_valores_1_lsoda['error_global'], label="LSODA",marker='o',color='cyan')
    ax21.legend()
    
    ax22 = figura.add_subplot(gs[3,:])
    ax22.set_title("Comparativa de errores globales (escala logarítmica)")
    ax22.grid()
    ax22.set_yscale('log')
    ax22.plot(tabla_valores_1_rk45['t'], tabla_valores_1_rk45['error_global'], label="RK45",marker='o',color='red')
    ax22.plot(tabla_valores_1_rk23['t'], tabla_valores_1_rk23['error_global'], label="RK23",marker='o',color='blue')
    ax22.plot(tabla_valores_1_dop853['t'], tabla_valores_1_dop853['error_global'], label="DOP853",marker='o',color='green')
    ax22.plot(tabla_valores_1_radau['t'], tabla_valores_1_radau['error_global'], label="Radau",marker='o',color='purple')
    ax22.plot(tabla_valores_1_bdf['t'], tabla_valores_1_bdf['error_global'], label="BDF",marker='o',color='orange')
    ax22.plot(tabla_valores_1_lsoda['t'], tabla_valores_1_lsoda['error_global'], label="LSODA",marker='o',color='cyan')
    ax22.legend()
    
    plt.tight_layout()
    return figura

def crear_grafico_barras_pasos(n_pasos_rk45, n_pasos_rk23, n_pasos_dop853, 
                               n_pasos_radau, n_pasos_bdf, n_pasos_lsoda):
    """
    Crea un gráfico de barras comparando el número de pasos usados por cada método
    
    :param n_pasos_rk45: int, número de pasos de RK45
    :param n_pasos_rk23: int, número de pasos de RK23
    :param n_pasos_dop853: int, número de pasos de DOP853
    :param n_pasos_radau: int, número de pasos de Radau
    :param n_pasos_bdf: int, número de pasos de BDF
    :param n_pasos_lsoda: int, número de pasos de LSODA
    :return: figura de matplotlib
    """
    metodos = ['RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA']
    pasos = [n_pasos_rk45, n_pasos_rk23, n_pasos_dop853, n_pasos_radau, n_pasos_bdf, n_pasos_lsoda]
    colores = ['red', 'blue', 'green', 'purple', 'orange', 'cyan']

    figura = plt.figure(figsize=(12,6), facecolor='w')
    barras = plt.bar(metodos, pasos, color=colores, alpha=0.7, edgecolor='black')

    # Agregar valores sobre las barras
    for i, (metodo, n_pasos) in enumerate(zip(metodos, pasos)):
        plt.text(i, n_pasos + max(pasos)*0.02, str(n_pasos), ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.xlabel('Método', fontsize=12, fontweight='bold')
    plt.ylabel('Número de pasos', fontsize=12, fontweight='bold')
    plt.title('Comparación del número de pasos usados por cada método\n(con control adaptativo de paso)', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    return figura
