import numpy as np
import matplotlib.pyplot as plt

l = np.pi  # długość obszaru
n = 10  # liczba punktów siatki
dx = l / n  # odstęp między punktami siatki
dt = 0.2  # krok czasowy
liczba_krokow = 50  # liczba kroków czasowych

# inicjalizacja pozycji
pozycje = np.zeros(n + 1)
for i in range(n + 1):
    pozycje[i] = np.sin(i * dx)

# inicjalizacja prędkości
predkosci = np.zeros(n + 1)

# listy energii
ek = []
ep = []
ec = []


# Funkcja wyliczająca przyspieszenie na podstawie pozycji
def wylicz_przyspieszenie(pozycje, dx):
    przyspieszenie = np.zeros(n + 1)
    for i in range(1, n):
        przyspieszenie[i] = (pozycje[i - 1] - 2 * pozycje[i] + pozycje[i + 1]) / dx ** 2
    return przyspieszenie


# Funkcja wykonująca jeden krok symulacji
def krok(pozycje, predkosci, przyspieszenia, dt, dx):
    polowa_predkosci = np.zeros(n + 1)
    for i in range(n + 1):
        polowa_predkosci[i] = predkosci[i] + 0.5 * przyspieszenia[i] * dt
    nowe_pozycje = np.zeros(n + 1)
    for i in range(n + 1):
        nowe_pozycje[i] = pozycje[i] + polowa_predkosci[i] * dt
    nowe_przyspieszenia = wylicz_przyspieszenie(nowe_pozycje, dx)
    nowe_predkosci = np.zeros(n + 1)
    for i in range(n + 1):
        nowe_predkosci[i] = polowa_predkosci[i] + 0.5 * nowe_przyspieszenia[i] * dt
    return nowe_pozycje, nowe_predkosci, nowe_przyspieszenia


# Funkcja wyliczająca energie na podstawie pozycji i prędkości
def wylicz_energie(pozycje, przyspieszenia, dx):
    ek = 0.0
    ep = 0.0
    for i in range(1, n):
        ek += 0.5 * dx * przyspieszenia[i] ** 2
        ep += 0.5 * (pozycje[i + 1] - pozycje[i]) ** 2 / dx
    return ek, ep


przyspieszenie = wylicz_przyspieszenie(pozycje, dx)

# SYMULACJA
for i in range(liczba_krokow):
    pozycje, predkosci, przyspieszenie = krok(pozycje, predkosci, przyspieszenie, dt, dx)
    en_kin, en_pot = wylicz_energie(pozycje, predkosci, dx)
    en_cal = en_kin + en_pot

    ek.append(en_kin)
    ep.append(en_pot)
    ec.append(en_cal)

print(ek)
print(ep)
print(ec)

# WYKRES
plt.plot(ek, label='Energia Kinetyczna')
plt.plot(ep, label='Energia Potencjalna')
plt.plot(ec, label='Energia całkowita')
plt.legend()
plt.xlabel('Czas (w krokach)')
plt.ylabel('Energia')
plt.show()
