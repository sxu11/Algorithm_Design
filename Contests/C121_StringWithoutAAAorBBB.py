
'''
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.


Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"


Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
'''


class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ""
        if A > B:
            for i in range(B):
                if i < A - B:
                    res += "aab"
                else:
                    res += "ab"
            for i in range(A - 2 * B):
                res += 'a'
        else:
            for i in range(A):
                if i < B - A:
                    res += "bba"
                else:
                    res += "ba"
            for i in range(B - 2 * A):
                res += 'b'
        return res


