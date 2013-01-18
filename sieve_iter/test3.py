import sieve

for n, i in zip(range(25), sieve.sieve()):
    print i

