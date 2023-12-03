# variant 1

import math
from funcs.half_rectangle import *
from funcs.simpson import *


def f(x):
    return math.exp(-pow(x, 2))


def main():
    a, b = 0, 2

    half_rectangle(f, a, b)
    simpson(f, a, b)


if __name__ == '__main__':
    main()
