class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)

        total_prod = 1
        total_prod_no_zeroes = 1
        
        num_zeroes = 0
        zero_index = -1

        for i, num  in enumerate(nums):
            if num == 0:
                num_zeroes += 1
                zero_index = i
            else:
                total_prod_no_zeroes *= num
            if num_zeroes > 1:
                return [0]*len(nums)
            
            total_prod *= num

        if num_zeroes == 0:
            return [total_prod//num for num in nums]
        

        # has exactly one zero - special case
        output[zero_index] = total_prod_no_zeroes

        return output