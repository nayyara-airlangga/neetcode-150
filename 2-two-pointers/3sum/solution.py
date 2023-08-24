from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        triplets = []
        first_ptr = 0

        while first_ptr < len(nums) - 1:
            first_num = nums[first_ptr]

            second_ptr, third_ptr = first_ptr + 1, len(nums) - 1

            while second_ptr < third_ptr:
                sum = nums[first_ptr] + nums[second_ptr] + nums[third_ptr]

                if sum > 0:
                    third_ptr -= 1
                elif sum < 0:
                    second_ptr += 1
                else:
                    triplet = [nums[first_ptr], nums[second_ptr], nums[third_ptr]]
                    triplets.append(triplet)

                    second_ptr += 1
                    third_ptr -= 1

                    while (
                        second_ptr < third_ptr
                        and nums[second_ptr] == nums[second_ptr - 1]
                    ):
                        second_ptr += 1

            first_ptr += 1
            while first_ptr < len(nums) - 1 and first_num == nums[first_ptr]:
                first_ptr += 1

        return triplets


solution = Solution()
print(solution.threeSum([-2, 0, 0, 2, 2]))
