# variant 1

import math
from funcs.trapezium import *
from funcs.simpson import *


def f(x):
    return math.sin(x) / x


def main():
    a, b = math.pi / 4, math.pi / 2

    trapezium(f, a, b)
    simpson(f, a, b)


if __name__ == '__main__':
    main()
