class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #make seperate lists for both of them which are sorted 
        #if they are the same return true for anagrams else false
        if sorted(s)==sorted(t):
            return True
        else:
            return False