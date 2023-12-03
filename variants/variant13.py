# variant 1

import math
from funcs.simpson import *


def f(x):
    return pow(1 + pow(x, 3), -1)


def main():
    a, b = 0.5, 1.5

    simpson(f, a, b)


if __name__ == '__main__':
    main()
