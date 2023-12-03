from common import *


def half_rectangle(f, a, b):
    def integrate(n):
        h = ((b - a) / n)
        sum1 = 0

        for k in range(1, n + 1):
            sum1 += f(a + (k - 0.5) * h)

        return sum1 * h

    results = cycle_function(integrate)
    print_res('halfRectangle:', *results)
