def Reverse(arr, i, j):
    if i >= j:   # Base condition
        return
    
    arr[i], arr[j] = arr[j], arr[i]  # Swap
    
    Reverse(arr, i + 1, j - 1)  # Recursive call

)
