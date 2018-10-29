"""
P1_TwoSum_Extended.py

The previous P1_TwoSum.py assumes "has one and only one answer".
Now try to find "all answers" if any (no duplicate).
"""

class Solution(object):
    def twoSum_extended(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        method = 0

        all_res = []
        if method == 0:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        all_res.append([i,j])

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

        return all_res

