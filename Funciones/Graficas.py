import matplotlib.pyplot as plt
import numpy as np

def graficar_solucion_exacta(valores_t, valores_y, titulo="Solución exacta"):
    """
    Grafica la solución exacta del problema
    
    :param valores_t: array, valores de tiempo
    :param valores_y: array, valores de la solución
    :param titulo: str, título del gráfico
    :return: figura de matplotlib
    """
    plt.figure(figsize=(10,5),facecolor='w')
    plt.plot(valores_t, valores_y, label=titulo)
    plt.xlabel('Tiempo (años)')
    plt.ylabel('Concentración C14')
    plt.grid()
    plt.legend()
    plt.show()

def crear_figura_completa_comparacion(h, valores_t, valores_solucion_exacta,
                                      tabla_valores_1_rk2, tabla_valores_1_rk4, 
                                      tabla_valores_1_ab2, tabla_valores_1_heun,
                                      tabla_valores_1_rk45, tabla_valores_1_rk23,
                                      tabla_valores_1_dop853, tabla_valores_1_radau,
                                      tabla_valores_1_bdf, tabla_valores_1_lsoda):
    """
    Crea una figura completa con todos los subplots de comparación para un valor de h dado
    
    :param h: float, tamaño de paso
    :param valores_t: array, valores de t para la solución exacta
    :param valores_solucion_exacta: array, valores de y para la solución exacta
    :param tabla_valores_1_rk2: DataFrame con resultados de RK2
    :param tabla_valores_1_rk4: DataFrame con resultados de RK4
    :param tabla_valores_1_ab2: DataFrame con resultados de Adams-Bashforth 2
    :param tabla_valores_1_heun: DataFrame con resultados de Heun
    :param tabla_valores_1_rk45: DataFrame con resultados de RK45 (scipy)
    :param tabla_valores_1_rk23: DataFrame con resultados de RK23 (scipy)
    :param tabla_valores_1_dop853: DataFrame con resultados de DOP853 (scipy)
    :param tabla_valores_1_radau: DataFrame con resultados de Radau (scipy)
    :param tabla_valores_1_bdf: DataFrame con resultados de BDF (scipy)
    :param tabla_valores_1_lsoda: DataFrame con resultados de LSODA (scipy)
    :return: figura de matplotlib
    """
    figura = plt.figure(figsize=(25,20),facecolor='w')
    gs = figura.add_gridspec(4,5)

    # Subplots que muestran la gráfica de la solución exacta y las aproximaciones de RK2, RK4, AB2 y Heun
    ax11 = figura.add_subplot(gs[0,0])
    ax11.set_title("Comparativa de valores reales \n con aproximados RK2 (h={})".format(h))
    ax11.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax11.plot(tabla_valores_1_rk2['t'], tabla_valores_1_rk2['y_aprox'], label="RK2",marker='o',color='red')
    ax11.grid()
    ax11.legend()

    ax12 = figura.add_subplot(gs[0,1])
    ax12.set_title("Comparativa de valores reales \n con aproximados RK4 (h={})".format(h))
    ax12.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax12.plot(tabla_valores_1_rk4['t'], tabla_valores_1_rk4['y_aprox'], label="RK4",marker='o',color='blue')
    ax12.grid()
    ax12.legend()

    ax13 = figura.add_subplot(gs[0,2])
    ax13.set_title("Comparativa de valores reales \n con aproximados AB2 (h={})".format(h))
    ax13.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax13.plot(tabla_valores_1_ab2['t'], tabla_valores_1_ab2['y_aprox'], label="AB2",marker='o',color='green')
    ax13.grid()
    ax13.legend()

    ax14 = figura.add_subplot(gs[0,3])
    ax14.set_title("Comparativa de valores reales \ncon aproximados Heun (h={})".format(h))
    ax14.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax14.plot(tabla_valores_1_heun['t'], tabla_valores_1_heun['y_aprox'], label="Heun",marker='o',color='purple')
    ax14.grid()
    ax14.legend()

    # Subplots para métodos de scipy
    ax15 = figura.add_subplot(gs[0,4])
    ax15.set_title("Comparativa de valores reales \ncon aproximados RK45".format(h))
    ax15.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax15.plot(tabla_valores_1_rk45['t'], tabla_valores_1_rk45['y_aprox'], label="RK45",marker='o',color='orange')
    ax15.grid()
    ax15.legend()

    ax16 = figura.add_subplot(gs[1,0])
    ax16.set_title("Comparativa de valores reales \ncon aproximados RK23".format(h))
    ax16.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax16.plot(tabla_valores_1_rk23['t'], tabla_valores_1_rk23['y_aprox'], label="RK23",marker='o',color='cyan')
    ax16.grid()
    ax16.legend()

    ax17 = figura.add_subplot(gs[1,1])
    ax17.set_title("Comparativa de valores reales \ncon aproximados DOP853".format(h))
    ax17.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax17.plot(tabla_valores_1_dop853['t'], tabla_valores_1_dop853['y_aprox'], label="DOP853",marker='o',color='brown')
    ax17.grid()
    ax17.legend()

    ax18 = figura.add_subplot(gs[1,2])
    ax18.set_title("Comparativa de valores reales \ncon aproximados Radau".format(h))
    ax18.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax18.plot(tabla_valores_1_radau['t'], tabla_valores_1_radau['y_aprox'], label="Radau",marker='o',color='pink')
    ax18.grid()
    ax18.legend()

    ax19 = figura.add_subplot(gs[1,3])
    ax19.set_title("Comparativa de valores reales \ncon aproximados BDF".format(h))
    ax19.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax19.plot(tabla_valores_1_bdf['t'], tabla_valores_1_bdf['y_aprox'], label="BDF",marker='o',color='gray')
    ax19.grid()
    ax19.legend()

    ax110 = figura.add_subplot(gs[1,4])
    ax110.set_title("Comparativa de valores reales \ncon aproximados LSODA".format(h))
    ax110.plot(valores_t, valores_solucion_exacta, label="Solución exacta")
    ax110.plot(tabla_valores_1_lsoda['t'], tabla_valores_1_lsoda['y_aprox'], label="LSODA",marker='o',color='olive')
    ax110.grid()
    ax110.legend()

    # Subplots que muestran los errores globales de cada método (escala lineal y log)
    ax21 = figura.add_subplot(gs[2,:-2])
    ax21.set_title("Comparativa de errores globales \n (escala lineal) (h={})".format(h))
    ax21.grid()
    ax21.plot(tabla_valores_1_rk2['t'], tabla_valores_1_rk2['error_global'], label="RK2",marker='o',color='red')
    ax21.plot(tabla_valores_1_rk2['t'], tabla_valores_1_rk4['error_global'], label="RK4",marker='o',color='blue')
    ax21.plot(tabla_valores_1_rk2['t'], tabla_valores_1_ab2['error_global'], label="AB2",marker='o',color='green')
    ax21.plot(tabla_valores_1_rk2['t'], tabla_valores_1_heun['error_global'], label="Heun",marker='o',color='purple')
    ax21.plot(tabla_valores_1_rk45['t'], tabla_valores_1_rk45['error_global'], label="RK45",marker='x',color='orange')
    ax21.plot(tabla_valores_1_rk23['t'], tabla_valores_1_rk23['error_global'], label="RK23",marker='x',color='cyan')
    ax21.plot(tabla_valores_1_dop853['t'], tabla_valores_1_dop853['error_global'], label="DOP853",marker='x',color='brown')
    ax21.plot(tabla_valores_1_radau['t'], tabla_valores_1_radau['error_global'], label="Radau",marker='x',color='pink')
    ax21.plot(tabla_valores_1_bdf['t'], tabla_valores_1_bdf['error_global'], label="BDF",marker='x',color='gray')
    ax21.plot(tabla_valores_1_lsoda['t'], tabla_valores_1_lsoda['error_global'], label="LSODA",marker='x',color='olive')
    ax21.legend()

    ax22 = figura.add_subplot(gs[2,-2:])
    ax22.set_title("Comparativa de errores globales \n (escala log.) (h={})".format(h))
    ax22.grid()
    ax22.set_yscale('log') 
    ax22.plot(tabla_valores_1_rk2['t'], tabla_valores_1_rk2['error_global'], label="RK2",marker='o',color='red')
    ax22.plot(tabla_valores_1_rk2['t'], tabla_valores_1_rk4['error_global'], label="RK4",marker='o',color='blue')
    ax22.plot(tabla_valores_1_rk2['t'], tabla_valores_1_ab2['error_global'], label="AB2",marker='o',color='green')
    ax22.plot(tabla_valores_1_rk2['t'], tabla_valores_1_heun['error_global'], label="Heun",marker='o',color='purple')
    ax22.plot(tabla_valores_1_rk45['t'], tabla_valores_1_rk45['error_global'], label="RK45",marker='x',color='orange')
    ax22.plot(tabla_valores_1_rk23['t'], tabla_valores_1_rk23['error_global'], label="RK23",marker='x',color='cyan')
    ax22.plot(tabla_valores_1_dop853['t'], tabla_valores_1_dop853['error_global'], label="DOP853",marker='x',color='brown')
    ax22.plot(tabla_valores_1_radau['t'], tabla_valores_1_radau['error_global'], label="Radau",marker='x',color='pink')
    ax22.plot(tabla_valores_1_bdf['t'], tabla_valores_1_bdf['error_global'], label="BDF",marker='x',color='gray')
    ax22.plot(tabla_valores_1_lsoda['t'], tabla_valores_1_lsoda['error_global'], label="LSODA",marker='x',color='olive')
    ax22.legend()

    # Subplot que muestra los errores locales de cada método
    ax31 = figura.add_subplot(gs[3,0])
    ax31.set_title("Errores locales RK2 (h={})".format(h))
    ax31.plot(tabla_valores_1_rk2['t'], tabla_valores_1_rk2['error_local'], label="RK2",marker='o',color='red')
    ax31.legend()
    ax31.grid()

    ax32 = figura.add_subplot(gs[3,1])
    ax32.set_title("Errores locales RK4  (h={})".format(h))
    ax32.plot(tabla_valores_1_rk4['t'], tabla_valores_1_rk4['error_local'], label="RK4",marker='o',color='blue')
    ax32.legend()
    ax32.grid()

    ax33 = figura.add_subplot(gs[3,2])
    ax33.set_title("Errores locales AB2  (h={})".format(h))
    ax33.plot(tabla_valores_1_ab2['t'], tabla_valores_1_ab2['error_local'], label="AB2",marker='o',color='green')
    ax33.legend()
    ax33.grid()

    ax34 = figura.add_subplot(gs[3,3])
    ax34.set_title("Errores locales Heun (h={})".format(h))
    ax34.plot(tabla_valores_1_heun['t'], tabla_valores_1_heun['error_local'], label="Heun",marker='o',color='purple')
    ax34.legend()
    ax34.grid()

    ax35 = figura.add_subplot(gs[3,4])
    ax35.set_title("Errores locales scipy (paso adaptativo)")
    ax35.plot(tabla_valores_1_rk45['t'], tabla_valores_1_rk45['error_local'], label="RK45",marker='x',color='orange')
    ax35.plot(tabla_valores_1_rk23['t'], tabla_valores_1_rk23['error_local'], label="RK23",marker='x',color='cyan')
    ax35.plot(tabla_valores_1_dop853['t'], tabla_valores_1_dop853['error_local'], label="DOP853",marker='x',color='brown')
    ax35.plot(tabla_valores_1_radau['t'], tabla_valores_1_radau['error_local'], label="Radau",marker='x',color='pink')
    ax35.plot(tabla_valores_1_bdf['t'], tabla_valores_1_bdf['error_local'], label="BDF",marker='x',color='gray')
    ax35.plot(tabla_valores_1_lsoda['t'], tabla_valores_1_lsoda['error_local'], label="LSODA",marker='x',color='olive')
    ax35.legend()
    ax35.grid()

    return figura
