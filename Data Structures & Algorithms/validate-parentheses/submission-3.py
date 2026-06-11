class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        valids = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in valids:
                stack.append(c)
                continue
            # c is a closer
            if len(stack) == 0:
                return False
            last_opened = stack.pop(-1)

            expected = valids[last_opened]
            print(f"encountered {c}, expecting {expected}")
            if valids[last_opened] != c:
                return False
        return len(stack) == 0