import math

x = input("Wprowadź x: ")
print()


def biblioteka_sin(wyraz_szeregu):
    liczba_licznik = math.pow(math.pi, wyraz_szeregu)
    znak = math.pow(-1, wyraz_szeregu)
    licznik = znak * liczba_licznik
    mianownik = math.factorial(wyraz_szeregu)
    ulamek = licznik / mianownik
    suma = math.fabs(math.pi * ulamek)

    return print(suma)


def blad(liczba):
    cos = liczba + 1

def wlasny_sin():
    suma = 0.0

    # iterujemy biorąc pod uwagę pierwsze 10 wyrazów szeregu
    for wyraz_szeregu in range(0, 11):
        nieparzysta_liczba = (2 * wyraz_szeregu) + 1
        liczba_licznik = math.pow(int(x), nieparzysta_liczba)
        znak = math.pow(-1, wyraz_szeregu)
        licznik = znak * liczba_licznik
        mianownik = math.factorial(nieparzysta_liczba)
        ulamek = licznik / mianownik
        suma += ulamek

        # DEBUG
        # print("Wykonanie: " + str(wyraz_szeregu))
        # print()
        # print("Nieparzysta liczba: " + str(nieparzysta_liczba))
        # print("Licznik: " + str(licznik))
        # print("Mianownik: " + str(mianownik))
        # print("Ułamek: " + str(ulamek))
        # print(suma)
        # print()
    return print("Wynik sin(x) = " + str(suma) + "\n"
                                                 "Błąd sin(x) = ")


biblioteka_sin(9)
wlasny_sin()
