class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # how to compare letters and frequency? only 26 lowercase letters... 
        # initialize array of 26, compare arrays? 
        frequency_map = {}
        for i in range(len(strs)):
            frequency = [0] * 26
            for char in strs[i]:
                frequency[ord(char) - 97] +=1
            
            if tuple(frequency) in frequency_map:
                frequency_map[tuple(frequency)].append(i)
            else:
                frequency_map[tuple(frequency)] = [i]
        
        to_return = []
        for indices in frequency_map.values():
            current = []
            for index in indices:
                current.append(strs[index])
            to_return.append(current)
        return to_return
            
