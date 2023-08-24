from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_counts = dict()
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
                if num_counts[num] >= 2:
                    return True
            else:
                num_counts[num] = 1
        
        return False