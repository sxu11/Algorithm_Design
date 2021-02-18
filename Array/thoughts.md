2Sum based:
- Use dict to make exact search so easy
- Variations I:
  - 2SumCls [170] w/ add & find, use what data structure? use {num:cnt} dict to still handle find in O(N); careful of same num
- Variations II:
  - 3Sum, use a helper func: find2Sum 
  - 3SumClosest (16), enumerate all I,J, binary search (BS) proper k from K
    - modified BS with final abs check (optimal index could be l, could be l-1)
    - Harder version: Closest Subsequence Sum [1755], need to add Subsets [78]
  - 3SumSmaller [259], use varied helper func on sorted array: cnt2SumSmaller
  - 4Sum: TODO

- Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Details: 
- When iter i,j,k, remember range of i is len-2
- WordBreak [139], use dict (can represent 3 states: not seen/true/false) instead of set's 2 states (true/other). In this problem, need to memorize/differentiate whether it is false/not seen to avoid TLE. 

- LongestPalindromicSubstring [5]
  - Stupid idea: O(n^3)
    a. iter all mid pt
    b. iter all expansion
    c. check if expansion is valid palindromic
  - Good idea is to combine a-c

Quotes:
- Subsets:
  - Try to build a directed graph in which node x connects to node y (y > x). For example, if the given set is [0,1,2,3,4], then:
    - node 0 is connected to node 1, 2, 3, 4
    - node 1 is connected to node 2,3,4
    - node 2 is connected to node 3,4
    - node 3 is connected to node 4
    - Then you do dfs. At the moment of visiting each node, you add the traced path to result.