# variant 1

import math
from funcs.left_rectangle import *
from funcs.gauss_2 import *


def f(x):
    return pow(1 + pow(x, 3), -1)


def main():
    a, b = 0, 1

    left_rectangle(f, a, b)
    gauss_2(f, a, b)


if __name__ == '__main__':
    main()
