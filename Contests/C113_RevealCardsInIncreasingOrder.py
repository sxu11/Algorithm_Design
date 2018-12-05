class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck_copy = deck[:]
        res_deck = []
        while deck:
            res_deck.append(deck[0])
            if len(deck) > 1:
                deck = deck[2:] + [deck[1]]
            else:
                break

        sorted_deck = sorted(deck_copy)
        sorted_inds = []  # sorted_inds[j] is its ind of deck[i] in sorted format
        for i in range(len(deck_copy)):
            sorted_inds.append(sorted_deck.index(deck_copy[i]))

        res = [-1] * len(deck_copy)
        for i in range(len(deck_copy)):
            j = sorted_inds[i]  # deck[i] should be at ind j in the res_deck!
            k = deck_copy.index(res_deck[j])  # who is at ind j in the res_deck? what's its origin ind k?
            res[k] = deck_copy[i]  # put me there!
        return res

