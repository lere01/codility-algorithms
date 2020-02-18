"""
Write a function:
def solution(A, B, K)
that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
{ i : A ≤ i ≤ B, i mod K = 0 }
For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
Write an efficient algorithm for the following assumptions:
A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

"""


def solution(A, B, K):
    # write your code in Python 3.6
    result = 0

    if K == None:
        return 0

    if A == B and B > K:
        result = int(B % K == 0)
        return result

    if A == 0 and K > B:
        return 1

    if A == None and B == None:
        return 0

    if K > B:
        return 0

    if A % K == 0:
        result = int((B - A) / K) + 1
        return result

    if A > K:
        # p = A + (K - (A % K))
        n = A + (K - (A % K))
        result = int((B - n) / K) + 1
        return result

    if A < K:
        result = int((B - K) / K) + 1
        return result


def another_solution(A, B, K):
    difference = B - A

    if A % K == 0:
        return (difference // K) + 1

    remainder = A % K
    result = (difference + remainder) // K
    return result
