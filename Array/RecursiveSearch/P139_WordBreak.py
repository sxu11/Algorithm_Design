'''
Dynamical programming is really easy.
Just brutal force + Memory.
(brainless way, using dictionary instead of array. )

After


Stephen:
def wordBreak(self, s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]


SomeOneElse123's improvement:
words should be a set to get a O(1) lookup:
This changes the complexity of the approach, independent of the specific task
we don't have to check substrings against the dictionary that are longer than the longest entry in it
Could be considered a heuristic, as it's effect massively depends on the words.
def wordBreak(self, s, words):
    ok = [True]
    max_len = max(map(len,words+['']))
    words = set(words)
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
    return ok[-1]
'''

'''
Index-based comparison, 408 ms. 
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        record_dict = {}
        wordDict = set(wordDict)

        '''
        Method 1: dp[i] means wordDict[:i] is good
        '''
        # TODO: do it when necessary

        '''
        Method 2: indices based dictionary
        '''

        #         def breakable(i,j): # whether s[i:j] is breakable
        #             if i==j:
        #                 return True

        #             elif j-i == 1:
        #                 return s[i:j] in wordDict

        #             else:
        #                 '''
        #                 Forgot this part!!!
        #                 '''
        #                 if s[i:j] in wordDict:
        #                     return True
        #                 for k in range(i+1,j):
        #                     if (i,k) in record_dict:
        #                         left_res = record_dict[(i,k)]
        #                     else:
        #                         left_res = breakable(i,k)
        #                         record_dict[(i,k)] = left_res

        #                     if (k,j) in record_dict:
        #                         right_res = record_dict[(k,j)]
        #                     else:
        #                         right_res = breakable(k,j)
        #                         record_dict[(k,j)] = right_res

        #                     if left_res and right_res:
        #                         return True
        #                 return False

        #         return breakable(0, len(s))

        '''
        Method 3: substring based dictionary
        '''
#         def breakable(s):
#             if not s:
#                 return True

#             elif len(s) == 1:
#                 return s in wordDict

#             else:
#                 '''
#                 Forgot this part!!!
#                 '''
#                 if s in wordDict:
#                     return True
#                 # len >= 2
#                 # catsandog
#                 # c|atsandog
#                 # catsando|g
#                 # [:i], [i:]
#                 for i in range(1,len(s)):
#                     # if breakable(s[:i]) and breakable(s[i:]):
#                     #     return True
#                     if s[:i] in record_dict:
#                         left_res = record_dict[s[:i]]
#                     else:
#                         left_res = breakable(s[:i])
#                         record_dict[s[:i]] = left_res

#                     if s[i:] in record_dict:
#                         right_res = record_dict[s[i:]]
#                     else:
#                         right_res = breakable(s[i:])
#                         record_dict[s[i:]] = right_res

#                     if left_res and right_res:
#                         return True
#                 return False

#         return breakable(s)