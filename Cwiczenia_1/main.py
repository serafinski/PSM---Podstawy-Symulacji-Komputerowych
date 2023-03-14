import math

wybor = input("Wprowadz: "
              "\n- 1 dla x w radianach"
              "\n- 2 dla x w stopniach"
              "\n\nWybór: ")

x = input("Wprowadź x: ")
print()


def taylor(wartosc, znak, potega):
    """
    It takes a value, a sign, and a power, and returns the Taylor series term for that value, sign, and power

    :param wartosc: the value of the function
    :param znak: the sign of the term, either +1 or -1
    :param potega: the power of the function
    :return: the value of the Taylor series.
    """
    return znak * (math.pow(wartosc, potega) / math.factorial(potega))


def konwersja(wartosc):
    """
    It takes a value and returns the value in the first quadrant

    :param wartosc: the value to be converted
    :return: the value of the angle in the first quadrant.
    """
    wartosc = float(wartosc)
    wartosc_znormalizowana = wartosc % (2 * math.pi)

    # między 0 a pi/2
    if 0 < wartosc_znormalizowana <= (math.pi / 2):
        return wartosc_znormalizowana

    # między pi/2 a pi
    elif (math.pi / 2) < wartosc_znormalizowana <= math.pi:
        return math.pi - wartosc_znormalizowana

    # między pi a 3/2pi
    elif math.pi < wartosc_znormalizowana <= (3 * (math.pi / 2)):
        return math.pi - wartosc_znormalizowana

    else:
        wartosc_znormalizowana = (2 * math.pi) - wartosc_znormalizowana
        return wartosc_znormalizowana - (2 * math.pi)


def wartosc_sin(wartosc):
    """
    It calculates the value of sin(x) using the Taylor series

    :param wartosc: the value of the angle in radians
    :return: The value of the sin function.
    """
    wartosc = konwersja(wartosc)

    suma = wartosc
    znak = -1.0
    potega = 3

    for value in range(1, 11):
        suma += taylor(wartosc, znak, potega)

        znak = znak * -1
        potega += 2

    return suma


def stopnie():
    """
    It takes a value in degrees, converts it to radians, calculates the sine of the value using the math library and the
    sine function from the previous exercise, and prints the results
    """
    radian = math.radians(float(x))
    sin_z_biblioteki = math.sin(radian)
    print("Biblioteka: " + str(sin_z_biblioteki))
    print("Ręcznie: " + str(wartosc_sin(radian)))
    print("Róznica: " + str(math.fabs(wartosc_sin(radian)-sin_z_biblioteki)))

def radiany():
    """
    It calculates the sine of a given angle in radians
    """
    sin_z_biblioteki = math.sin(float(x))
    print("Biblioteka: " + str(sin_z_biblioteki))
    print("Ręcznie: " + str(wartosc_sin(x)))
    print("Róznica: " + str(math.fabs(wartosc_sin(x)-sin_z_biblioteki)))


if int(wybor) == 1:
    radiany()
elif int(wybor) == 2:
    stopnie()
else:
    print("Nie wprowadzono prawidłowej opcji - spróbuj ponownie!")
