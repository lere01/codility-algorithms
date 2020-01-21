def Solution(A, K):
    # if the given array is empty, return the array
    if len(A) == 0:
        return A

    # get the rotation factor
    factor = K % len(A)

    # slice the array using the rotation factor
    first_slice = A[len(A) - factor:]
    second_slice = A[:len(A) - factor]

    # return a rotated array
    return first_slice + second_slice
