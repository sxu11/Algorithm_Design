
'''
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