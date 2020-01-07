class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashtable = {}

        for i, n in enumerate(numbers):
            if target - n in hashtable:
                return [hashtable[target - n], i + 1]

            hashtable[n] = i + 1
