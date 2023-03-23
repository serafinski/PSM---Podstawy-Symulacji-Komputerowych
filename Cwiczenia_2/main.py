from typing import List
import pandas as pd
import matplotlib.pyplot as plt

podstawowy_koordynat_x_list = []
podstawowy_koordynat_y_list = []

zaawansowany_koordynat_x_list = []
zaawansowany_koordynat_y_list = []


class Euler:

    # KONSTRUKTOR
    def __init__(self, koordynat_x: float,
                 koordynat_y: float,
                 predkosc_x: float,
                 predkosc_pionowa_y: float,
                 przyspieszenie_x: float,
                 przyspieszenie_y: float,
                 zmiana_pozycja_x: float,
                 zmiana_pozycja_y: float,
                 zmiana_predkosc_x: float,
                 zmiana_predkosc_y: float,
                 czas: int):
        # kolejność ustawienia self będzie miała znaczenie na kolejność wypisywania kolumn
        self.czas = czas
        self.koordynat_x = koordynat_x
        self.koordynat_y = koordynat_y
        self.predkosc_x = predkosc_x
        self.predkosc_pionowa_y = predkosc_pionowa_y
        self.przyspieszenie_x = przyspieszenie_x
        self.przyspieszenie_y = przyspieszenie_y
        self.zmiana_pozycja_x = zmiana_pozycja_x
        self.zmiana_pozycja_y = zmiana_pozycja_y
        self.zmiana_predkosc_x = zmiana_predkosc_x
        self.zmiana_predkosc_y = zmiana_predkosc_y


def podstawowyeuler(pochodna_czasu, grawitacja_x, grawitacja_pionowa_y, masa, opor_osrodka, czas):
    # LISTA
    euler: List[Euler] = []

    # PODSTAWOWY EULER
    koordynat_x_basic = 0
    koordynat_y_basic = 0
    predkosc_x_basic = 10
    predkosc_pionowa_y_basic = 10
    zmiana_pozycja_x_basic = pochodna_czasu * predkosc_x_basic
    zmiana_pozycja_y_basic = pochodna_czasu * predkosc_pionowa_y_basic

    for i in range(0, 200, int(pochodna_czasu * 100)):
        podstawowy_koordynat_x_list.append(koordynat_x_basic)
        podstawowy_koordynat_y_list.append(koordynat_y_basic)
        koordynat_x_basic += zmiana_pozycja_x_basic
        koordynat_y_basic += zmiana_pozycja_y_basic
        przyspieszenie_x_basic = (masa * grawitacja_x - opor_osrodka * predkosc_x_basic) / masa
        przyspieszenie_y_basic = (masa * grawitacja_pionowa_y - opor_osrodka * predkosc_pionowa_y_basic) / masa
        zmiana_pozycja_x_basic = pochodna_czasu * predkosc_x_basic
        zmiana_pozycja_y_basic = pochodna_czasu * predkosc_pionowa_y_basic
        zmiana_predkosc_x_basic = pochodna_czasu * przyspieszenie_x_basic
        zmiana_predkosc_y_basic = pochodna_czasu * przyspieszenie_y_basic
        predkosc_x_basic += zmiana_predkosc_x_basic
        predkosc_pionowa_y_basic += zmiana_predkosc_y_basic

        euler.append(
            Euler(koordynat_x_basic,
                  koordynat_y_basic,
                  predkosc_x_basic,
                  predkosc_pionowa_y_basic,
                  przyspieszenie_x_basic,
                  przyspieszenie_y_basic,
                  zmiana_pozycja_x_basic,
                  zmiana_pozycja_y_basic,
                  zmiana_predkosc_x_basic,
                  zmiana_predkosc_y_basic,
                  czas))

        czas += 1

    # KONWERSJA NA SŁOWNIK DATAFRAME
    df_podstawowyeuler = pd.DataFrame([e.__dict__ for e in euler])
    print(df_podstawowyeuler.to_string(index=False))


