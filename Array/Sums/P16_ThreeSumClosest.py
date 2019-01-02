
'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).



When dealing with three-dim iterations,
pay special attention to range:
for i in range(len(nums_sorted)-2):
'''

class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_sorted = sorted(nums)
        closest = sum(nums_sorted[:3])

        def find_closest(alist, atarget):
            # sorted list
            i = 0
            j = len(alist) - 1

            cur_closest = alist[i] + alist[j]
            while i < j:
                cur_sum = alist[i] + alist[j]

                if cur_sum == atarget:
                    return atarget
                elif cur_sum < atarget:
                    i += 1
                else:
                    j -= 1

                if abs(cur_sum-atarget) < abs(cur_closest-atarget):
                    cur_closest = cur_sum
            return cur_closest

        for i in range(len(nums_sorted)-2):
            cur_closest = nums_sorted[i] + find_closest(nums_sorted[i+1:], target-nums_sorted[i])
            if abs(cur_closest-target) < abs(closest-target):
                closest = cur_closest

        return closest