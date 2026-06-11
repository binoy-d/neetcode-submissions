from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # should be O(n)
        counts = Counter(nums)

        # at most a num can occur len(nums) times
        frequencies = [set() for _ in nums]
        # write each one to bucket
        for num, num_count in counts.items():
            frequencies[num_count-1].add(num)
        out = []
        for i in reversed(frequencies):
            out.extend(i)
            if len(out) == k:
                return out

        return out            

