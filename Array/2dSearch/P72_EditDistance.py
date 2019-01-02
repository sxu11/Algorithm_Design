

'''

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Comment on 2018-11-24, actually WRONG!
When looking forward, you confuse (from dp[i][j] to dp[i+1][j],dp[i][j+1],dp[i+1][j+1]???)
When looking backward, there is the solution (from dp[i-1][j-1],dp[i-1][j],dp[i][j-1] to dp[i][j])
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