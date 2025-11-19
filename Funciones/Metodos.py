import pandas as pd
import numpy as np
import scipy.integrate as spi

def runge_kutta_2_trapecio(t_inicial, t_final, h, y_inicial, f):
    """
    Función que implementa el método del trapecio o Euler modificado (Runge-Kutta de segundo orden)
    :parametros t_inicial: float, valor inicial de t, t_final: float, valor final de t (valor a aproximar), h: float, tamaño del paso, y_inicial: float, valor inicial para el primer paso, f: función derivada del PVI
    :return: DataFrame, tabla de valores de t, y_aprox y error_local
    """
    # Guardamos los valores en listas para luego armar la tabla
    filas_tabla = []

    # Se agrega la primera linea
    y_n = y_inicial
    filas_tabla.append([t_inicial, np.nan, np.nan]) # no se guarda como valor aprox el valor inicial
    
    # Se calcula el resto de las filas, usando t_final+h para incluir el valor a aproximar. 
    for t in np.arange(t_inicial+h, t_final+0.5*h, h).round(4):
        # Calculo de y_n+1, valor aproximado
        k1 = f(t-h, y_n)
        k2 = f(t, y_n + h*k1)
        y_n_1 = y_n + (h/2) * (k1+k2)

        # Calculo del error local antes de reasignar y_n_1
        e_local = np.abs(y_n_1 - y_n)

        # Reasignación para próximo paso
        y_n = y_n_1
        
        # Agregamos los valores al conjunto de filas para la tabla
        filas_tabla.append([t, y_n_1, e_local])
    
    tabla_valores = pd.DataFrame(columns=['t','y_aprox','error_local'], data=filas_tabla)
    
    return tabla_valores

def runge_kutta_4(t_inicial, t_final, h, y_inicial, f):
    """
    Función que implementa el método de Runge-Kutta de cuarto orden
    :parametros t_inicial: float, valor inicial de t, t_final: float, valor final de t (valor a aproximar), h: float, tamaño del paso, y_inicial: float valor de y inicial para el primer paso, f: función derivada del PVI
    :return: DataFrame, tabla de valores de t, y_aprox y error_local
    """
    # Guardamos los valores en listas para luego armar la tabla
    filas_tabla = []

    # Se agrega la primera linea
    y_n = y_inicial
    filas_tabla.append([t_inicial, np.nan, np.nan])
    # print("valor de yinicial", y_inicial) PARA CONTROL
    
    # Se calcula el resto de las filas, usando t_final+h para incluir el valor a aproximar. 
    for t in np.arange(t_inicial+h, t_final+0.5*h, h).round(4):
        # Calculo de y_n+1, valor aproximado
        k1 = f(t-h, y_n)
        k2 = f(t-h+h/2, y_n + (h/2)*k1)
        k3 = f(t-h+h/2, y_n + (h/2)*k2)
        k4 = f(t-h+h, y_n + h*k3)
        # print("Valores de k1, k2, k3, k4", k1, k2, k3, k4, "calculados con", t-h, t-h+h/2, t-h+h/2, t-h+h, y_n) PARA CONTROL

        y_n_1 = y_n + (h/6)*(k1+2*k2+2*k3+k4)

        # Calculo del error local antes de reasignar y_n_1
        e_local = np.abs(y_n_1 - y_n)

        # Reasignación para próximo paso
        y_n = y_n_1

        # Agregamos los valores al conjunto de filas para la tabla
        filas_tabla.append([t, y_n_1, e_local])
    
    tabla_valores = pd.DataFrame(columns=['t','y_aprox','error_local'], data=filas_tabla)
    
    return tabla_valores

def adam_bashforth_2_con_euler_RK1_explicito(t_inicial, t_final, h, y_inicial, f):
    """
    Función que implementa el método de Adam-Bashforth 2, usando para el segundo paso inicial el método de Euler explícito (RK1)

    :parametros t_inicial: float, valor inicial de t, t_final: float, valor final de t (valor a aproximar), h: float, tamaño del paso, y_inicial: float, valor de y inicial para el primer paso inicial f: función derivada del PVI
    :return: DataFrame, tabla de valores de t, y_real, y_aprox, error_global y error_local
    """
    # Guardamos los valores en listas para luego armar la tabla
    filas_tabla = []

    # Se agrega la primera linea
    y_n_m1 = y_inicial
    filas_tabla.append([t_inicial, np.nan, np.nan])

    # Se agrega la segunda línea usando el método de Euler explícito (RK1) 
    y_n = y_n_m1 + h*f(t_inicial, y_n_m1) #aproximado con Euler explícito

    e_local = np.abs(y_n-y_n_m1)
    filas_tabla.append([t_inicial+h, y_n, e_local])

    # Se calcula el resto de las filas, usando t_final+h para incluir el valor a aproximar. Ahora se comienza desde el tercer paso (t_inicial+2*h)
    
    for t in np.arange(t_inicial+2*h, t_final+0.5*h, h).round(4):
        # Calculo del valor aproximado
        y_n_1 = y_n + (h/2)*(3*f(t-h, y_n) - f(t-2*h, y_n_m1))
        # print("calculado yaprox usando", y_n, y_n_m1, t-h, t-2*h, f(t-h, y_n), f(t-2*h, y_n_m1)) PARA CONTROL
        # Calculo del error local antes de reasignar 
        e_local = np.abs(y_n_1 - y_n)

        # Reasignación para próximo paso
        y_n_m1 = y_n
        y_n = y_n_1
        
        # Agregamos los valores al conjunto de filas para la tabla
        filas_tabla.append([t, y_n_1, e_local])
    
    tabla_valores = pd.DataFrame(columns=['t','y_aprox','error_local'], data=filas_tabla)
    
    return tabla_valores

