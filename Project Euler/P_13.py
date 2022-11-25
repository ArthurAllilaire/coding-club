with open("Project Euler\P_13.txt", 'r') as f:
    strnum = f.read().split() #split into the ints
    total = 0
    for i in strnum:
        total += int(i)
    print(total)