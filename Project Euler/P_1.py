import math
# P1
# 
# n = 1000000000

# def m_t(n,m):
#     """Returns total of all multiples of m below n"""
#     # First get how many multiples there are:
#     m_num = (n-1)//m
#     #Therefore total of all those multiples is 1*5 + 2*5 .... m_5 * 5

#     return int((m_num+1)*m_num/2)*m

# print(m_t(n,5)+m_t(n,3)-m_t(n,15))

#P2
# Get sum of all even numbers in fibonacci squence below 4 million
# I think i should brute force it :(

def fib_even(max):
    """Returns sum of all even terms below n almost want a stack"""
    n = [1,1]
    total = 0
    counter = 2 # Created 2 to start with
    while True:
        n3 = sum(n)
        if n3 > max:
            return total
        counter += 1
        if counter % 3 == 0:
            total += n3
        n.pop(0)
        n.append(n3)

#SOL 2 (using phi)
def fib_even(max):
    phi = 5/(1+2**0.5)
    n= round(phi)
    #first even term is phi
    total = 0
    while True:
        total += n
        n = round(n*phi**3)
        if n > max:
            return total
phi = 5/(1+2**0.5)
for i in range(10):
    print(phi**i)
print(fib_even(10))