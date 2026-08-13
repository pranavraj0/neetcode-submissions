class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_map = {')': '(', '}':'{', ']': '['}

        for i in s:
            if i in close_map.values():
                stack.append(i)
            else:
                if stack and close_map[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return False if stack else True

        