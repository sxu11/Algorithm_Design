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
                """only in this case (ss processed), we don't need proceed"""
                return cached[ss]
            if ss in wordDict:
                """even in this case (ss self in), we need see if substr in
                for e.g. even if 'aa' was in dict, maybe 'a' was also in!"""
                cached[ss] = [(ss,)]
            else:
                cached[ss] = []
            for i in range(len(ss)): """here, don't need to worry about i=0,
            because once ss cached, won't do repeated processing
                BUT still need to handle above 'ss in dict' case, which is 
            actually the only place where we do the core logic: in dict?
            """
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
