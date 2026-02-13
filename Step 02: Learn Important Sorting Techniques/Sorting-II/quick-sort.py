def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]   # first element as pivot
    
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)


# Example
arr = [5, 3, 8, 4, 2, 7, 1, 10]
print(quick_sort(arr))
# Time Complexity : O(n²)
