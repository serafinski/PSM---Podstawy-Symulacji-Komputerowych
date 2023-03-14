# Tomasz Serafiński s24535 - Grupa 12c

# ZADANIE 1
import math

a = input("Wprowadź a: ")
b = input("Wprowadź b: ")
c = input("Wprowadź c: ")


def delta(a, b, c):
    rownanie = math.pow(float(b), 2) - 4 * float(a) * float(c)

    print(rownanie)

    if rownanie > 0:
        return print("Delta większa od 0")
    else:
        return print("Delta mniejsza od 0")


delta(a, b, c)

# ZADANIE 2
liczba1 = input("Wprowadź liczbę w systemie dwójkowym: ")
liczba2 = input("Wprowadź liczbę w systemie ósemkowym: ")
liczba3 = input("Wprowadź liczbę w systemie szesnastkowym: ")


def konwersja(liczba1, liczba2, liczba3):
    print("Liczba w systemie dwójkowym zapisana w systemie dziesiętnym: " + str(int(liczba1, 2)))
    print("Liczba w systemie ósemkowym zapisana w systemie dziesiętnym: " + str(int(liczba2, 8)))
    print("Liczba w systemie szesnastkowym zapisana w systemie dziesiętnym: " + str(int(liczba3, 16)))


konwersja(liczba1, liczba2, liczba3)