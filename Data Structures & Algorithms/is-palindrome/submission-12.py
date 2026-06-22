class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0

        s = "".join([c.lower() for c in s if c.isalnum()])

        r = len(s) - 1
        while l <= r and l <= len(s)/2:
            left = s[l]
            right = s[r]
            if left != right:
                print(left, right)
                return False
            l += 1
            r -= 1
        return True