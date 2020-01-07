class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)

        if n % 2 == 0:
            return (nums[(n // 2) - 1] + nums[n // 2]) / 2.0
        else:
            return nums[n // 2]
