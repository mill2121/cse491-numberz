# an implementation of Eratosthenes' Sieve:
#   http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# Checks whether a number is prime or not
def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

# Loops through numbers and jumps back to the test files once one is found
def sieve():
    _primeslist = [2]
    
    start = _primeslist[-1] + 1
    while 1:
        if _is_prime(_primeslist, start):
            _primeslist.append(start)
            yield start

        start += 1
