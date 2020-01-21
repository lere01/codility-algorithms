def my_solution(X, A):
    my_set = set()
    check_list = set(range(1, X + 1))

    for index, item in enumerate(A):
        my_set.add(item)

        if len(my_set) == X:
            return index

    return -1
