from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """

        Ex:
        nums = [2,20,4,10,3,4,5]
        lookup = {2,20,4,10,3,4,5}
        stops = {20, 10, 5}
        max_len = 3
        check_num = 2

        """
        # put it all in a set for O(1) lookup
        lookup = set(nums) # O(n)

        stops = set()
        for num in nums:
            # if we know the next number in the sequence is not there
            # this is an end to a a sequence
            if num+1 in lookup:
                continue
            stops.add(num)
        
        max_len = 0

        for num in stops:
            check_num = num -1
            
            while check_num in lookup:
                check_num -= 1
            if (num - check_num) > max_len:
                max_len = num - check_num

        return max_len



                

        
