class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums2=set()
        # for num in nums:
        #     nums2.add(num)
        # print(nums2)
        # if len(nums2)==len(nums):
        #     return False
        # else:
        #     return True
        arr=set(nums)
        if len(arr)==len(nums):
            return False
        else:
            return True