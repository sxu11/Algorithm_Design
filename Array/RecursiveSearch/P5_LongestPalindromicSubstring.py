class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if len_s <= 1:
            return s

        '''
        method 1: brutal force (fast enough)
        
        Not really a Dynamical Programming. 
        
        May worth checking out Manacher's algorithm: 
        https://en.wikipedia.org/wiki/Longest_palindromic_substring
        '''
        #
        max_len = 1
        max_palindrome = s[0]

        ## find things like aba
        for i in range(1, len_s):
            cur_max = 1
            for j in range(1, min(i + 1, len_s - i)):
                if s[i - j] == s[i + j]:  # s[0] and s[len_s-1] should be the limits
                    cur_max += 2
                else:
                    j -= 1
                    break
            if cur_max > max_len:
                max_len = cur_max
                max_palindrome = s[i - j:i + j + 1]

        ## find things like bb
        for i in range(0, len_s):  # Wrong: range(1,len_s)
            cur_max = 0
            for j in range(0, min(i + 1, len_s - i - 1)):
                if s[i - j] == s[i + 1 + j]:  # s[0] and s[len_s-1] should be the limits
                    cur_max += 2
                else:
                    j -= 1
                    break
            if cur_max > max_len:
                max_len = cur_max
                max_palindrome = s[i - j:i + j + 2]  # Wrong: s[i-j:i+j]

        return max_palindrome

