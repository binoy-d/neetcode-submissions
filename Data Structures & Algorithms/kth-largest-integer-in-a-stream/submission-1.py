class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stack = []
        
        # [largest, less large, kth large]
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.stack) == 0:
            self.stack = [val]
            print(f"add {val}, stack: {self.stack}")
            return val
        # work backward from end of stack and insert after first element larger than it

        i = len(self.stack) - 1
        while i >= 0:
            if self.stack[i] >= val:
                self.stack.insert(i+1, val)
                break
            i -= 1
            if i == -1:
                self.stack.insert(0, val)
                break
        if len(self.stack) > self.k:
            self.stack = self.stack[:min(self.k, len(self.stack)-1)]
        print(f"add {val}, stack: {self.stack}")
        return self.stack[-1]