class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # store 1 in all empty buckets
        length = len(nums)
        result = [1] * length
        right = [1] * length
        left = [1] * length
        # find right and left products
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(length):
            result[i] = right[i] * left[i]
        # return step 4 
        return result
        