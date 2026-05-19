class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # some sort of hash map with values being lists? and keys being the sorted? 

        anagram_map = {}

        for i in range(len(strs)):
            sorted_string = "".join(sorted(strs[i]))
            if sorted_string in anagram_map:
                anagram_map[sorted_string].append(i)
            else:
                anagram_map[sorted_string] = [i]
        
        to_return = []

        for k in anagram_map:
            current = []
            for i in anagram_map[k]:
                current.append(strs[i])
            to_return.append(current)
        return to_return