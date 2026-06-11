class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        10 6 -132 

        """
        stack = []
        ops = ['+', '-', '*',  '/']
        for t in tokens:
            if t not in ops:
                stack.append(t)
                continue
            num_2 = stack.pop()
            num_1 = stack.pop()
            if t == '/':
                t = '/'
            operation = f"{num_1}{t}{num_2}"
            output = int(eval(operation))
            print(f"{operation}={output}")
            stack.append(output)
        return int(stack[-1])