import numpy as np
if __name__=='__main__':
    n,m = map(int, input().split())
    arr = []
    for row in range (0, n):
        arr.append(list(map(int, input().split())))
    arr = np.array(arr)
    print (max(arr.min(axis=1)))
