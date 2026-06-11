class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
         [1, 1, 2, 3, 4, 4], target=3
         left = 0, right = 4
         num_left = 1, num_right = 4
         
         key discover: moving left up increases total, moving right down decreases total

         edge cases:
         []
        
        """
        total = 0
        left = 0
        right = len(numbers) -1
        if len(numbers) == 2:
            return [1, 2]

        while True:
            num_left = numbers[left]
            num_right = numbers[right]
            total = num_left + num_right
            if total == target:
                return [left+1, right+1]
            # too big
            if total > target:
                # move right to the left to decrease
                right -= 1
                continue
            # too small
            left += 1


