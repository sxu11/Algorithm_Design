class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        cached = dict()  # ss: [(word1, word2, word3..), (word1, word2, word4), ...]

        def crossCombineValues(tuples1, tuples2):
            res = []
            for tuple1 in tuples1:
                for tuple2 in tuples2:
                    res.append(tuple1 + tuple2)
            return res

        def getBreakableTuples(ss):
            if ss in cached:
                return cached[ss]
            # elif ss in wordDict:
            # cached[ss] = [(ss,)]
            if ss in wordDict:
                cached[ss] = [(ss,)]
            else:
                cached[ss] = []
            # if ss not in cached:
            # cached[ss] = []
            for i in range(len(ss)):
                ss1 = ss[:i]
                ss2 = ss[i:]
                tuple1s = getBreakableTuples(ss1)
                tuple2s = getBreakableTuples(ss2)
                if tuple1s and tuple2s:
                    res = crossCombineValues(tuple1s, tuple2s)
                    cached[ss] += res

            return cached[ss]

        getBreakableTuples(s)

        resInTuples = cached[s]
        res = []
        for tuple1 in resInTuples:
            res.append(' '.join(tuple1))
        return list(set(res))
