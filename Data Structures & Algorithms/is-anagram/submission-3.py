from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s) # O(n)
        c2 = Counter(t) # O(n)
        return c == c2