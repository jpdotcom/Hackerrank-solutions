import time
def tuple_hasing(n):
    s=time.time()
    x={(1,2,3,4,5,6,7,8,9):0}
    y=(1,2,3,4,5,6,7,8,9)
    for i in range(n):
        if y in x:
            s=1
    return time.time()-s


def matrix_hashing(n):

    s=time.time()
    x={((1,2,3),(4,5,6),(7,8,9)):0}
    y=((1,2,3),(4,5,6),(7,8,9))
    for i in range(n):
        if y in x:
            s=1
    return time.time()-s


print(matrix_hashing(10000),tuple_hasing(10000))