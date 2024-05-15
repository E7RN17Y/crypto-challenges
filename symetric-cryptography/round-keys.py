import numpy as np

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]



def add_round_key(s, k):
    matrix_1 =  np.matrix(s,dtype=np.int32)
    matrix_2 = np.matrix(k, dtype=np.int32)

    return (matrix_1 ^ matrix_2).tolist()

def flag(xord):
    return bytes(sum(xord,[]))

print(flag(add_round_key(state, round_key)))