def heun(t_inicial, t_final, h, y_inicial, f, eps, itmax):
    """
    Función que implementa el método de Heun predictor-corrector. Se usa como método predictor el método de Euler explícito (RK1) y como corrector el método de Euler modificado (RK2) o trapecio

    :parametros t_inicial: float, valor inicial de t, t_final: float, valor final de t (valor a aproximar), h: float, tamaño del paso, y_inicial: float valor de y inicial para el primer paso f: función derivada del PVI, eps: float, representa la tolerancia en cuanto al error, itmax: int, cantidad máxima de iteraciones que se aceptará
    :return: DataFrame, tabla de valores de t, y_real, y_aprox, error_global y error_local
    """
    # Guardamos los valores en listas para luego armar la tabla
    filas_tabla = []

    # Se agrega la primera linea
    y_n = y_inicial
    filas_tabla.append([t_inicial, np.nan, np.nan])

    # Se calcula el resto de las filas, usando t_final+h para incluir el valor a aproximar. 
    for t in np.arange(t_inicial+h, t_final+0.5*h, h).round(4):

        it = 0

        # Usamos el método predictor (Euler explícito RK1)
        y_n_1 = y_n + h*f(t-h, y_n)

        # Calculo del error local antes de aplicar el corrector
        e_local = np.abs(y_n_1 - y_n)

        # print("Del predictor resulta yaprox", y_n_1, "con error local", e_local, "calculado usando",y_n, t-h) PARA CONTROL
    
        while it <= itmax and e_local > eps:
            # Método corrector (Euler modificado RK2)
            aux_y_ant = y_n_1 # para calcular el error necesitamos almacenar el valor otorgado por el predictor en una primera iteración o por el corrector si se sigue iterando más.

            y_n_1 = y_n + (h/2)*(f(t-h, y_n) + f(t, y_n_1))
            e_local = np.abs(y_n_1 - aux_y_ant)
            # Notar que y_n sigue correspondiendo al valor del paso anterior ya que no hubo reasignación aún.

            # print("Paso ", t, " Iteración ", it, " Error local ", e_local, "valor corregido", y_n_1) PARA CONTROL

            it += 1

        # Calculo del error local definitivo del paso
        e_local = np.abs(y_n_1 - y_n)

        # Reasignacion
        y_n = y_n_1
        #print("el valor de y_n_1 resultante es ", y_n_1, "paso", t)
        
        # Agregamos los valores al conjunto de filas para la tabla
        filas_tabla.append([t,y_n_1, e_local])
    
    tabla_valores = pd.DataFrame(columns=['t','y_aprox','error_local'], data=filas_tabla)
    
    return tabla_valores

def resolver_con_scipy(metodo, dya, t_inicial, t_final, y_inicial, rtol=1e-3, atol=1e-6):
    """
    Función que resuelve una EDO usando métodos de scipy.integrate.solve_ivp
    
    :parametros metodo: str, nombre del método ('RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA')
                dya: función derivada del PVI
                t_inicial: float, valor inicial de t
                t_final: float, valor final de t
                y_inicial: float, valor inicial
                rtol: float, tolerancia relativa (por defecto 1e-3)
                atol: float, tolerancia absoluta (por defecto 1e-6)
    :return: DataFrame, tabla de valores de t, y_aprox y error_local
    """
    # Resolver usando scipy (sin especificar t_eval para que use el paso predefinido)
    limites_intervalo = (t_inicial, t_final)
    solucion = spi.solve_ivp(dya, limites_intervalo, [y_inicial], method=metodo, rtol=rtol, atol=atol)
    
    # Guardar valores en listas para armar la tabla
    filas_tabla = []
    
    for i in range(len(solucion.t)):
        t = solucion.t[i]
        y_aprox = solucion.y[0][i]
        
        # Calcular error local (diferencia con el paso anterior)
        if i == 0:
            e_local = np.nan
        else:
            e_local = np.abs(y_aprox - solucion.y[0][i-1])
        
        filas_tabla.append([t, y_aprox, e_local])
    
    tabla_valores = pd.DataFrame(columns=['t','y_aprox','error_local'], data=filas_tabla)
    
    return tabla_valores
