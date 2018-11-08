
'''
Question:
Given an array of integers and an integer k, you need to find the total
number of continuous subarrays whose sum equals to k.

I had a chance to come up w/ the internet solution.

From t -> t+1.
If we solved the problem for t, then new (continuous) subarrays
must contain nums[t+1], which could be nums[0:t+2], nums[1:t+2], ..., nums[t:t+1] (yes, itself!)
However, cannot make a dict that uses (i,j) as k and running sum as value, which
saves any running sum of nums[i:j], which takes n^2 time & space

But, can make a dict that saves running sum of nums[0:j]!!!
The key is the running sum itself. The value is the cnt of such sums.
'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        method = 'recursive'

        if method == 'recursive':  # n^2 time, 1 space; TLE
            if len(nums) == 1:
                if nums[0] == k:
                    return 1
                else:
                    return 0

            tot_cnt = self.subarraySum(nums[:-1], k)

            cur_sum = nums[-1]
            if cur_sum == k:  # forgot to check this!
                tot_cnt += 1
            for i in range(len(nums[:-1]) - 1, -1, -1):
                cur_sum += nums[i]
                if cur_sum == k:
                    tot_cnt += 1
            return tot_cnt

        elif method == 'recursive':  # n^2 time, 1 space; TLE
            tot_cnt = 0
            for i in range(len(nums)):
                '''
                if nums[i] == k:
                    tot_cnt += 1
                if nums[i]+nums[i-1] == k:
                    tot_cnt += 1
                ...
                if nums[i]+nums[i-1]+...nums[0] == k:
                    tot_cnt += 1
                '''
                cur_sum = k
                if cur_sum == k:
                    tot_cnt += 1
                for j in range(i - 1, -1, -1):
                    cur_sum += nums[j]
                    if cur_sum == k:
                        tot_cnt += 1
            return tot_cnt

        elif method == 'internet': # n time, n space, out of my reach ...
            # https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation

            count, cur, res = {0: 1}, 0, 0
            for v in nums:
                cur += v
                res += count.get(cur - k, 0)
                count[cur] = count.get(cur, 0) + 1
            return res




