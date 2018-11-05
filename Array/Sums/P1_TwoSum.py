"""
TwoSum.py


Method 0: 4612 ms, beats 16%
Brutal force (n^2), 'cause there seems
no trick to play (list is not ordered).
(DO remember j starts from i+1, not i)

But, there IS potential redundant examination of
elements.
For example, in the worse case, the last element
will be examined n-1 times.

Method 1: 24 ms, beats 88%
is transforming the problem into a familiar form,
sorted list (nlogn).
However, it is a little dirty to (DO remember!) map back the indices

In particular, there is logic flaw, if trying to find
nums_sorted[i] & nums_sorted[j] from nums again.
(Consider the case nums_sorted[i] == nums_sorted[j])

Also, cannot use i_true = None as initial condition
and "not i_true" as condition. Since i_true = 0 is possible...

Method 2: 24 ms, beats 88%
TODO: Why above two methods have the exact same running time?!
Use 1 indexing and 1 hashing, which uses const time.

Created on 2018-10-27


TODO: Current solutions assume "has one and only one answer".
In the future, devleop into "find all answers".
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        method = 1

        if method == 0:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]

        elif method == 1:
            nums_sorted = sorted(nums)
            i = 0
            j = len(nums) - 1
            while i < j:
                if nums_sorted[i]+nums_sorted[j] == target:
                    break
                elif nums_sorted[i]+nums_sorted[j] < target:
                    i += 1
                else:
                    j -= 1

            i_true, j_true = float('nan'), float('nan')
            for k in range(len(nums)):
                if nums[k]==nums_sorted[i] and i_true != i_true:
                    i_true = k
                elif nums[k]==nums_sorted[j]:
                    j_true = k

            return [i_true, j_true]

        elif method == 2:
            # use dict
            val2ind_dict = {}
            for i in range(len(nums)):
                num = nums[i]
                if target - num in val2ind_dict:
                    return [val2ind_dict[target - num], i]
                else:
                    val2ind_dict[num] = i

