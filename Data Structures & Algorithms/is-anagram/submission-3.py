class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        comparison_s, comparison_t = {}, {}

        for i in range(len(s)):
            comparison_s[s[i]] = 1 + comparison_s.get(s[i], 0)

            comparison_t[t[i]] = 1 + comparison_t.get(t[i], 0)

        for key in comparison_s:
            if comparison_s.get(key) != comparison_t.get(key):
                return False
        return True
        