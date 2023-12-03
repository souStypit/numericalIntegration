def print_res(method, *args):
    print(f'{method} f1={args[0]} f2={args[1]} n={args[2]} sigma = {args[3]}')


def cycle_function(func):
    n, sigma, x1, x2 = 1, 0, 0, func(1)
    while sigma >= abs(x1) * 0.001:
        n = n * 2
        x1 = func(n)
        sigma = abs(x2 - x1)
        x2 = x1

    return x1, x2, n, sigma
