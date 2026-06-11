class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = dict(zip("abcdefghijklmnopqrstuvwxyz", range(0, 27)))
        # brute force
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [[strs[0]]]
        
        anagrams = {}

        for s in strs:
            normalized = [0]*26
            for j in s:
                normalized[alphabet[j]] += 1
            
            normalized = hash(tuple(normalized))

            if normalized not in anagrams:
                anagrams[normalized] = []
            print(f"adding {s} to anagrams[{normalized}]")
            anagrams[normalized]+=[s]

        return anagrams.values()