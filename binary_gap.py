
def Solution(N):
    # convert the given number to binary number and remove the preceeding '0x'
    binary_number = list(bin(N)[2:])

    # retrieve all the indexes for which the item is one
    index_of_ones = [index for index, item in enumerate(binary_number) if item == '1']
    
    # find the differences of index_of_ones and find the maximum
    if len(index_of_ones) > 1:
        differences = [index_of_ones[i + 1] - index_of_ones[i] for i in range(len index_of_ones) - 1)]
        return (max(differences) - 1)
    return 0
        

