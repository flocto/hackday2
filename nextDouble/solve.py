SEED = 0
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

data = open('output.txt', 'r').read().split('\n')
enc = eval(data[1])
r = float(data[0])
r *= 1 << 56
r = int(r)

a = r >> 28
b = r - (a << 28)

a <<= 4
b <<= 4

for a_small in range(16):
    for b_small in range(16):
        ta = a | a_small
        tb = b | b_small
        x = tb - ta
        if x < 0:
            x += 1 << 31
            x += 1 # carry
        
        y = tb
        SEED = (x << 32) | y
        
        for _ in enc:
            print(randFloat())

        exit()