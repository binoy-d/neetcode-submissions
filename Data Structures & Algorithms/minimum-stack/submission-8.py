class MinStack:
    """
    stack = [1, 2]
    min =   [1, 1]
    """ 
    def __init__(self):
        self.min_stack = []
        self.stack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or (val < self.min_stack[-1]):
            self.min_stack.append(val)
            return    
        self.min_stack.append(self.min_stack[-1])
        
    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]
