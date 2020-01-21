def Solution(A):
    return [x for x in set(A) if A.count(x) % 2 == 1][0]
