class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        target = 4
        nums = [-1,0,2,3,6,8]
        start = 3
        stop = 4
        mid = 3
        mid_num = 3

        """


        start = 0
        stop = len(nums)-1
        
        

        while start <= stop:
            mid = (start + stop) // 2
            mid_num = nums[mid]
            if mid_num < target:
                start = mid + 1
            elif mid_num > target:
                stop = mid -1
            else:
                return mid
        return -1            

    

        
