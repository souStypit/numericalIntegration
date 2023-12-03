# variant 1

import math
from funcs.trapezium import *
from funcs.gauss_2 import *


def f(x):
    return pow(1 + x, -1)


def main():
    a, b = 0, 1

    trapezium(f, a, b)
    gauss_2(f, a, b)


if __name__ == '__main__':
    main()
