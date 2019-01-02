'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?



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

