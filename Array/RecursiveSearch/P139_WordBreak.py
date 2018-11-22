'''
Dynamical programming is really easy.
Just brutal force + Memory.

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

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        record_dict = {}

        def breakable(s):
            if not s:
                return True

            elif len(s) == 1:
                return s in wordDict

            else:
                '''
                Forgot this part!!!
                '''
                if s in wordDict:
                    return True
                # len >= 2
                # catsandog
                # c|atsandog
                # catsando|g
                # [:i], [i:]
                for i in range(1, len(s)):
                    # if breakable(s[:i]) and breakable(s[i:]):
                    #     return True
                    if s[:i] in record_dict:
                        left_res = record_dict[s[:i]]
                    else:
                        left_res = breakable(s[:i])
                        record_dict[s[:i]] = left_res

                    if s[i:] in record_dict:
                        right_res = record_dict[s[i:]]
                    else:
                        right_res = breakable(s[i:])
                        record_dict[s[i:]] = right_res

                    if left_res and right_res:
                        return True
                return False

        return breakable(s)
