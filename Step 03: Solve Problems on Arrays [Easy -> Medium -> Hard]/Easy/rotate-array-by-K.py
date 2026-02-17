def rotate(arr, k):
    n = len(arr)
    k = k % n   # handle k > n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Step 1
    reverse(0, n - 1)
    
    # Step 2
    reverse(0, k - 1)
    
    # Step 3
    reverse(k, n - 1)


# Example
arr = [1,2,3,4,5,6,7]
rotate(arr, 3)
print(arr)


#Time Complexity : O(n)
#Space Complexity : O(1)
