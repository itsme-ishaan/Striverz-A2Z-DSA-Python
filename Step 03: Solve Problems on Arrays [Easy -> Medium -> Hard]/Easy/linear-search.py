def linear_search(arr, target):
    """
    Simplest & Most Optimal for unsorted array
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found! Return index
    return -1  # Not found

# Time Complexity:
# Best Case:    O(1)    → Element first position pe
# Average Case: O(n/2)  → Element middle mein
# Worst Case:   O(n)    → Element last mein ya nahi hai

# Space Complexity: O(1)
