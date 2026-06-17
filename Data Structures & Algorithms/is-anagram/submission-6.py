class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs, ct = dict(), dict()
        for c in s:
            cs[c] = cs.get(c, 0) + 1

        for c in t:
            ct[c] = ct.get(c, 0) + 1
            
        return cs == ct