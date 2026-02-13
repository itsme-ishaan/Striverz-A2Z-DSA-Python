def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        
        # Find smallest element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap smallest with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Time Complexity : O(n²)

