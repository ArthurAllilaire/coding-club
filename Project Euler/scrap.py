import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]], np.int32)
print(np.fliplr(x).diagonal(-1,axis1=1,axis2=0))
print(x)

def gen_diags(inp_arr):
    """Takes a 2D array and generates all diagonals (both main and anti diagonal)"""
    for arr in [inp_arr,np.fliplr(inp_arr)]:
        row_len = inp_arr.shape[1]
        for offset in range(-row_len+1, row_len):
            diag = arr.diagonal(offset)
            yield diag

diag_gen = gen_diags(x)
for i in diag_gen:
    print(i)