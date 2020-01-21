def solution(A):

    my_set = set(A)
    ideal_set = set(range(1, len(my_set) + 1))

    list_of_difference = list(ideal_set.difference(my_set))

    if len(list_of_difference) == 0:
        return len(ideal_set) + 1

    elif min(list_of_difference) < 0:
        return 1

    return min(list_of_difference)