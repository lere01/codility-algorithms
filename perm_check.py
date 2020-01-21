def Solution(A):
    ideal_list = list(range(1, len(A) + 1))
    return int(sum(A) == sum(ideal_list) and len(set(A)) == len(ideal_list))
