# variant 1

import math
from funcs.right_rectangle import *
from funcs.simpson import *


def f(x):
    return math.log(1 + x, math.e) / (1 + x ** 3)


def main():
    a, b = 0, 1

    right_rectangle(f, a, b)
    simpson(f, a, b)


if __name__ == '__main__':
    main()
