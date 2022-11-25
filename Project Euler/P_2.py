import unittest
n = 600851475143
class Divisors:
    def __init__(self, n, divisors=None):
        #This is going to act as a stack
        if divisors:
            self.Divisors = sorted(divisors)
        else:
            self.Divisors = self.get_divisors(n)
            self.n = n

    def get_divisors(self, n=None):
        if n == None:
            n = self.n
        factors = []
        for i in range(1,round(n**0.5)):
            if n % i == 0:
                factors.append(i)
        return factors
    
    def insert_divisors(self, new_divs):
        """
        Assumes self.Divisors is already sorted - this is an insertion algorithm (using binary search) to insert new_divs
        [1,2,3,4,5,6,7,8,9,10] len = 10
        For even you are using upper of two vals by doing len/2
        For odd want middle one - so len/2 = x.5 so round to higher one

        """
        for i in new_divs:
            p1 = 0
            p2 = len(self.Divisors)-1
            while p2 != p1:
                temp_p = round(((p2-p1)/2)+p1) # First get the middle value
                if i < self.Divisors[temp_p]:
                    p2 = temp_p - 1
                    if p2 == p1 and i != self.Divisors[p2]: # No need to add already there
                        self.Divisors.insert(p2+1,i)
                elif i == self.Divisors[temp_p]:
                    break
                else:
                    p1 = temp_p + 1
                    if p1 == p2:
                        self.Divisors.insert(p1,i)      

    def get_largest_prime(self):
        while True:
            divisor = self.Divisors.pop()
            i_factors = self.get_divisors(divisor)
            if len(i_factors) == 1: #ie if prime
                return i_factors
            else:
                self.insert_divisors(i_factors)




factors = Divisors(n)
print(factors.get_largest_prime())

class DivisorsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.n = n
        self.Divisors = Divisors(n)
        self.factors = self.Divisors.get_divisors()
        return super().setUp()

    def test_get_divisors(self):
        print(self.factors)
        for i in self.factors:
            print(self.Divisors.get_divisors(i))

if __name__ == "__main__":
    unittest.main()

    





