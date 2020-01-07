class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            y = target - x

            try:
                j = nums.index(y)

                if i != j:
                    return i, j
            except ValueError:
                pass
