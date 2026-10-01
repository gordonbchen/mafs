from argparse import ArgumentParser


def mod_add_offset(x, shift, offset, mod):
    return ((x - offset + shift) % mod) + offset

def encode(text, shift):
    return "".join(chr(mod_add_offset(ord(c), shift, ord('a'), 26)) for c in text)

def decode(text, shift):
    return "".join(chr(mod_add_offset(ord(c), -shift, ord('a'), 26)) for c in text)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("text")
    parser.add_argument("-s", "--shift", type=int, default=3)
    parser.add_argument("-d", "--decode", action="store_true")
    args = parser.parse_args()

    if args.decode:
        print(decode(args.text, args.shift))
    else:
        print(encode(args.text, args.shift))
