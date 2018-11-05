'''

Use one module to handle all tests.
TODO: how to set "from XXX import" and "suite.addTest(tester(XXX))" by one command

Created: 2018-10-28
'''


import unittest
class tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_P1(self):
        nums = [7, 7, 1, 4]
        target = 14

        actual_res = self.s.twoSum(nums, target)
        expect_res = [0, 1]
        self.assertEqual(actual_res, expect_res)

    def test_15(self):
        nums = [2,7,11,15]
        target = 9

        actual_res = self.s.threeSum(nums)
        expect_res = [1,2]
        self.assertEqual(actual_res, expect_res)

    def test_167(self):
        nums = [2,7,11,15]
        target = 9

        actual_res = self.s.twoSumII(nums, target)
        expect_res = [1,2]
        self.assertEqual(actual_res, expect_res)

def suite():
    suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(tester))
    suite.addTest(tester("test_167"))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())