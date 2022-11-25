def brute_force(n):
    """Need a + b + """
    for a in range(1, n):
        for b in range(a,n):
            c = (a**2+b**2)**0.5
            if a + b + c == 1000.0:
                return (a,b,c)


print(brute_force(1000))
