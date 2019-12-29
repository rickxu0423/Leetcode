class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append( (x, min(x, self.getMin())) )

    def pop(self) -> None:
        if len(self.stack) == 0: return None
        return self.stack.pop()[0]

    def top(self) -> int:
        if len(self.stack) == 0: return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0: return float('inf')
        return self.stack[-1][1]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) #-3
    minStack.pop()
    print(minStack.top()) #0
    print(minStack.getMin()) #-2