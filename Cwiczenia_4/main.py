import math

import numpy as np
import matplotlib.pyplot as plt

# SFERA

# Masa
m_sfery = 1
# Promień
r_sfery = 2
# Moment bezwładności wokół osi obrotu
ik_sfery = 2 / 3 * m_sfery * r_sfery ** 2
# Prędkość kątowa sfery wokół jej osi obrotu
w_sfery = 0
# Kąt obrotu kuli wokół jej osi obrotu
gamma_sfery = 0

# KULA

# Masa
m_kuli = 1
# Promień
r_kuli = 2
# Moment bezwładności wokół osi obrotu
ik_kuli = 2 / 5 * m_kuli * r_kuli ** 2
# Prędkość kątowa kuli wokół jej osi obrotu
w_kuli = 0
# Kąt obrotu kuli wokół jej osi obrotu
gamma_kuli = 0

# INNE ZMIENNE

# Kąt nachylenia pochylni
alfa = np.deg2rad(45)  # angle of inclination of the incline in radians
# Wysokość pochylni
h = 20
# Grawitacja
g = 10
# Położenie sfery wzdłuż pochylni
sx_sfery = 0
# Prędkość sfery wzdłuż pochylni
v_sfery = 0
# Położenie kuli wzdłuż pochylni
sx_kuli = 0
# Prędkość kuli wzdłuż pochylni
v_kuli = 0

# Wysokość obiektów nad ziemią (2, bo tyle samo co promień)
sy = 2
# Start czasu
t = 0  # current time in s
# Krok czasu
dt = 0.1
# Koniec czasu
t_max = 5
# Liczba kroków
n = int(t_max / dt)

# ZMIENNE POMOCNICZE
b_start_sfery = 0
b_start_kuli = 0

# Tablice do zapisywania
czasy = np.zeros(n)
wartosci_Sx_sfera = np.zeros(n)
wartosci_Sx_kula = np.zeros(n)
wartosci_Sy_sfera = np.zeros(n)  # added line
wartosci_Sy_kula = np.zeros(n)  # added line
wartosci_gamma_sfera = np.zeros(n)
wartosci_gamma_kula = np.zeros(n)


def ruch_liniowy(ik, m, r, v, sx):
    # Przyspieszenie obiektu wzdłuż pochylni
    acc = g * np.sin(alfa) / (1 + ik / (m * r ** 2))

    # prędkość obiektu prostopadłego do pochylni
    vd = acc * dt / 2
    # Zmiana położenia obiektu wzdłuż pochylni podczas jednego kroku czasowego
    dSx = (v + vd) * dt

    # Zmiana prędkości obiektu wzdłuż pochylni podczas jednego kroku czasowego
    dV = acc * dt

    sx += dSx
    v += dV

    # Wysokość obiektu nad ziemią
    sy = r
    return sx, v, sy, acc


def ruch_rotacyjny(r, w, acc, b_start):
    # Przyspieszenie kątowe obiektu wokół jego osi obrotu
    eps = acc / r

    # Zmiana prędkości kątowej obiektu w jednym kroku czasowym
    dw = eps * dt

    # Zmiana kąta pomiędzy wektorem prędkości a pochylnią podczas jednego kroku czasowego
    db = (w + dw / 2) * dt

    # Kąt pomiędzy wektorem prędkości a pochyleniem
    b = b_start + db

    # Kąt obrotu obiektu wokół jego osi obrotu
    gamma = math.pi / 2 - b

    # Prędkość kątowa obiektu wokół jego osi obrotu
    w += dw

    return gamma, w, db, b


# Midpoint
for i in range(n):
    # Ruch sfera
    sx_sfery, v_sfery, sy, acc_sfery = ruch_liniowy(ik_sfery, m_sfery, r_sfery, v_sfery, sx_sfery)
    gamma_sfery, w_sfery, db_sfery, b_start_sfery = ruch_rotacyjny(r_sfery, w_sfery, acc_sfery, b_start_sfery)

    # Ruch kula
    sx_kuli, v_kuli, sy_kuli, acc_kuli = ruch_liniowy(ik_kuli, m_kuli, r_kuli, v_kuli, sx_kuli)
    gamma_kuli, w_kuli, db_kuli, b_start_kuli = ruch_rotacyjny(r_kuli, w_kuli, acc_kuli, b_start_kuli)

    # Zapisywanie wyników
    czasy[i] = t
    wartosci_Sx_sfera[i] = sx_sfery
    wartosci_Sx_kula[i] = sx_kuli
    wartosci_Sy_sfera[i] = sy
    wartosci_Sy_kula[i] = sy_kuli
    wartosci_gamma_sfera[i] = gamma_sfery
    wartosci_gamma_kula[i] = gamma_kuli

    # Update czasu
    t += dt

# WYKRESY

fig, axs = plt.subplots(2, 2)

# SFERA
axs[0, 0].plot(czasy, wartosci_Sx_sfera)
axs[0, 0].set_xlabel('Czas (s)')
axs[0, 0].set_ylabel('sx Sfera (m)')
axs[0, 0].set_title('Ruch liniowy sfery (sx)')

axs[1, 0].plot(czasy, wartosci_Sy_sfera)
axs[1, 0].set_xlabel('Czas (s)')
axs[1, 0].set_ylabel('sy Sfera (m)')
axs[1, 0].set_title('Ruch liniowy sfery (sy)')

# KULA
axs[0, 1].plot(czasy, wartosci_Sx_kula)
axs[0, 1].set_xlabel('Czas (s)')
axs[0, 1].set_ylabel('sx Kula (m)')
axs[0, 1].set_title('Ruch liniowy kula (sx)')

axs[1, 1].plot(czasy, wartosci_Sy_kula)
axs[1, 1].set_xlabel('Czas (s)')
axs[1, 1].set_ylabel('sy Kula (m)')
axs[1, 1].set_title('Ruch liniowy kula(sy)')

fig.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()