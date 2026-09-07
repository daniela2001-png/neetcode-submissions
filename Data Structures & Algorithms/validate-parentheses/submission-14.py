class Solution:
    def isValid(self, s: str) -> bool:
        open_parantheses = []
        mapper = {")":"(", "}":"{", "]":"["}
        if len(s) == 1:
            return False
        for char in s:
            if char in mapper.values():
                open_parantheses.append(char)
            if len(open_parantheses) > 0:
                if mapper.get(char) is not None and mapper.get(char) != open_parantheses.pop():
                    return False
            else:
                return False
        if char in mapper.values() and char == open_parantheses.pop():
            return False
        if len(open_parantheses) != 0:
            return False

        return True
            