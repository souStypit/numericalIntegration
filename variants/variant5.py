# variant 1

import math
from funcs.half_rectangle import *
from funcs.gauss_2 import *


def f(x):
    return math.sin(x ** 2)


def main():
    a, b = 0, math.pi / 4

    half_rectangle(f, a, b)
    gauss_2(f, a, b)


if __name__ == '__main__':
    main()
