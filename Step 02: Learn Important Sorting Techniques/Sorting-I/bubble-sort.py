def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Example arr = [5, 3, 8, 4, 2]


