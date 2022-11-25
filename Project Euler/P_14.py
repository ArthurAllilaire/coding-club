def formula(n):
    if n == 1:
        return [1]
    if n%2 == 0: # If even return n/2
        return [n] + formula(n//2)
    return [n] + formula(3*n+1)

def form_len(i):
    

def longest(n):
    max_len = 1
    for i in range(1,n):
        if form_len(i) > max_len:
            )
        pass

longest(1000000)

print(formula(243))