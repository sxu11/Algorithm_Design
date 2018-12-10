class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        my_dict = dict(zip(order, "abcdefghijklmnopqrstuvwxyz"))

        words_mapped = []
        for word in words:
            word_mapped = [my_dict[x] for x in word]
            words_mapped.append(''.join(word_mapped))
        return words_mapped == sorted(words_mapped)

        # ptrs = [0] * len(words)
        # while True:
        #     cur_elements = []
        #     all_ended = True
        #     for i in range(len(words)):
        #         if ptrs[i] < len(words[i]):
        #             cur_elements.append(my_dict[words[i][ptrs[i]]])
        #             all_ended = False
        #             ptrs[i] += 1
        #     if all_ended:
        #         return True
        #     else:
        #         if cur_elements != sorted(cur_elements):
        #             return False


