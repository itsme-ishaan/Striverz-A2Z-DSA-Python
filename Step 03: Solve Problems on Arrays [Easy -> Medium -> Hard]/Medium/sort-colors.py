class Solution:
    def sortColors(self, nums: list[int]) -> None:
        c0, c1, c2 = 0, 0, 0
        
        # PASS 1: Count frequencies
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
                
        # PASS 2: Fill the array based on counts
        idx = 0
        while c0 > 0:
            nums[idx] = 0
            idx += 1
            c0 -= 1
            
        while c1 > 0:
            nums[idx] = 1
            idx += 1
            c1 -= 1
            
        while c2 > 0:
            nums[idx] = 2
            idx += 1
            c2 -= 1
