class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in pairs:
                stack.append(char)
            elif char in pairs:
                if not stack:
                    return False
                else:
                    x = stack.pop()
                if x != pairs[char]:
                    return False
        if not stack:
            return True
        else:
            return False