class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_stack = []
        for index, operation in enumerate(operations):
            if operation == "+":
                my_stack.append(int(my_stack[-1]) + int(my_stack[-2]))
            elif operation == "D":
                my_stack.append(2 * int(my_stack[-1]))
            elif operation == "C":
                my_stack.pop()
            else:
                my_stack.append(int(operations[index]))
        return sum(my_stack)
        