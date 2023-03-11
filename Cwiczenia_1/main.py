import math

wybor = input("Wprowadz: "
              "\n- 1 dla x w radianach"
              "\n- 2 dla x w stopniach"
              "\n\nWybór: ")

x = input("Wprowadź x: ")
print()


# zapewnienie, że wartość zawsze mieści się w granicy 0-2pi (360 stopniach)
def zapewnienie_wartosci(modulo_radian):
    modulo_radian = float(modulo_radian)
    if modulo_radian > 0:
        return modulo_radian
    else:
        return modulo_radian + (2 * math.pi)


def konwersja_kata(kat):
    # wprowadzamy kąt
    kat = float(kat)
    # zamiana na radiany
    kat %= (2 * math.pi)

    return zapewnienie_wartosci(kat)


def konwersja_do_pierwszej_cwiartki(radian):
    # między 0 a pi/2
    radian = float(radian)
    if radian > 0 and radian <= (math.pi / 2):
        return radian
    # między pi/2 a pi
    elif radian > (math.pi / 2) and radian <= math.pi:
        radian = math.pi - radian
        return radian
    # między pi a 3/2pi
    elif radian > math.pi and radian <= (3 * (math.pi / 2)):
        radian = radian - math.pi
        return radian
    else:
        radian = (2 * math.pi) - radian
        return radian


def sin_kat():
    kat = float(x)
    radian = konwersja_kata(kat)
    radian = konwersja_do_pierwszej_cwiartki(radian)

    suma = 0
    potega_przez_silnie = 1

    # wyliczenie z biblioteki
    sin_biblioteka = math.sin(radian)

    for wyraz_szeregu in range(1, 11):
        #
        potega_przez_silnie = potega_przez_silnie * (radian / wyraz_szeregu)

        # pozytywny wierzchołek sin'usa
        if wyraz_szeregu % 4 == 1:
            suma = suma + potega_przez_silnie

        # negatywny wierzchołek sin'usa
        if wyraz_szeregu % 4 == 3:
            suma = suma - potega_przez_silnie

    print(math.sin(float(x)))
    print("Wynik sin(x) = " + str(suma))
    blad = (math.fabs(suma) - math.fabs(sin_biblioteka))
    print("Błąd sin(x) = " + str(blad))
    print()


def sin_rad():
    radian = zapewnienie_wartosci(x)
    radian = konwersja_do_pierwszej_cwiartki(radian)

    suma = 0
    potega_przez_silnie = 1

    # wyliczenie z biblioteki
    sin_biblioteka = math.sin(radian)

    for wyraz_szeregu in range(1, 11):
        #
        potega_przez_silnie = potega_przez_silnie * (radian / wyraz_szeregu)

        # pozytywny wierzchołek sin'usa
        if wyraz_szeregu % 4 == 1:
            suma = suma + potega_przez_silnie

        # negatywny wierzchołek sin'usa
        if wyraz_szeregu % 4 == 3:
            suma = suma - potega_przez_silnie

    print("Wynik sin(x) = " + str(suma))
    blad = (math.fabs(suma) - math.fabs(sin_biblioteka))
    print("Błąd sin(x) = " + str(blad))
    print()


if int(wybor) == 1:
    sin_rad()
elif int(wybor) == 2:
    sin_kat()
else:
    print("Nie wprowadzono prawidłowej opcji - spróbuj ponownie!")
