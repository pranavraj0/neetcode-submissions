class Solution:
    def isValid(self, s: str) -> bool:
        # first index equal to last
        # pop first and last
        # recurse
        stack = []
        

        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
            elif len(stack) == 0:
                    return False
            else:
                if stack[-1] == '(' and c != ')' or stack[-1] == '{' and c != '}' or stack[-1] == '[' and c != ']':
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

                