from itertools import product

def iterate_key(keysize):
    combinations = product(range(256), repeat=keysize)
    for combo in combinations:
        yield bytes(combo)