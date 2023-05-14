from random import randint

SEED = randint(1, 2**64-1)


def rand(b: int = 32):
    '''
    Generates a random 32-bit integer, or
    a random integer with b bits.
    '''
    global SEED

    x = SEED >> 32
    y = SEED - (x << 32)
    SEED += x

    return y >> (32 - b)


def randFloat():
    '''
    Generates a random float in the range [0, 1).
    '''
    r = rand(28) << 28 | rand(28)
    return r / (1 << 56)


flag = b'chsctf{java_nextDouble_is_harder_tbh}'
enc = []

with open("output.txt", "w") as f:
    f.write(str(randFloat()) + "\n")
    for c in flag:
        r = randFloat()
        print(r)
        enc.append(c * r)
    f.write(str(enc))