def twoSum(nums, target):
    num_map = {}  # value -> index mapping
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in map, we found the pair
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number and its index
        num_map[num] = i
    
    return []

# Example
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
# Time Complexity : O(n) using Hashmap Approach
