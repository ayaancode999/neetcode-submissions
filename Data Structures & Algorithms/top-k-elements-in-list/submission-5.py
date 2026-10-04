class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = {}
        for num in nums:
            key = num
            if key not in n:
                n[key] = 0
            n[key] += 1
        # print(n)
        n2 = sorted(n, key = n.get)
        n2.reverse()
        # print(n2)
        n3 = []
        for i in range(0,k):
            # print(n2[i])
            n3.append(n2[i])
        return n3

        