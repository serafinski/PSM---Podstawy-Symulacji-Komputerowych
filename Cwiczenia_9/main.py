import numpy as np
import matplotlib.pyplot as plt

# Parametry wejściowe
A = 10
B = 25
C = 8 / 3

# Różne delty, bo dla 0,03 nie widać nic sensownego dla Eulera
dt = 0.03
dt_euler = 0.02

# Początek
czas_start = 0
# Koniec
czas_koniec = 100

# Od jakich wartości x, y, z zaczynamy
wartosci_poczatkowe = np.array([1, 1, 1])


# Funkcja licząca podany układ równań z zadania
def uklad_rownan(tablica):
    # Pobieramy wartości z tablicy wejściowej
    x, y, z = tablica
    # Liczymy
    dx_dt = A * (y - x)
    dy_dt = -x * z + B * x - y
    dz_dt = x * y - C * z
    # Zwracamy
    return np.array([dx_dt, dy_dt, dz_dt])


# Euler
def euler(f, wartosci_poczatkowe, dt, start, koniec):
    # Tablica na punkty czasowe
    czas = np.arange(start, koniec, dt)
    # Tworzymy tablicę, do której będą dodawane policzone wartości
    tablica_wyjsciowa = np.zeros((len(czas), len(wartosci_poczatkowe)))
    # Inicjalizacja tablicy wyjściowej — wartościami tablic początkowych
    tablica_wyjsciowa[0] = wartosci_poczatkowe

    # Faktyczny Euler
    for i in range(1, len(czas)):
        tablica_wyjsciowa[i] = tablica_wyjsciowa[i - 1] + dt * f(tablica_wyjsciowa[i - 1])
    return czas, tablica_wyjsciowa


# Midpoint
def midpoint(f, wartosci_poczatkowe, dt, start, koniec):
    # Tablica na punkty czasowe
    czas = np.arange(start, koniec, dt)
    # Tworzymy tablicę, do której będą dodawane policzone wartości
    tablica_wyjsciowa = np.zeros((len(czas), len(wartosci_poczatkowe)))
    # Inicjalizacja tablicy wyjściowej — wartościami tablic początkowych
    tablica_wyjsciowa[0] = wartosci_poczatkowe

    # Faktyczny Midpoint
    for i in range(1, len(czas)):
        k1 = dt * f(tablica_wyjsciowa[i - 1])
        k2 = dt * f(tablica_wyjsciowa[i - 1] + 0.5 * k1)
        tablica_wyjsciowa[i] = tablica_wyjsciowa[i - 1] + k2
    return czas, tablica_wyjsciowa


# RK4
def rk4(f, wartosci_poczatkowe, dt, start, koniec):
    # Tablica na punkty czasowe
    czas = np.arange(start, koniec, dt)
    # Tworzymy tablicę, do której będą dodawane policzone wartości
    tablica_wyjsciowa = np.zeros((len(czas), len(wartosci_poczatkowe)))
    # Inicjalizacja tablicy wyjściowej — wartościami tablic początkowych
    tablica_wyjsciowa[0] = wartosci_poczatkowe

    # Faktyczny RK4
    for i in range(1, len(czas)):
        k1 = dt * f(tablica_wyjsciowa[i - 1])
        k2 = dt * f(tablica_wyjsciowa[i - 1] + 0.5 * k1)
        k3 = dt * f(tablica_wyjsciowa[i - 1] + 0.5 * k2)
        k4 = dt * f(tablica_wyjsciowa[i - 1] + k3)
        tablica_wyjsciowa[i] = tablica_wyjsciowa[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return czas, tablica_wyjsciowa


# Zwrotka czasu i tablic wynikowych w celu zrobienia wykresów
t_euler, wyjsciowa_euler = euler(uklad_rownan, wartosci_poczatkowe, dt_euler, czas_start, czas_koniec)
t_midpoint, wyjsciowa_midpoint = midpoint(uklad_rownan, wartosci_poczatkowe, dt, czas_start, czas_koniec)
t_rk4, wyjsciowa_rk4 = rk4(uklad_rownan, wartosci_poczatkowe, dt, czas_start, czas_koniec)

# Euler Wykres
plt.figure(figsize=(8, 6))
plt.plot(wyjsciowa_euler[:, 0], wyjsciowa_euler[:, 2], label="Euler", alpha=0.7)
plt.xlabel("x")
plt.ylabel("z")
plt.legend()
plt.title("Euler")
plt.grid(True)
plt.show()

# Midpoint Wykres
plt.figure(figsize=(8, 6))
plt.plot(wyjsciowa_midpoint[:, 0], wyjsciowa_midpoint[:, 2], label="Midpoint", alpha=0.7)
plt.xlabel("x")
plt.ylabel("z")
plt.legend()
plt.title("Midpoint")
plt.grid(True)
plt.show()

# RK4 Wykres
plt.figure(figsize=(8, 6))
plt.plot(wyjsciowa_rk4[:, 0], wyjsciowa_rk4[:, 2], label="RK4", alpha=0.7)
plt.xlabel("x")
plt.ylabel("z")
plt.legend()
plt.title("RK4")
plt.grid(True)
plt.show()
