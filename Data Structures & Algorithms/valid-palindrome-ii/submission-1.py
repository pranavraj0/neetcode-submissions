class Solution:
    def validPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        

        l, r = 0, len(newStr) - 1

        while l < r:
            if newStr[l] != newStr[r]:
                return newStr[l+1:r + 1] == newStr[l + 1:r + 1][::-1] or newStr[l:r] == newStr[l:r][::-1]
            else:
                l +=1
                r-=1
        return True
            


        


        