# BRAK MASY I OPORU OŚRODKA
def ulepszonyeuler(pochodna_czasu, grawitacja_x, grawitacja_pionowa_y, czas):
    # LISTA
    ulepszony_euler: List[Euler] = []

    # ZAAWANSOWANY EULER
    koordynat_x_ulepszony = 0
    koordynat_y_ulepszony = 0
    predkosc_x_ulepszony = 10
    predkosc_y_ulepszony = 10

    przyspieszenie_x_ulepszony = grawitacja_x
    przyspieszenie_y_ulepszony = grawitacja_pionowa_y
    predkosc_x_ulepszony_polowa = pochodna_czasu * przyspieszenie_x_ulepszony / 2 + predkosc_x_ulepszony
    predkosc_y_ulepszony_polowa = pochodna_czasu * przyspieszenie_y_ulepszony / 2 + predkosc_y_ulepszony
    zmiana_predkosc_x_ulepszony = grawitacja_x * pochodna_czasu
    zmiana_predkosc_y_ulepszony = grawitacja_pionowa_y * pochodna_czasu
    zmiana_pozycja_x_ulepszony = predkosc_x_ulepszony_polowa * pochodna_czasu
    zmiana_pozycja_y_ulepszony = predkosc_y_ulepszony_polowa * pochodna_czasu

    for i in range(0, 200, int(pochodna_czasu * 100)):
        zaawansowany_koordynat_x_list.append(koordynat_x_ulepszony)
        zaawansowany_koordynat_y_list.append(koordynat_y_ulepszony)
        koordynat_x_ulepszony += zmiana_pozycja_x_ulepszony
        koordynat_y_ulepszony += zmiana_pozycja_y_ulepszony
        predkosc_x_ulepszony += zmiana_predkosc_x_ulepszony
        predkosc_y_ulepszony += zmiana_predkosc_y_ulepszony
        przyspieszenie_x_ulepszony = grawitacja_x
        przyspieszenie_y_ulepszony = grawitacja_pionowa_y

        # POŁOWA
        predkosc_x_ulepszony_polowa = pochodna_czasu * przyspieszenie_x_ulepszony / 2 + predkosc_x_ulepszony
        predkosc_y_ulepszony_polowa = pochodna_czasu * przyspieszenie_y_ulepszony / 2 + predkosc_y_ulepszony
        zmiana_predkosc_x_ulepszony = grawitacja_x * pochodna_czasu
        zmiana_predkosc_y_ulepszony = grawitacja_pionowa_y * pochodna_czasu
        zmiana_pozycja_x_ulepszony = predkosc_x_ulepszony_polowa * pochodna_czasu
        zmiana_pozycja_y_ulepszony = predkosc_y_ulepszony_polowa * pochodna_czasu

        ulepszony_euler.append(
            Euler(koordynat_x_ulepszony,
                  koordynat_y_ulepszony,
                  predkosc_x_ulepszony,
                  predkosc_y_ulepszony,
                  przyspieszenie_x_ulepszony,
                  przyspieszenie_y_ulepszony,
                  zmiana_pozycja_x_ulepszony,
                  zmiana_pozycja_y_ulepszony,
                  zmiana_predkosc_x_ulepszony,
                  zmiana_predkosc_y_ulepszony,
                  czas))
        czas += 1

    # KONWERSJA NA SŁOWNIK DATAFRAME
    df_ulepszonyeuler = pd.DataFrame([e.__dict__ for e in ulepszony_euler])
    print(df_ulepszonyeuler.to_string(index=False))


if __name__ == '__main__':
    # ZMIENNE
    pochodna = float(input("Wprowadź pochodną czasu: "))  # 0.01
    grav_x = float(input("Wprowadź grawitacje w kierunku horyzontalnym: "))  # 0
    grav_y = float(input("Wprowadź grawitacje w kierunku wertykalnym: "))  # -10
    mass = float(input("Wprowadź masę cząsteczki: "))  # 1
    opor = float(input("Wprowadź współczynnik oporu ośrodka w przedziale od 0 do 1: "))  # 0.2
    print()
    time = 1

    print("Podstawowy")
    podstawowyeuler(pochodna, grav_x, grav_y, mass, opor, time)
    print()
    print("Zaawansowany")
    ulepszonyeuler(pochodna, grav_x, grav_y, time)

    plt.plot(podstawowy_koordynat_x_list, podstawowy_koordynat_y_list, label="Podstawowy")
    plt.plot(zaawansowany_koordynat_x_list, zaawansowany_koordynat_y_list, label="Zaawansowany")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("dt: " + str(pochodna) +
              "; gx: " + str(grav_x) +
              "; gy: " + str(grav_y) +
              "; mass: " + str(mass) +
              "; k: " + str(opor))
    plt.legend()
    plt.show()
