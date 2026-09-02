def gcd(a: int, b: int) -> int:
    while True:
        a %= b
        if (a == 0): return b

        b %= a
        if (b == 0): return a

print(gcd(2415, 945))
