"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#Firstly need algo that gets prime factorisation (that is not my calculator)
def prime_fac(n):
    #First try 2 and 3
    primes = []
    for d in [2,3]:
        while(n%d == 0):
            primes.append(d)
            n /= d
    if n == 1:
        return primes
    d = 5
    while (d*d<=n):
        for i in [d, d+2]: # Do for 6n+/-1
            if not prime_fac(i): # If there are not prime facs (as algo only checks below sqrt(d))
                while(n%i == 0):
                    primes.append(i)
                    n /= i
        d += 6
    if len(primes) == 0:
        primes.append(n)
    return primes

print(prime_fac(199653))

def smallest_divis(n):
    """Returns the smallest number that is divisble by all numbers below and including n"""
    #To do this I need the prime factors of all of them then multiply the biggest factor of each
    def count(lst):
        counter = {}
        for i in lst:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        return counter

    def update(count1, count2):
        """Given update count1 so that has largest primes of both counters (modifies original dict as more efficient)"""
        for p,i in count2.items():
            if p not in count1 or count1[p] < i:
                count1[p] = i


    counter = {}
    for i in range(1,n):
        temp_count = count(prime_fac(i)) # i.e. it is not prime itself
        update(counter, temp_count)
    total = 1
    for prime,power in counter.items():
        total *= prime**power
    return counter, total

def gcd(a,b):
    while b != 0:
        rem = a%b
        a = b
        b = rem
    return a

def lcm(a,b):
    return a*b/gcd(a,b)

def PE(N):
    ans=1
    for i in range(2, N+1):
        ans=lcm(i,ans)
    return ans

print(int(PE(10000)))

#print(smallest_divis(100000))