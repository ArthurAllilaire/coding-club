import numpy as np
with open("Project Euler\P_11.txt", 'r') as f:
    #n = f.read().replace(" ","").replace("\n", "")
    strnum = f.read().split() #split into the ints
    nums = np.reshape(strnum, (20,20)).astype(np.int)

def multiply(lst):
    total = 1
    for i in lst:
        total *= i
    return total
    
def max_4(row):
    if len(row) < 4:
        return 0
    max = 1
    for i in range(len(row)-3):
        product = multiply(row[i:i+4])
        if product > max:
            max = product
    return max

def across_4(nums):
    max = 1
    for row in nums:
        max4 = max_4(row)
        if max4>max:
            max = max4
    return max

def down_4(nums):
    """Takes a numpy array and transpose for columns"""
    max = 1
    for cols in nums.T:
        max4 = max_4(cols)
        if max4>max:
            max = max4
    return max

"""def diag_4(numArr, reverse=False):
     
    max = 1
    row = []
    #n(cols)*m(rows)
    for nums in [numArr,numArr.T]:
        n = nums.shape[0]
        for m in range(nums.shape[1]):
            i = m
            j = 0 # Start at (m,0)
            if reverse:
                j = n-1
            while i<nums.shape[1] and j<n and j>=0: # Iterate till out of vals
                row.append(nums[j,i])
                i += 1
                if reverse:
                    j -= 1
                else:
                    j += 1
            print(row)
            prod = max_4(row)
            if prod>max:
                max = prod
            print(max)
            row = []
    return max"""

"""
[1,2,3]
[4,5,6]
[7,8,9]
row = []
n*m: n cols and m rows 
for m in range(nums[1]):
    i = m
    j = 0 # Start at (m,0)
    while i<nums[1] and j<nums[0]: # Iterate till out of vals
        row.append(nums[i,j])
        i += 1
        j += 1
    j = 0



"""

def gen_diags(inp_arr):
    """Takes a 2D array and generates all diagonals (both main and anti diagonal)"""
    for arr in [inp_arr,np.fliplr(inp_arr)]:
        row_len = inp_arr.shape[1]
        for offset in range(-row_len+1, row_len):
            diag = arr.diagonal(offset)
            yield diag

max = 1
diag_gen = gen_diags(nums)
for i in diag_gen:
    prod = max_4(i)
    if prod > max:
        max = prod
print(max)
#Get all left to right diagonals
#print(diag_4(nums))
#print(diag_4(nums.T))
#Get all right to left values
#print(diag_4(nums, reverse=True))
#print(across_4(nums))
#print(down_4(nums))
max = 0