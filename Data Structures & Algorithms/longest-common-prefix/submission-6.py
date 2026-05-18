class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        smallestString = 0
        for i in range(len(strs)):
            if len(strs[i]) < len(strs[smallestString]):
                smallestString = i

        # somehow compare the maxprefixstring to all other strings
        for prefixIndex in range(len(strs[smallestString])):
            for s in strs:
                if s[prefixIndex] != strs[smallestString][prefixIndex]:
                    return strs[smallestString][:prefixIndex]
            

        #understand why this is true.... if you get all the way through, the whole string is the prefix
        return strs[smallestString]

        #pick an arbitrary string amongst them? or find shortest string amongst them? 
        #for each character in shortest string, make sure all characters found in other strings match
        # add to prefix if match, return result if no match
