from common import *
from math import sqrt


def gauss_3(f, a, b):
    def integrate(n):
        h = ((b - a) / (2 * n))
        root = sqrt(0.6)
        sum1 = 0

        for k in range(1, n + 1):
            sum1 += (5 / 9) * f(a + (2 * k - 1) * h - root * h)
            sum1 += (5 / 9) * f(a + (2 * k - 1) * h + root * h)
            sum1 += (8 / 9) * f(a + (2 * k - 1) * h)

        return sum1 * h

    results = cycle_function(integrate)
    print_res('gauss_3:', *results)
