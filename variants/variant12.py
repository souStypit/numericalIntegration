# variant 1

import math
from funcs.left_rectangle import *
from funcs.simpson import *


def f(x):
    return math.sin(x ** 2)


def main():
    a, b = math.pi / 4, math.pi / 2

    left_rectangle(f, a, b)
    simpson(f, a, b)


if __name__ == '__main__':
    main()
