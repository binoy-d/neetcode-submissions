class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(1) lookup
        indices = {}
        for i, num in enumerate(nums):
            if num not in indices:
                indices[num] = i
            needed = target - num
            if needed in indices and indices[needed] != i:    
                i2 = indices[needed]
                if i < i2:
                    return [i, i2]
                return [i2, i]