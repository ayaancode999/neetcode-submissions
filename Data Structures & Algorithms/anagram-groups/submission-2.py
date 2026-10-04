class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in word:
                word[key] = []
            word[key].append(s)
        return list(word.values())