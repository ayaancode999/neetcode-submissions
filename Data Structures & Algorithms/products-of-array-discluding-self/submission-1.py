class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # store 1 in all empty buckets
        result = [1] * len(nums)
        right = [1] * len(nums)
        left = [1] * len(nums)
        # find right and left products
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            result[i] = right[i] * left[i]
        # return step 4 
        return result
        