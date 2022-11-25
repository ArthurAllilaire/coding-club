"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
def get_primes(n):
    """Gets all primes up to but excluding the nth number e.g. n = 17 output: [2,3,5,7,11,13]"""
    if n == 1:
        primes = [2]
        return primes
    
    primes = [2,3]
    counter = 1
    while primes[-1]< n:
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
    primes.pop() # Have one higher than n
    return primes

print(sum(get_primes(100)))

"""
Alternative and faster method using maths :))

Okay the sum of all numbers below v that are prime is going to be all primes and numbers that are multiples of primes largers than some p (therefore as long as p**2 is greater than or equal to v will be sum of all primes)

To calculate this use recursive formula. That the sum of prims S(v,p) = S(v,p-1) - p(sum of all )
"""

def S(v,p):
    """Returns the sum of all primes up to v + numbers from multiples of primes higher"""
    #If p == 1 
    if p == 1:
        return (v*(v+1)/2) -1
    return S(v,p-1) - p*(S(int(v/p),p-1)-S(p-1,p-1))

print(S(10,1))