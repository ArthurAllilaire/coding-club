"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
def get_primes(n):
    """Gets all primes up to and including the nth prime e.g. n = 6 output: [2,3,5,7,11,13]"""
    if n == 1:
        primes = [2]
        return primes
    
    primes = [2,3]
    counter = 1
    while len(primes)< n:
        for j in [6*counter-1, 6*counter+1]: # iterate over 6n+/-1
            prime = True
            for i in primes:
                if j%i == 0:
                    prime = False
                    break
                if (i*i > j):#Once past sqaure root no point looking further
                    break
            if prime:
                primes.append(j)
        counter += 1
    return primes

print(get_primes(1000000)[-1])