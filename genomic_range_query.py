"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).
"""


def solution(S, P, Q):
    # write your code in Python 3.6
    arr = []

    def mapString(x):
        if 'A' in x:
            return 1
        if 'C' in x:
            return 2
        if 'G' in x:
            return 3
        if 'T' in x:
            return 4

    zip_ = list(zip(P, Q))

    for i, j in zip_:
        sub_list = S[i:j + 1]
        arr.append(mapString(sub_list))

    return arr
