class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r, s):
            if l == r:
                return
            elif l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1, s)
        reverse(0, len(s) - 1, s)
        
        
        