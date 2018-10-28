'''

Solved with Method 2 of Problem #1.

Speical: "Your returned answers (both index1 and index2)
are not zero-based."
DO remember to convert 1-based inds when indexing
(NOT just intializing like i = 1, j = len(numbers)).

2018-10-28
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 1
        j = len(numbers)
        while i < j:
            if numbers[i - 1] + numbers[j - 1] == target:
                return [i, j]
            elif numbers[i - 1] + numbers[j - 1] < target:
                i += 1
            else:
                j -= 1

import unittest
class TesTwoSumII(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
        nums = [2,7,11,15]
        target = 9

        actual_res = self.s.twoSum(nums, target)
        expect_res = [1,2]
        self.assertEqual(actual_res, expect_res)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TesTwoSumII))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())