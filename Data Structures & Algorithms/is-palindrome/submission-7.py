class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        "  "
        left = 0
        right = 1


        """
        if len(s) <= 1:
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            print(f"s[{left}] vs s[{right}]")
            # push up left pointer until we hit a valid character
            while not s[left].isalnum():
                left += 1
                if left > len(s) - 1:
                    return True
                continue
            
            # push back right pointer until we hit a valid character
            while not s[right].isalnum():
                right -= 1
                if right < 0:
                    return True
                continue
            
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        return True
