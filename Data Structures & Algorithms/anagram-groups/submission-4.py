from functools import reduce
from itertools import groupby
from operator import mul
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        # 1. Lambda function to calculate the prime product key for any given word
        get_prime_hash = lambda word: reduce(mul, map(lambda char: primes[ord(char) - 97], word), 1)
        
        # 2. itertools.groupby requires the input collection to be sorted by the grouping key first
        sorted_strs = sorted(strs, key=get_prime_hash)
        
        # 3. Group the sorted elements and extract the lists
        return [list(group) for key, group in groupby(sorted_strs, key=get_prime_hash)]
