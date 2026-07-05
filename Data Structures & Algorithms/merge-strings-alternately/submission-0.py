class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        toReturn = ""

        w1 = 0
        w2 = 0
        first = True
        while w1 < len(word1) and w2 < len(word2):
            if first:
                toReturn += word1[w1]
                w1+=1
                first = False
            else:
                toReturn += word2[w2]
                w2+=1
                first = True

        if w1 < len(word1):
            toReturn += word1[w1:]
        
        if w2 < len(word2):
            toReturn += word2[w2:]

        return toReturn
            

