class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create lists for each amount of length
        #compare the lists if they are anagrams 
        #return pairs into a list 
        words = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in words:
                words[key] = []
            words[key].append(word)
        return list(words.values())