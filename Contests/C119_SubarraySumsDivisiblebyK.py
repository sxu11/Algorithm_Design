
'''
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.



Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        cumsums = {0: 1}
        cur_cumsum = 0

        num_res = 0
        for a in A:
            if a % K == 0:
                num_res += 0

            cur_cumsum = (cur_cumsum + a) % K
            cur_num = cumsums.get(cur_cumsum, 0)
            num_res += cur_num
            cumsums[cur_cumsum] = cur_num + 1
        return num_res


