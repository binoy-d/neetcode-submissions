class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = dict()
        for i in range(len(nums)):
            n = nums[i]
            need = target - n
            if need in indices:
                i2 = indices[need]
                if i2 != i:
                    return [min(i, i2), max(i, i2)]
            indices[n] = i
        return []


        # indices = {5: 0,}