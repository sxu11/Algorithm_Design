
'''

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