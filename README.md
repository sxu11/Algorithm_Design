
Essence of many algorithms: avoid repeated searching


Data structures that I always forget:
- Priority queue
    - One (and the best?) way to do this is using heap
    - Heaps are binary trees for which every parent node has a value less than or equal to any of its children. 
    
    - This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, 
    counting elements from zero.
    
    - Example:
        - h = []
        - heappush(h, (5, 'write code'))
        - heappush(h, (7, 'release product'))
        - heappush(h, (1, 'write spec'))
        - heappush(h, (3, 'create tests'))
        - heappop(h): 
            (1, 'write spec')
            
    - Complexity:
        - Insertion: O(logn)
        - Pop: O(logn)
        - Build a heap by inserting 1 element a time: O(nlogn)
        - Build a heap w/ all elements all at once: O(n) with Floyd's algorithm 
        - Variation: Only keep the k-th largest elements. Discard if smaller than the root.
    
    

List of e.g.'s:


- Using "find in set O(1) is faster than find in list O(n)":
    - Time-space tradeoff

    Example, brutal force, what is wasted, how to memorize
    - Two sum, 
    scan twice, 
    "know the target (given), so know what is wanted, 
        most naturally want to do if (target-num) in nums"
    "'in' takes O(n) in array, but takes O(1) in set"
        - the current problem wants information from all previous
        steps (easy to formulate, store whatever encountered!)
    
    - Three sum, 
    scan three times,
    "",
    "(1)Make use of (modified) TwoSum,
    (2)De-duplicate results
    "
    
    - Four sum,

- Using "find in a structured array, instead of re-calculation"
    - recursive with memorization (replace dynamical programming?)
        - This is easy, since recursive is simplest way of constructing how the current
        problem RELATES to a sub-problem

- Using special data structures to save previous results
    - 