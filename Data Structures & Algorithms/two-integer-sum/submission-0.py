class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#make a first loop going through the elements
        for i in range(len(nums)):
#make a second loop that adds the element next to it
            for j in range(i+1,len(nums)):
              if nums[i]+nums[j]==target:
                return [i,j]
                
#find the index of two numbers that add up to the target number
#return them
    
       