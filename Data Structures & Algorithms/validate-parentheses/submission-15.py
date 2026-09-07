class Solution:
    def isValid(self, s: str) -> bool:
        """
        Implement a LIFO stack sturcture for open parentheses
        and in each iteration compare the actual char with the latest
        element inserted in our stack (top element) if the current char is not the equivalent close parenthese
        we should marked as an invalid substring. 

        Also we should make sure that at the end of our total iterations
        this stack will be empty, otherwise this means that tha string is NOT a valid
        parentheses.

        the Complexity time of this solution is O(n) and the space one is also O(n) 
        this because of the open_parentheses is gonna grown as equal as the number of 
        open parentheses in the input string. 
        """
        open_parentheses = []
        mapper = {")":"(", "}":"{", "]":"["}
        if len(s) == 1:
            return False
        for char in s:
            if char in mapper.values():
                open_parentheses.append(char)
            if len(open_parentheses) > 0:
                if mapper.get(char) is not None and mapper.get(char) != open_parentheses.pop():
                    return False
            else:
                return False
        if char in mapper.values() and char == open_parentheses.pop():
            return False
        if len(open_parentheses) != 0:
            return False

        return True
            