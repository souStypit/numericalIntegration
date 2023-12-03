# variant 11

import math
from funcs.right_rectangle import *
from funcs.gauss_2 import *


def f(x):
    return math.sin(x) / (x - 1)


def main():
    a, b = math.pi / 2, math.pi

    right_rectangle(f, a, b)
    gauss_2(f, a, b)


if __name__ == '__main__':
    main()
