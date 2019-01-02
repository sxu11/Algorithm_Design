
'''

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?




This problem ROCKs!

In problems like "equal", "closest",
one tries to find THE OPTIMAL:
                if alist[i] + alist[j] < atarget:
                    anum_smaller += 1
but for "smaller", there is A RANGE.
                if alist[i] + alist[j] < atarget:
                    anum_smaller += j-i

...
'''


class Solution(object):

    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_sorted = sorted(nums)


        def find_smaller(alist, atarget):
            # sorted list
            i = 0
            j = len(alist) - 1

            anum_smaller = 0
            while i < j:
                if alist[i] + alist[j] < atarget:
                    anum_smaller += j-i
                    i += 1
                else:
                    j -= 1

            return anum_smaller

        num_smaller = 0
        for i in range(len(nums_sorted) - 2):
            num_smaller += find_smaller(nums_sorted[i + 1:], target - nums_sorted[i])

        return num_smaller