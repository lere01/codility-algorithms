"""
This is a demo task.
Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""


def solution(A):

    my_set = set(A)
    ideal_set = set(range(1, len(my_set) + 1))

    list_of_difference = list(ideal_set.difference(my_set))

    if len(list_of_difference) == 0:
        return len(ideal_set) + 1

    elif min(list_of_difference) < 0:
        return 1

    return min(list_of_difference)