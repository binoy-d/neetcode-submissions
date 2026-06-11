class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        contains={p}
        2
        012345
         lr
        pwwkew

        """
        
        if len(s) <= 1:
            return len(s)
        
        left = 0
        right = 1
        contains = {s[left]}
        result = right - left + 1
        max_len = 0
        while right < len(s):
            right_char = s[right]
            while right_char in contains:
                if s[left] in contains:
                    contains.remove(s[left])
                    left += 1
                    continue
                contains.remove(right_char)
                left+=1
            contains.add(right_char)
            result = right - left +1
            right+=1
            
            if result > max_len:
                max_len = result
        return max_len