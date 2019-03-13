

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
        - Space: O(n)
        - Insertion: O(logn)
        - Pop: O(logn)
        - Build a heap by inserting 1 element a time: O(nlogn)
        - Build a heap w/ all elements all at once: O(n) with Floyd's algorithm 
        - Variation: Only keep the k-th largest elements. Discard if smaller than the root.

- Double linked list:
    - Complexity:
        - Push/pop: O(1)
        - Search: O(n)
        - Intrinsic order

- Dictionary:
    - Complexity:
        - Push/pop/Search: O(1)
        - No order
        
- Trie:
    - From wiki, a trie, also called digital tree, radix tree or prefix tree, is a kind 
of search tree—an ordered tree data structure used to store a dynamic set or 
associative array where the keys are usually strings.

    - Example: 
For keys {"A", "to", "tea", "ted", "ten", "i", "in", and "inn"}:
            None
    t       A(15)       i(11)
to(7)      te              in(5)
    tea(3) ted(4) ten(12)     inn(9)

    - Insight:
Node does not have key, but the key info is in its POSITION.

    - Application:
Both Insert and Find runs in O(n) time, where n is the length of the key. 
Save space if many common prefixes exist (Similar to a nested dictionary?). 



Essence of many algorithms: avoid repeated searching. 
List of e.g.'s:


- Using special data structures to save previous results
    - Using Dict/Set for O(1) random search (no need for ordered pushing,
    no need for poping):
        - Time-space tradeoff
        
        - Using Table for O(1) indexed search (hierarchial dicionary is fine, too)
        (No need for ordered pushing, no need for poping)
            - recursive with memorization (replace dynamical programming?)
                - This is easy, since recursive is simplest way of constructing how the current
                problem RELATES to a sub-problem
    
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

    - Using combined Data structures by referencing
        - LRU cache: Dict + Double linked list for achieving O(1) 
        random search, ordered pop, and ordered push
        
    - ?: Trie
    
- Using various methods to know which previous results to use/store
    in which case (whether it will be smart/stupid transitions). 
    - Edit distance:
        - Two dimensional problem, misleading to think about given 
        dist(A[:i], B[:j]) solved, how to do dist(A[:i+1], B[:j]), 
        dist(A[:i], B[:j+1]), dist(A[:i+1], B[:j+1])!
        - Think about in order to solve dist(A[:i], B[:j]), what's needed
        
        - Try a few examples and find the implicits (most difficult!)
        
        - The problem itself determined what are smart & stupid:
            - "Smart": In which case: same char between A[i] and B[i]
            - "Stupid": all other cases (including same char not canceled out)
    
        - Finding implicits of rule for smart transitions: 
        dist(AAA, AA)=1, but dist(AAA, AAA)=0. So it is
        not non-decreasing, from dist(A[:i-1], B[:j-1]) to dist(A[:i], B[:j-1]);
        But it IS non-decreasing from dist(A[:i-1], B[:j-1]) to dist(A[:i], B[:j])!
        Proof: A[i] canceling with B[j] is optimal already; it is impossible for
        3 or 4 elements to cancel out together!
        
        - Smart transitions: dist(AAA, AA) -> but dist(AAA, AAA).
        The key thing is to be mathematically sure that only when A[i]==B[j] there is
        the smart transition!! Cases like A[i]==B[j-1] does not help!
        
        - Stupid transitions: (AAA, BB) -> (AAA, BBB)
        
        - Using the rule: dist(A[:i], B[:j]) comes from three transformations: 
            - Innovation: dist(A[:i-1], B[:j-1]), if A[i]==B[j]
            - Otherwise??? No Innovation, only stupid following prior results