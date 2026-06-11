class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        [1, 2, 3, 4], h = 9
        low = 1
        high = 4
        mid = 2
        things we know:
        if h = 1, you can only eat one pile and k has to be the max num

        each hour, we want to always try and use the full k

        binary search -> need low and high
        low = min(piles)
        high = max(piles)

        """

        def calculate_hours(k):
            total = 0
            for num in piles:
                if num < k:
                    total += 1
                    continue
                total += ((num // k) + (1 if num%k != 0 else 0))
            return total

        piles = sorted(piles)
        
        low = 1
        high = piles[-1]
        best_k = high
        min_hours = calculate_hours(high)
        while low <= high:
            
            # mid is the eating rate, k
            mid = (low + high) // 2
            
            hours_needed = calculate_hours(mid)
            print(f"{piles}, {low}-{mid}-{high} = {hours_needed}")
            # we know its too high if it takes longer than allotted time, increase the rate
            if hours_needed > h:
                print(" - going higher")
                low = mid + 1
            
            # we can go lower if it takes less hours than we're allotted
            if hours_needed <= h:
                print(" - going lower")
                if mid < best_k:
                    best_k = mid
                min_hours = hours_needed
                high = mid - 1

        return best_k


