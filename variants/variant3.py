# variant 1

import math
from funcs.right_rectangle import *
from funcs.gauss_3 import *


def f(x):
    return math.sin(x) / (1 + pow(x, 2))


def main():
    a, b = 0, 0.5

    right_rectangle(f, a, b)
    gauss_3(f, a, b)


if __name__ == '__main__':
    main()
