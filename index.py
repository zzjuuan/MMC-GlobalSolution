# Importando bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Definindo funções.
def T(t):
    return 35 + (1 - np.exp(-t / 27)) + t * np.exp(-34.33 * t)

def e(x):
    return 5.47 + 1.85 * np.exp(-x) * np.cos(np.sqrt(8)*x - 19.47) + (x - 1.365) * np.exp(-34.33 * x)

# Definindo valores de intervalo.
t = np.linspace(0, 36, 1000)  # Tempo de 0 a 36 meses
x = np.linspace(0, 5, 1000)   # Velocidade de 0 a 5 m/s

# calculo dos valores
T_values = T(t)
e_values = e(x)

#Definindo mínimo e máximo de T(t) e de e(x)

peaks_T, _ = find_peaks(T_values)
valleys_T, _ = find_peaks(-T_values)

peaks_e, _ = find_peaks(e_values)
valleys_e, _ = find_peaks(-e_values)

#plot do gráfico da função T(t).

plt.figure(figsize=(10, 5))
plt.plot(t, T_values, label='T(t)')
plt.scatter(t[peaks_T], T_values[peaks_T], color='red', label='Máximos')
plt.scatter(t[valleys_T], T_values[valleys_T], color='blue', label='Mínimos')
plt.title('Temperatura T(t) - Onda de Calor')
plt.xlabel('Tempo (meses)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()
plt.show()

#plot do gráfico e(x).

plt.figure(figsize=(10, 5))
plt.plot(x, e_values, label='e(x)')
plt.scatter(x[peaks_e], e_values[peaks_e], color='red', label='Máximos')
plt.scatter(x[valleys_e], e_values[valleys_e], color='blue', label='Mínimos')
plt.title('Escala Richter e(x) - Movimentos Anômalos da Terra')
plt.xlabel('Velocidade (m/s)')
plt.ylabel('Magnitude (Richter)')
plt.grid(True)
plt.legend()
plt.show()