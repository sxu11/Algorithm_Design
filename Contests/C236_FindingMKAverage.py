"""
1. Most recent m numbers
2. Remove k largest & smallest
3. Average the rest

Most naive:
- add: O(1)
- get: sort O(mlogm), sum O(m-2k)

Double linked list (DLL):
- a DLL to track age
- a sorted list (SL) to keep m

- get: sum O(m-2k)
- add:
  - remove oldest from DLL O(m)
  - find its ind in SL, remove it O(m)
  - SL: search, insert O(m)

heap:
- maintain:
  - total sum
  - smallest heap/sum
  - largest heap/sum
  - (does not need a sorted list?!)

- get: O(1)
- add:
  - if larger than min of largeHeap (logk), update heap & heapSum
  - if smaller than max of smallHeap (logk), update heap & heapSum

"""
