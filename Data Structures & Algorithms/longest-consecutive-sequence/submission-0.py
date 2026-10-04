class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put in a set
        filtered = {num : "start of sequence" for num in nums}
        # check if it is a sequence
        for num in nums:
            if num - 1 in filtered:
                filtered[num] = "smaller number exists"
        # extract the length of sequence
        max_length = 0
        for num, start_of_seq in filtered.items():
            if start_of_seq == "start of sequence":
                current_num = num
                streak = 1
                while current_num + 1 in filtered:
                    current_num += 1
                    streak +=1
                max_length = max(max_length, streak)
        return max_length
