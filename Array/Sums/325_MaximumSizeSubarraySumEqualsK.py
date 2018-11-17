'''
Very similar to a previous problem

'''


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        my_dict = {0: -1}  # cumSum, ind
        cumSum = 0

        curr_max_len = 0
        for i in range(len(nums)):
            cumSum += nums[i]
            if cumSum - k in my_dict:
                curr_max_len = max(curr_max_len, i - my_dict[cumSum - k])

            if not cumSum in my_dict:
                my_dict[cumSum] = i

        return curr_max_len

