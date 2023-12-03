from common import *


def trapezium(f, a, b):
    def integrate(n):
        h = ((b - a) / n)
        sum1 = 0

        for k in range(1, n):
            sum1 += f(a + k * h)

        return sum1 * h + (h / 2) * (f(a) + f(b))

    results = cycle_function(integrate)
    print_res('trapezium:', *results)
