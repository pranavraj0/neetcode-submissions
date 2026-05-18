class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        #how to find minimum length of array
        maxPrefixLen = 201

        for s in strs:
            if len(s) < maxPrefixLen:
                maxPrefixLen = len(s)

        for i in range(maxPrefixLen):
            currPrefix = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] == currPrefix:
                    currPrefix = strs[j][i]
                else:
                    return "".join(prefix)
            prefix += currPrefix
        return "".join(prefix)



        

        #check if all elements at a single index are the same? how to efficiently do? start with brute force then optimize
        #check the same index for all strings in array of strings and if they are the same, can add to prefix, if not, return