class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force -> sort all of the strings
        sorted_strings = []
        for i in range(len(strs)):
            sorted_strings.append(("".join(sorted(strs[i])), i))
        
        to_return = []

        sorted_strings = sorted(sorted_strings)
        print(sorted_strings)
        current = [strs[sorted_strings[0][1]]]
        for i in range(1, len(sorted_strings)):
            if sorted_strings[i][0] == sorted_strings[i - 1][0]:
                current.append(strs[sorted_strings[i][1]])
            else:
                to_return.append(current)
                current = [strs[sorted_strings[i][1]]]
        
        to_return.append(current)
        
        return to_return  



