def majorityElement(nums):
    from collections import Counter
    
    counts = Counter(nums)
    return max(counts.keys(), key=counts.get)

# Approach 2 : Boyer Moore's Algorithm 

def majorityElement(nums):
    candidate = None
    count = 0
    
    for num in nums:
        # If count is 0, we need a new candidate
        # (previous battles ended in a tie)
        if count == 0:
            candidate = num
            count = 1
        
        # If current number matches our candidate
        # (ally found - strengthen our position)
        elif num == candidate:
            count += 1
        
        # If current number is different
        # (opponent found - cancel votes)
        else:
            count -= 1
    
    # The last candidate standing is the majority
    return candidate
