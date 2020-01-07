class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            prev_max = [0, nums[0], nums[1]]

            for i in nums[2:]:
                tmp = max(prev_max[0], prev_max[1]) + i

                prev_max[0] = prev_max[1]
                prev_max[1] = prev_max[2]
                prev_max[2] = tmp

            return max(prev_max)
