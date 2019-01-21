

'''

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.



Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1


Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9


'''


class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2:
            return len(A)

        if A[0] < A[1]:
            cur_sign = 1
        elif A[0] > A[1]:
            cur_sign = -1
        else:
            cur_sign = 0

        max_len = 2
        cur_len = 2
        for i in range(2, len(A)):
            if A[i - 1] == A[i]:
                cur_sign = 0
                cur_len = 1
            elif A[i - 1] < A[i]:
                if cur_sign == -1:
                    cur_len += 1
                    cur_sign = 1
                    max_len = max(max_len, cur_len)  # could be optimized
                # elif cur_sign == -1:
                #     cur_sign = 1
                #     cur_len = 2
                else:
                    cur_sign = 1
                    cur_len = 2
            else:
                if cur_sign == 1:
                    cur_sign = -1
                    cur_len += 1
                    max_len = max(max_len, cur_len)  # could be optimized
                # elif cur_sign == -1:
                #     cur_sign = 1
                #     cur_len = 2
                else:
                    cur_sign = -1
                    cur_len = 2
        return max_len
