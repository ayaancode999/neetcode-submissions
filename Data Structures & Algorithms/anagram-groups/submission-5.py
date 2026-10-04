from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a fixed-size integer array structure internally for keys
        groups = defaultdict(list)
        
        for string in strs:
            # 1. Allocate a fixed array of 26 zeros on the stack frame
            count = [0] * 26
            
            # 2. Populate character frequencies (no string replication)
            for char in string:
                count[ord(char) - 97] += 1
                
            # 3. Convert to an immutable tuple to use as a hash key
            groups[tuple(count)].append(string)
            
        # 4. In-place modification trick: clear the original reference to free memory 
        # while converting the dictionary values to the final output list.
        result = list(groups.values())
        groups.clear() 
        
        return result
