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
    """
    Case 1:
    1,1,...,1,2,...,m-2,
    """
    if m <= i:
        res += (m - 1) * m / 2 + (i - m)
    else:
        res += (2 * m - i) * (i - 1) / 2

    # cur = m
    # for j in range(i+1,n):
    #     if cur > 1:
    #         cur -= 1
    #     else:
    #         cur = 1
    #     res += cur

    #     use n-i to replace (i-1), or use n-i+1 to replace i
    if m <= n - i + 1:
        res += (m - 1) * m / 2 + (n - i + 1 - m)
    else:
        res += (2 * m - (n - i + 1)) * (n - i) / 2  # (2*m-n+i)*(n-i-1)/2
    return int(res)


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 0
        r = maxSum
        while l < r:
            m = (l + r + 1) // 2  # int((l+r)/2)
            # if getMinArraySum(m, index, n) > maxSum:
            #     r = m
            # else:
            #     l = m + 1
            if getMinArraySum(m, index + 1, n) <= maxSum:
                l = m
            else:
                r = m - 1

        """ 
        Binary Search Weakness!!!
        How to find the m, that,
        getMinArraySum(m+1) > maxSum,
            - need to make sure getMinArraySum(r) > maxSum
        getMinArraySum(m) <= maxSum
            - getMinArraySum(l) <= maxSum
        """
        """ OK I gave up!! """
        # if getMinArraySum(l,index,n) > maxSum:
        #     return l-1
        # else:
        #     return l
        return l