'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]



WARNING: Return vals, not inds (compared to P1_TwoSum)!

Method 0.
0.1 In the i-th step, find n1+n2=-num[i] from nums[i+1:]
0.2 Use twoSum, but revise s.t. returns all solutions
0.3 Remove redundancy (de-duplicate from list of lists)


Method 1.1/1.2
Almost the same, but distribute the task of "Remove redundancy"
in step 0.3, which was performed on the final list of lists
;
to two smaller steps:
I. Remove redundancy when choosing "-target"; O(n) --> O(1)
II (Variation 1.1) Remove redundancy after searched (n1, n2) pairs.
II (Variation 1.2) Remove redundancy when searching (n1, n2) pairs; result correct
in step 0.2.

'''

# class Solution(object):
#
#     def twoSum_extended(self, nums, target, method):
#
#         all_res = []
#
#         i = 0
#         j = len(nums) - 1
#         while i < j:
#             if nums[i] + nums[j] == target:
#                 all_res.append([nums[i],nums[j]])
#
#                 # Remove redundancy II
#                 if method == 1.2:
#                     while nums[i] == all_res[-1][0] and i < j:
#                         i += 1
#                     while nums[j] == all_res[-1][1] and i < j:
#                         j -= 1
#                 else:
#                     i += 1
#                     j -= 1
#             elif nums[i] + nums[j] < target:
#                 i += 1
#             else:
#                 j -= 1
#
#         # deduplicate here!
#
#         if method == 1.1:
#             new_res = []
#             for res in all_res:
#                 if res not in new_res:
#                     new_res.append(res)
#         else:
#             new_res = all_res
#
#         return new_res
#
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         ress = []
#
#         method = 1.1
#
#
#         nums_origin = nums[:]
#         nums = sorted(nums)
#
#         for i in range(len(nums)):
#
#             if method > 1:
#                 if i>0 and nums[i]==nums[i-1]:
#                     continue
#
#             cur_nums = nums[i+1:]
#             target = -nums[i]
#
#             cur_all_res = self.twoSum_extended(cur_nums, target, method)
#             for one_res in cur_all_res:
#                 one_res = [nums[i]] + one_res
#                 ress.append(one_res)
#
#         if method == 0:
#             ress_new = []
#             for res in ress:
#                 if res not in ress_new:
#                     ress_new.append(res)
#
#         nums = nums_origin
#         return ress

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(target, array):
            seen = set()
            res = []
            for num in array:
                if target - num in seen:
                    res.append(sorted([target - num, num, -target]))
                seen.add(num)
            return res

        final_res_set = set()
        for i in range(len(nums)):
            cur_res = twoSum(-nums[i], nums[i + 1:])
            for pair in cur_res:
                final_res_set.add(tuple(pair))
        return list(final_res_set)