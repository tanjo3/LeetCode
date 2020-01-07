class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_i = 0
        seen = {}

        for n in nums:
            if n not in seen:
                seen.setdefault(n)
                nums[prev_i] = n
                prev_i += 1

        return len(seen)
