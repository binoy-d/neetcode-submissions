class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [[strs[0]]]
        
        anagrams = {}

        for s in strs:
            normalized = ''.join(sorted(s))
            if normalized not in anagrams:
                anagrams[normalized] = []
            anagrams[normalized] += [s]
        return anagrams.values()