# variant 1

import math
from funcs.trapezium import *
from funcs.gauss_3 import *


def f(x):
    return math.cos(x ** 2)


def main():
    a, b = 0, math.pi / 4

    trapezium(f, a, b)
    gauss_3(f, a, b)


if __name__ == '__main__':
    main()
