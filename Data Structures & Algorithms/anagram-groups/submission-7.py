class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in words:
                words[key] = []
            words[key].append(s)
        return list(words.values())
