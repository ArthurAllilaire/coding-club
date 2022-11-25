# <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.</p>
# <p>Find the largest palindrome made from the product of two 3-digit numbers.</p>
def pali(n):
    """n is the upper limit of two numbers we can multiply. There is always a palindrome somewhere"""
    def isPali(str):
        for i in range(len(str)//2):
            if str[i] != str[-(i+1)]:
                return False
        return True
    p1 = p2 = n # Set both to upper limit
    result = []
    while p1 > 885: # The first one found was 888888, so to ensure no higher check till x*999 < 888888
        while p1 <= p2:
            tem = p1 * p2
            if isPali(str(tem)):
                result.append(tem)
            p2 -= 1            
        p1 -= 1
        p2 = n
    return result


# def pali(n):
#     """This time going to try using batches of ten"""
    
#     #I think the best way is to start from 999*999 and brute force it.

print(pali(999))

def isPali(str):
        for i in range(len(str)//2):
            if str[i] != str[-(i+1)]:
                return False
        return True

print(isPali("912219"))