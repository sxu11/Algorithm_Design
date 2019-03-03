'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
'''


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        len_A = len(A)

        used_inds = [-1] * K
        used_num = 0

        longest_len = 0
        cur_len = 0

        if K == 0:
            i = 0
            while i < len_A:
                if A[i] == 0:
                    cur_len = 0
                else:
                    cur_len += 1
                    longest_len = max(longest_len, cur_len)

                i += 1
            return longest_len

        i = 0
        while i < len_A:
            if A[i] == 0:
                if used_num < K:
                    used_inds[used_num] = i
                    used_num += 1

                else:
                    # find how many are lost
                    m = used_inds[0] - 1
                    while m >= 0 and A[m] == 1:
                        m -= 1
                    cur_len -= used_inds[0] - m
                    used_inds = used_inds[1:] + [i]

                # find how many extra 1's are linked
                j = i + 1
                while j < len_A and A[j] == 1:
                    j += 1
                cur_len += j - i

                i = j

                pass
            else:
                i += 1
                cur_len += 1
                pass

            longest_len = max(longest_len, cur_len)
        return longest_len