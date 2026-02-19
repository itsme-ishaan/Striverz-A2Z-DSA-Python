class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        currentIndex = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[currentIndex] = nums[currentIndex], nums[i]
                currentIndex += 1


      # Time Compleity : O(n)
