from argparse import ArgumentParser


def bezout(a, n):
    """Return (x, y) s.t. nx + ay = gcd(a, n)."""
    q, r = divmod(n, a)
    if r == 0:
        return 0, 1

    c1, c2 = bezout(r, a)
    c3 = c2
    c4 = c1 + c2*(-q)
    return c3, c4


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    a, n = args.a, args.n

    x, y = bezout(a, n)
    assert (n*x + a*y == 1)
    print(f"{n}*{x} + {a}*{y} = 1")
