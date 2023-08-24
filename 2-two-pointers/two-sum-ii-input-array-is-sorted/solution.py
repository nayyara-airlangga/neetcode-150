from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin_ptr, end_ptr = 0, len(numbers) - 1

        while begin_ptr < end_ptr:
            sum = numbers[begin_ptr] + numbers[end_ptr]

            if sum > target:
                end_ptr -= 1
            elif sum < target:
                begin_ptr += 1
            else:
                return [1 + begin_ptr, 1 + end_ptr]

        return []


solution = Solution()
print(solution.twoSum([0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 9, 9, 9, 9, 9], 5))
