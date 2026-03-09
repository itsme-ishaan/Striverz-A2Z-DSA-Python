def majorityElement(nums):
    from collections import Counter
    
    counts = Counter(nums)
    return max(counts.keys(), key=counts.get)
