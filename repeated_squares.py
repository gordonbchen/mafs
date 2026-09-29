from argparse import ArgumentParser


def mod_pow(a, b, n):
    """Compute a^b mod n."""
    assert (a >= 0) and (b >= 0) and (n > 0)
    if a == 0:
        return 0

    a %= n

    res = 1
    a_pow = a
    while b > 0:
        if (b & 1):
            res = (res * a_pow) % n
        b >>= 1
        a_pow = (a_pow * a_pow) % n
    return res


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("n", type=int)
    args = parser.parse_args()

    print(mod_pow(args.a, args.b, args.n))
