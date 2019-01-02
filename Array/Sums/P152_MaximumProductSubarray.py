'''

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Supposed solved the prob for nums[:i]
        Know: (1) maxProduct of nums[:i]
        (2) maxProduct of nums[:i] ending with nums[i-1]
        (3) minProduct of nums[:i] ending with nums[i-1]

        w/ nums[i]
        if nums[i] is positive:
        if nums[i] is negative:

        '''
        if len(nums) == 0:
            return 0

        maxProdEnd = nums[0]
        minProdEnd = nums[0]
        maxProd = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                maxProdEnd = max(nums[i], maxProdEnd * nums[i])  # WRong! maxProdEnd *= nums[i]
                minProdEnd = min(nums[i], minProdEnd * nums[i])  # WRong! minProdEnd *= nums[i]

            elif nums[i] < 0:
                maxProdEnd, minProdEnd = max(nums[i], minProdEnd * nums[i]), min(nums[i], maxProdEnd * nums[i])

            else:
                maxProdEnd, minProdEnd = 0, 0

            maxProd = max(maxProdEnd, maxProd)
        return maxProd





