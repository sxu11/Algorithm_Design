def getMinArraySum(m, i, n):
    """ can better optimize by not using for loop, but math here...

    brain messed up in last few minutes!!!
    """
    res = m
    # cur = m
    # for j in range(i-1,-1,-1):
    #     if cur > 1:
    #         cur -= 1
    #     else:
    #         cur = 1
    #     res += cur
    if m < i:
        res += (m - 1) * m / 2 + (i - m)
    else:
        res += (2 * m - i + 2) * m / 2

    cur = m
    # for j in range(i+1,n):
    #     if cur > 1:
    #         cur -= 1
    #     else:
    #         cur = 1
    #     res += cur
    if m < n - i - 1:
        res += (m - 1) * m / 2 + (n - i - 1 - m)
    else:
        res += (2 * m - n + i + 1 + 2) * m / 2
    return res


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 0
        r = maxSum
        while l < r:
            m = int((l + r) / 2)
            # print(l,m,r)
            if getMinArraySum(m, index, n) > maxSum:
                r = m
            else:
                l = m + 1

        """ 
        Binary Search Weakness!!!
        How to find the m, that,
        getMinArraySum(m+1) > maxSum,
            - need to make sure getMinArraySum(r) > maxSum
        getMinArraySum(m) <= maxSum
            - getMinArraySum(l) <= maxSum
        """
        """ OK I gave up!! """
        if getMinArraySum(l, index, n) > maxSum:
            return l - 1
        else:
            return l