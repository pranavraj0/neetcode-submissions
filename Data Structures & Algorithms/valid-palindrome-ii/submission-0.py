class Solution:
    def validPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()


        if newStr == newStr[::-1]:
            return True
        else:
            for i in range(len(s) - 1):
                strRemoved = newStr[:i] + newStr[i+1:]
                if strRemoved == strRemoved[::-1]:
                    return True
        return False
        