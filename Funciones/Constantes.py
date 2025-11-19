import numpy as np
# ==================== CONSTANTES DEL PROBLEMA ====================
# Vida media del Carbono-14
T_HALF = 5730.0  # años

# Constante de desintegración radiactiva
LAMBDA = np.log(2) / T_HALF  # año^-1

# Porcentaje de C14 remanente (14.5% = 85.5% desintegrado)
R_REMANENTE = 0.145

# Condición inicial (100% de C14)
y0 = 1.0 #La concentración de C14 en el tiempo t=0 (al morir el organismo) se toma como 100%.

T_INICIAL = 0 # años
T_FINAL = int(-np.log(R_REMANENTE) / LAMBDA)  # Pues sabemos que la concentración final es el 14.5%, despejando t en la fórmula de desintegración radiactiva (años)

# Valores de h para pruebas con distintos tamaños de paso
VALORES_H = [5000, 3000, 1000, 100, 10]
