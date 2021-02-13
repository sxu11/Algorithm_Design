2Sum based:
- Use dict to make exact search so easy
- Variations I:
  - 2SumCls (170) w/ add & find, use what data structure? use {num:cnt} dict to still handle find in O(N); careful of same num
- Variations II:
  - 3Sum, use a helper func: find2Sum 
  - 3SumSmaller (259), use varied helper func on sorted array: cnt2SumSmaller
  - 

- Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.