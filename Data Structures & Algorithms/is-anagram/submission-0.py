class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts_S = {}
        
        for letter in s:
            if letter in counts_S:
                counts_S[letter] = counts_S[letter] + 1
            else:
                counts_S[letter] = 1
        
        counts_T = {}

        for letter in t:
            if letter in counts_T:
                counts_T[letter] = counts_T[letter] + 1
            else:
                counts_T[letter] = 1
        
        for letter, count in counts_S.items():
            if counts_T.get(letter, 0) != count:
                return False
            del counts_T[letter]

        return len(counts_T) == 0
        
        