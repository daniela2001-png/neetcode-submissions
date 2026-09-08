class MinStack:

    def __init__(self):
        self.stack = []
        self.p = []


    def validate_len_stack(self) -> bool:
        return not self.stack and not self.p

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.p:
            self.p.append(min(val, self.p[-1]))
        else:
            self.p.append(val)
        

    def pop(self) -> None:
        if self.validate_len_stack():
            raise IndexError()
        self.stack.pop()
        self.p.pop()
        

    def top(self) -> int:
        if self.validate_len_stack():
            raise IndexError()
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.validate_len_stack():
            raise IndexError()
        return self.p[-1]