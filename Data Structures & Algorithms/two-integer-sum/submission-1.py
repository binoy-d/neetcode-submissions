class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {num: i for i, num in enumerate(nums)}
        for i, n in enumerate(nums):
            t = target-n
            if t in needed and needed[t] != i:
                return [i, needed[t]]
         
