from itertools import product


Z3 = (0, 1, 2)
for a, b, c in list(product(*([Z3] * 3))):
    if a == 0:
        continue

    for x in Z3:
        res = (a* x*x + b * x + c) % 3
        if res == 0:
            break
    else:
        print((a, b, c))
