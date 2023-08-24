from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = dict()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffMap:
                return [diffMap[diff], i]
            diffMap[num] = i
        
        return []