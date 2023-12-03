# variant 1

import math
from funcs.half_rectangle import *
from funcs.gauss_3 import *


def f(x):
    return math.log(1 + x, math.e) / (1 + x ** 3)


def main():
    a, b = 0, 1

    half_rectangle(f, a, b)
    gauss_3(f, a, b)


if __name__ == '__main__':
    main()
