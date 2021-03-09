Contest 230, 02/27/2021
- 3 problems done (while babysitting after 7:15pm), 1533 / 11654
  - 5689 Count Items Matching a Rule
    - too easy
  - 5690 Closest Dessert Cost
    - Subsets, small variation! Good use, cool think & execution
  - 5691 Equal Sum Arrays With Minimum Number of Operations
    - Good & clean initial thoughts w/ greedy! proud
- 1 problem undone
  - 1776 Car Fleet II
    - I later came up with my O(n^2) TLE solution based on following observation 1
    - Use of stack is really shocking!! 
      - closest right cars most likely
    - [Good Explain](https://leetcode.com/problems/car-fleet-ii/discuss/1085844/Python3.-Simple-solution-with-using-stack): Based on the code and comment, two key observations are:
        - The collision time for a car won't be affected by the cars on its left. Thus if going from right to left, we can fix the collision time along the way.
        - The collision time for a car will only be affected by the cars on its right. Again among all the cars on current car's right, there are certain cars that won't affect current car's collision time. Namely, if the car has a higher speed than the current car, or, if the car's collision time is earlier than the current car's collision time with this car, then such cars won't affect current car's collision time, and can be ignored. The mono stack has only kept those cars that can possibly affect the current car.
    - [Good Recommend](https://leetcode.com/problems/car-fleet-ii/discuss/1085987/JavaC%2B%2BPython-O(n)-Stack-Solution): stack problems
        - Car Fleet II
        - Find the Most Competitive Subsequence
        - Minimum Number of Removals to Make Mountain Array
        - Final Prices With a Special Discount in a Shop
        - Constrained Subsequence Sum
        - Minimum Cost Tree From Leaf Values
        - Sum of Subarray Minimums
        - Online Stock Span
        - Score of Parentheses
        - Next Greater Element II
        - Next Greater Element I
        - Largest Rectangle in Histogram
        - Trapping Rain Water
      
      
Context 231, 03/06/2021

Number of Restricted Paths From First to Last Node. Good problem!
  1. Construct Graph
    - [this](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/discuss/1097204/PythonJava-Dijkstra-and-Cached-DFS-Clean-and-Concise) is so simple & elegent:
        - graph = defaultdict(list)
        - for u, v, w in edges:
            - graph[u].append((w, v))
            - graph[v].append((w, u))
    - mine is awkward: 
        - constructed a Node class
        - used a Node list to append all Nodes
  2. Dijkstra:
    - mine: wiki step-by-step
        - create list-based Q and dict-based dist
        - while Q not empty:
          - find min dist的node (O(nodes), not good!)
          - 用它来更新所有neighbors (O(edges))的dist
    - good: 
        - minHeap = [(0,n)]  # dist,node; with heap, becomes O(log(nodes))
        - dist = [float("inf")] * (n+1)
        - dist[n] = 0
        - while minHeap:
          - d,u = heappop(minHeap)  
          - if d!=dist[u]: continue  # Pruning step, can be ignored; there is shorter path than direct connect to it's neighbor, therefore, it can be ignored
          - for w,v in graph[u]:
            - if dist[v]>dist[u]+w:
              - dist[v]=dist[u]+w
              - heappush(minHeap, (dist[v],v))
          - return dist
        - 所以先建堆，和边iter边建堆的区别在哪里？
          - 貌似[都行](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
  3. dfs也有讲究，是否可以用@lru_cache(None):
    - mine: 
      - 纯dfs visit各Node, 不返回结果，如果遇到sink就把self.res += 1
      - 这种如果用cache就会出错，因为dfs(self, node)只要node相同就会skip (?)
    - good: 
      - dfs的return返回"从当前node出发找到的path数"