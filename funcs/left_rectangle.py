from common import *


def left_rectangle(f, a, b):
    def integrate(n):
        h = ((b - a) / n)
        sum1 = 0

        for k in range(n):
            sum1 += f(a + k * h)

        return sum1 * h

    results = cycle_function(integrate)
    print_res('leftRectangle:', *results)
