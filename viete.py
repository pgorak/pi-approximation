from functools import reduce
from mpmath import mp

def viete_numerators(n):
    current = 1
    result = []
    for i in range(n):
        if i == 0:
            current = mp.sqrt(2)
        else:
            current = mp.sqrt(2 + current)
        result.append(current)
    return result

def pi_approx(n):
    multiplication = reduce(lambda x,y: x*y, map(lambda x: x/2, viete_numerators(n)))
    return 2 / multiplication

if __name__ == '__main__':
    mp.dps = 150
    print(pi_approx(500))
    