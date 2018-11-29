

'''
Comment on 2018-11-24, actually WRONG!
When looking forward, you confuse (from dp[i][j] to dp[i+1][j],dp[i][j+1],dp[i+1][j+1]???)
When looking forward, there is the solution (from dp[i-1][j-1],dp[i-1][j],dp[i][j-1] to dp[i][j])
'''


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        #         '''
        #         Method 1: Brutal force (forward recursive)
        #         '''

        #         if word1 == "":
        #             return len(word2)
        #         elif word2 == "":
        #             return len(word1)
        #         else:
        #             if word1[0] == word2[0]:
        #                 return self.minDistance(word1[1:], word2[1:])
        #             else:
        #                 return min([self.minDistance(word1, word2[1:]),
        #                             self.minDistance(word1[1:], word2),
        #                             self.minDistance(word1[1:], word2[1:])
        #                            ]) + 1

        '''
        Method 2: Brutal force (forward recursive) w/ memory
        '''
        max_int = 100000000
        d = [[max_int] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        def minDist(i, j):  # distance between word1[i:] and word2[j:]
            if i == len(word1):
                return len(word2) - j
            elif len(word2) == j:
                return len(word1) - i
            else:
                if word1[i] == word2[j]:
                    if d[i][j] == max_int:
                        d[i][j] = minDist(i + 1, j + 1)
                    return d[i][j]
                else:
                    if d[i][j + 1] == max_int:
                        d[i][j + 1] = minDist(i, j + 1)
                    if d[i + 1][j] == max_int:
                        d[i + 1][j] = minDist(i + 1, j)
                    if d[i + 1][j + 1] == max_int:
                        d[i + 1][j + 1] = minDist(i + 1, j + 1)
                    return min([d[i][j + 1],
                                d[i + 1][j],
                                d[i + 1][j + 1]
                                ]) + 1

        return minDist(0, 0)