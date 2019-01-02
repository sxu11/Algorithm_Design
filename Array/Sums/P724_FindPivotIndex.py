'''

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].


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

