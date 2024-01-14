def find_min_swaps(arr):
    def count_swaps(arr, order):
        swaps_count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (order == 'asc' and arr[i] > arr[j]) or (order == 'desc' and arr[i] < arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps_count += 1
        return swaps_count

    def min_swaps_to_beautiful(arr):
        swaps_ascending = count_swaps(arr.copy(), 'asc')
        swaps_descending = count_swaps(arr.copy(), 'desc')
        return min(swaps_ascending, swaps_descending)

    return min_swaps_to_beautiful(arr)

# Input
num_elements = int(input())
array_elements = list(map(int, input().split()))

# Output
result_swaps = find_min_swaps(array_elements)
print(result_swaps)
