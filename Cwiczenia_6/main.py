import math
import numpy as np

l = math.pi
n = 10
dx = l / n
dt = 0.2
x = []
i = []
y = []
v = []

ep = []
ek = []


def init_i():
    for var in range(11):
        i.append(var)


def init_x():
    for var in i:
        tmp = dx * var
        x.append(tmp)


def init_y():
    for var in x:
        tmp = math.sin(var) / 1000
        y.append(tmp)


def init_v():
    tmp = np.zeros(10)
    v.extend(tmp)


def count_ep(array):
    array = np.array(array)
    tmp = 0
    for var in range(1, len(array)):
        tmp += (array[var] - array[var - 1]) ** 2

    final = 1 / (2 * dx) * tmp

    ep.append(final)


def count_ek(array):
    array = np.array(array)
    tmp = 0
    for var in range(1, len(array)):
        tmp += array[var] ** 2

    final = dx / 2 * tmp

    ek.append(final)


if __name__ == "__main__":
    init_i()
    init_x()
    init_y()
    init_v()

    count_ep(y)
    count_ek(v)
    print(ek)
