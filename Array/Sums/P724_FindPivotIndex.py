'''
Brutal force, THE best!

Two-pter method, but actually more troubles!
        (cannot take care of negative numbers).
Essentially, there is no 'order' when positivity is not promised.
'''


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        leftSum = 0
        rightSum = sum(nums) - nums[0]
        for i in range(len(nums) - 1):
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            rightSum -= nums[i + 1]

        if leftSum == rightSum:
            return len(nums) - 1
        else:
            return -1

        if False:

            i = 0
            j = len(nums) - 1

            leftSum = nums[i]
            rightSum = nums[j]
            while i < j:
                if leftSum > rightSum:
                    j -= 1
                    rightSum += nums[j]
                elif leftSum < rightSum:
                    i += 1
                    leftSum += nums[i]
                else:
                    if j - i == 2:
                        return i + 1
                    elif j - i == 1:
                        j -= 1
                        rightSum += nums[j]
                    else:
                        i += 1
                        j -= 1
                        leftSum += nums[i]
                        rightSum += nums[j]
            if leftSum == rightSum:
                return i
            else:
                return -1

