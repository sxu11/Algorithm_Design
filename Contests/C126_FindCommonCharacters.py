'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
'''


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        all_lowers = 'abcdefghijklmnopqrstuvwxyz'
        print len(all_lowers)
        all_dict = {}
        for lower in all_lowers:
            all_dict[lower] = [0] * len(A)  # the i-th

        for i in range(len(A)):
            for lower in A[i]:
                all_dict[lower][i] += 1

        res = []
        for lower in all_lowers:
            cur_cnt = min(all_dict[lower])
            if cur_cnt > 0:
                res += [lower] * cur_cnt
        return res