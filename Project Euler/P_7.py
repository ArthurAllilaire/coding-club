with open("Project Euler\P_7.txt", 'r') as f:
    #n = f.read().replace(" ","").replace("\n", "")
    num = f.read().split()
    nums = []
    for i in num:
        for j in i:
            nums.append(j)
    print(nums)

def productOf(lst):
    total = 1
    for i in lst:
        total *= int(i)
    return total

max = 0
for i in range(len(nums)):
    temp = productOf(nums[i:i+13])
    if temp > max:
        max = temp
    
print(max)
