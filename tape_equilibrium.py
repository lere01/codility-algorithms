def Solution(A):
    section_one = A[0]
    section_two = sum(A[1:])
    min_difference = abs(section_one - section_two)

    for i in range(1, len(A) - 1):
        section_one += A[i]
        section_two -= A[i]
        difference = abs(section_one - section_two)

        if difference < min_difference:
            min_difference = difference

    return min_difference
