class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        toReturn = ""

        # is there a cleaner way to accomplish this? 
        # can iterate through each string an place in an array the size of the final string, then convert to string
        # could determine which string is longer to begin with, then just iterate to that index on each string then append the rest onto the end


        w1, w2 = 0, 0
        res = []
        while w1 < len(word1) and w2 < len(word2):
            res.append(word1[w1])
            res.append(word2[w2])
            w1+=1
            w2+=1

        res.append(word1[w1:])
        res.append(word2[w2:])

        return "".join(res)
            

