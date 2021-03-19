import numpy as np


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # """
        # n = len(nums)
        # - Make a matrix of dimen (n,n), the (i,j)-th element stores the product of nums[i]*nums[i+1]*...*nums[0]*...*nums[j]
        #     - Construct this matrix from the 0-th row: [0,j]
        # """
        # n = len(nums)
        # dataMatrix = np.zeros((n,n))
        # for i in range(0,n):
        #     for j in range(0,n):
        #         prod = nums[i]
        #         if j>=i:
        #             """nums[i]*nums[i+1]*...*nums[j]"""
        #             for k in range(i+1,j):
        #                 prod *= nums[k]
        #         else:
        #             """nums[i]*...*nums[0]*...*nums[j]"""
        #             for k in range(i+1,n):
        #                 prod *= nums[k]
        #             for k in range(0,j):
        #                 prod *= nums[k]

        """
        (1)*2*3*4, 1*(1)*3*4, 1*2*(1)*4, 1*2*3*(1)
        """
        lefts = [1]
        rights = [1]
        for num in nums[:-1]:
            newLeft = lefts[
                          -1] * num  # TODO: use p to replace lefts[-1] and rights[-1], so no need for using 2 seperate lists
            lefts.append(newLeft)
        for num in nums[1:][::-1]:
            newRight = rights[-1] * num
            rights.append(newRight)
        rights = rights[::-1]

        return [lefts[i] * rights[i] for i in range(len(lefts))]