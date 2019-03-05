
Solutions to tree problems are relatively easy to come up. Here I study several special trees.

Trie:
From wiki, a trie, also called digital tree, radix tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings.

Example: 
For keys {"A", "to", "tea", "ted", "ten", "i", "in", and "inn"}:
            None
    t       A(15)       i(11)
to(7)      te              in(5)
    tea(3) ted(4) ten(12)     inn(9)

Insight:
Node does not have key, but the key info is in its POSITION.

Application:
Both Insert and Find runs in O(n) time, where n is the length of the key. 
Save space if many common prefixes exist (Similar to a nested dictionary?). 