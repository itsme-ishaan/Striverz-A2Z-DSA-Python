def union_sorted(arr1, arr2):
    """
    Simplified two-pointer approach
    """
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        # Compare current elements
        if arr1[i] < arr2[j]:
            # Add arr1[i] if not duplicate
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            # Add arr2[j] if not duplicate
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:  # arr1[i] == arr2[j]
            # Add once (avoid duplicate)
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
    
    # Add remaining from arr1
    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    
    # Add remaining from arr2
    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1
    
    return result

# Time: O(m + n) ✅
# Space: O(m + n) ✅
