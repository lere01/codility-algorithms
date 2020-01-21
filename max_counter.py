def solution(N, A):
    # create list of counters
    counters = [0] * N

    # initialize variable to keep track of max counter
    counter = 0

    # check for an array of max counter operations
    if len(set(A)) == 1 and A[0] == N + 1:
        return counters

    # loop through the array of operations and perform the operations
    for _, item in enumerate(A):
        if item <= N:
            counters[item - 1] += 1
            counter = max([counter, counters[item - 1]])

        elif item == N + 1:
            counters = [counter] * N

    return counters
