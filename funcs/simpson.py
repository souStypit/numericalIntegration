from common import *


def simpson(f, a, b):
    def integrate(n):
        h = ((b - a) / (2 * n))
        sum1, sum2 = 0, 0

        for k in range(1, n + 1):
            sum1 += f(a + (2 * k - 1) * h)
        for k in range(1, n):
            sum2 += f(a + 2 * k * h)

        return (4 * h / 3) * sum1 + (2 * h / 3) * sum2 + (h / 3) * (f(a) + f(b))

    results = cycle_function(integrate)

    print_res('simpson:', *results)