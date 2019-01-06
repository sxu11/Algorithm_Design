
'''
Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.



Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]


Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6

'''


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # TODO: when x or y is 1..
        if x == 1 and y == 1:
            if x + y <= bound:
                return [2]
            else:
                return []

        ress = []
        import numpy as np
        if x == 1:
            j_max = int(np.log(bound - 1) / np.log(y)) + 1
            cur_j = 1
            for j in range(j_max + 1):
                if 1 + cur_j <= bound:
                    ress.append(1 + cur_j)
                else:
                    break
                cur_j *= y
            return ress

        if y == 1:
            i_max = int(np.log(bound - 1) / np.log(x)) + 1
            cur_i = 1
            for i in range(i_max + 1):
                if 1 + cur_i <= bound:
                    ress.append(1 + cur_i)
                else:
                    break
                cur_i *= x
            return ress

        i_max = int(np.log(bound) / np.log(x)) + 1
        j_max = int(np.log(bound) / np.log(y)) + 1

        cur_i = 1
        for i in range(i_max + 1):
            cur_j = 1
            for j in range(j_max + 1):
                if cur_i + cur_j <= bound:
                    ress.append(cur_i + cur_j)
                else:
                    break
                cur_j *= y
            cur_i *= x
        return list(set(ress))

