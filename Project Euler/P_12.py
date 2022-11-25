def triangle_num(n):
    return int(n*(n+1)/2)

print(triangle_num(7))
#First number where n and n+1 have 500 divisors

#So find divisors of n and n+1, add them then multiply all till above 500
