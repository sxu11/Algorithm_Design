"""
TwoSum.py


The first

Created on 2018-10-27
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
            # use dict
            val2ind_dict = {}
            for i in range(len(nums)):
                num = nums[i]
                if target - num in val2ind_dict:
                    return [val2ind_dict[target - num], i]
                else:
                    val2ind_dict[num] = i

import unittest
class TesTwoSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        nums = [7, 7, 1, 4]
        target = 14

        actual_res = self.s.twoSum(nums, target)
        expect_res = [0, 1]
        self.assertEqual(actual_res, expect_res)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TesTwoSum))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())