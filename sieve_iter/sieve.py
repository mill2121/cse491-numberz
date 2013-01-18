# an implementation of Eratosthenes' Sieve:
#   http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

class sieve(object):
    def __init__(self):
        self.primeslist = [2]

    def __iter__(self):
        return self

    def _is_prime(self, primes, n):
        for i in primes:
            if n % i == 0:
                return False
        return True

    def next(self):
        start = self.primeslist[-1] + 1
        while 1:
            if self._is_prime(self.primeslist, start):
                self.primeslist.append(start)
                return start

            start += 1
