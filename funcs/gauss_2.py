from common import *
from math import sqrt


def gauss_2(f, a, b):
    def integrate(n):
        h = ((b - a) / (2 * n))
        root = h / sqrt(3)
        sum1 = 0

        for k in range(1, n + 1):
            sum1 += f(a + (2 * k - 1) * h - root)
            sum1 += f(a + (2 * k - 1) * h + root)

        return sum1 * h

    results = cycle_function(integrate)
    print_res('gauss_2:', *results)
