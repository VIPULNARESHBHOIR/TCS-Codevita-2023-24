def find_min_swaps(arr):
    size = len(arr)
    # Count swaps for both ascending and descending order
    swaps_ascending = count_no_swaps(arr.copy(), "asc",size)
    swaps_descending = count_no_swaps(arr.copy(), "desc",size)

    # return minimum swaps
    return min(swaps_ascending, swaps_descending)

# count the number of swaps needed to sort the array
def count_no_swaps(array, order_type,size):
    count = 0
    for i in range(size):
        for j in range(i + 1, size):
            if (order_type == "asc" and array[i] > array[j]) or (order_type == "desc" and array[i] < array[j]):
                array[i], array[j] = array[j], array[i]
                count += 1
    return count


# Input
number_of_elements = int(input())
array = list(map(int, input().split()))

# Output
result = find_min_swaps(array)
print(result)
