class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_arr(s):
            arr = [0 for c in 'abcdefghijklmnopqrstuvwxyz']
            for c in s:
                i = ord(c) - ord('a')
                arr[i] += 1
            return arr
            
        
        # map ag count
        ags = {}
        for s in strs:
            arr = str(get_arr(s))
            if arr in ags:
                ags[arr].append(s)
            else:
                ags[arr] = [s]
        print(ags)
        return list(ags.values())


