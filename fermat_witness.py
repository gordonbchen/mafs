from argparse import ArgumentParser
from repeated_squares import mod_pow

parser = ArgumentParser()
parser.add_argument("n", type=int)
n = parser.parse_args().n

for i in range(1, n):
    a = mod_pow(i, n-1, n)
    if a != 1:
        print(f"{i}^{n-1} = {a} mod {n}")
        break
else:
    print("No fermat witnesses found.")
