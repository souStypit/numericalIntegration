# variant 1

import math
from funcs.left_rectangle import *
from funcs.gauss_3 import *


def f(x):
    return pow(1 + pow(x, 2), -1)


def main():
    a, b = 0, 1

    left_rectangle(f, a, b)
    gauss_3(f, a, b)


if __name__ == '__main__':
    main()
