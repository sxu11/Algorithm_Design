'''
Two pointer method.
Don't use log... "equal" is tricky.
The outer for/while, the inner for/while, really need be careful
'''


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i = 0
        partProd = 1  # product of log_nums[i:j+1]
        combinations = 0
        for j in range(len(nums)):
            partProd *= nums[j]
            while i < j and partProd >= k:
                partProd /= nums[i]
                i += 1

            if partProd < k:
                combinations += j - i + 1

        return combinations

