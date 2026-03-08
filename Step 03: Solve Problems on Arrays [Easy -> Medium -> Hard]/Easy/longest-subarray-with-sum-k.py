from typing import List

def longest_subarray_sum_k(nums: List[int], k: int) -> int:
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            max_len = max(max_len, right - left + 1)

    return max_len


# example
nums = [1, 2, 1, 1, 1, 3, 2]
k = 3
print(longest_subarray_sum_k(nums, k))  # 3
