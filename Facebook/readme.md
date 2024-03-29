[AMZN, FB, MS高频题交集](https://docs.google.com/spreadsheets/d/1Hwa-xGVXcLdMtKr0JqDBppB86dQJZDCtCw4q-TqxS0Y/edit#gid=0)

No.	#	Title
1	973	K Closest Points to Origin
- my Contests/C119
    - heappush all pts, using dist as 1st dim
    - heappop K pts
    
2	238	Product of Array Except Self
- 之前做了，但最优解抄答案
    - Could you solve it in O(n) time complexity and without using division?
        - 关键是发现：第i个数，来自于nums[:i]和nums[i+1:]的乘积
        - 用一个list A, 其第i个元素是i前所有元素的乘积（关键在于用了cumSum的思想，A[-1]就包含了累计乘积，不需要额外for loop）
        - 用一个list B, 其第i个元素是i后所有元素的乘积
        - 最后把二者相乘
    - Could you solve it with O(1) constant space complexity?
        - 怎么不用list B? 直接在A上操作
            - 这样就不能用A[-1] (因为被b污染), 换做用一个constant p

3	560	Subarray Sum Equals K
- 之前做了, CumSum思想 

4	273	Integer to English Words
- 我的思路：
    - 先变成string, 来念
        - 不好！本质上要按照"范围"的数字性，来分类！！
    - 举出几个例子（0, 10, 11, 12, 21, 100）
        - 例子不够！
    - 先搞定3位数的以内的
        - 这个思路是对的，但以下都没搞清楚：
            - 外部怎么用它
            - 它内部还是要recursive
        - 个位数硬map，十位数分类，百位数hundred+十位数
            - 0～20分类没够！实际上dict+ifElse极其混乱；不如全部dict.
            - tens也直接dict !! + recursive..
            - 百位数dict + recursive...
    - 4位数以上的：分segment处理
        - ifElse来判断是10^3, 10^6, 还是10^9区间！
            - 没法消除1 Billion中的"Million"!
                - 什么时候没有Million? 当Million这个segment没有数的时候！（sth like num%1000==0）
        

5	124	Binary Tree Maximum Path Sum
    - TLE, but whatever, 93/94 passed, it's a Hard!

6	269	Alien Dictionary
    - locked (seems done!)
    
7	415	Add Strings
    - 

8	23	Merge k Sorted Lists
9	297	Serialize and Deserialize Binary Tree
10	199	Binary Tree Right Side View
11	211	Add and Search Word - Data structure design
12	426	Convert Binary Search Tree to Sorted Doubly Linked List
13	523	Continuous Subarray Sum
14	340	Longest Substring with At Most K Distinct Characters
15	543	Diameter of Binary Tree
16	636	Exclusive Time of Functions
17	76	Minimum Window Substring
18	139	Word Break
19	31	Next Permutation
20	349	Intersection of Two Arrays
21	215	Kth Largest Element in an Array
22	173	Binary Search Tree Iterator
23	721	Accounts Merge
24	33	Search in Rotated Sorted Array
25	767	Reorganize String
26	88	Merge Sorted Array
27	56	Merge Intervals
- done, under Basic\

28	71	Simplify Path
29	270	Closest Binary Search Tree Value
30	29	Divide Two Integers
31	621	Task Scheduler
32	34	Find First and Last Position of Element in Sorted Array
33	785	Is Graph Bipartite?
34	938	Range Sum of BST
35	146	LRU Cache
36	286	Walls and Gates
37	140	Word Break II
38	98	Validate Binary Search Tree
39	133	Clone Graph
40	143	Reorder List
41	1004	Max Consecutive Ones III
42	236	Lowest Common Ancestor of a Binary Tree
43	528	Random Pick with Weight
44	314	Binary Tree Vertical Order Traversal
45	380	Insert Delete GetRandom O(1)
46	419	Battleships in a Board
47	42	Trapping Rain Water
48	463	Island Perimeter
49	863	All Nodes Distance K in Binary Tree
50	50	Pow(x, n)
51	138	Copy List with Random Pointer
52	200	Number of Islands
53	253	Meeting Rooms II
54	10	Regular Expression Matching
55	227	Basic Calculator II
56	162	Find Peak Element
57	277	Find the Celebrity
58	987	Vertical Order Traversal of a Binary Tree
59	529	Minesweeper
60	32	Longest Valid Parentheses
61	347	Top K Frequent Elements
62	490	The Maze
63	692	Top K Frequent Words
64	15	3Sum
65	114	Flatten Binary Tree to Linked List
66	515	Find Largest Value in Each Tree Row
67	348	Design Tic-Tac-Toe
68	1	Two Sum
69	323	Number of Connected Components in an Undirected Graph
70	977	Squares of a Sorted Array
71	239	Sliding Window Maximum
72	126	Word Ladder II
73	78	Subsets
74	3	Longest Substring Without Repeating Characters
75	540	Single Element in a Sorted Array
76	350	Intersection of Two Arrays II
77	257	Binary Tree Paths
78	207	Course Schedule
79	224	Basic Calculator
80	378	Kth Smallest Element in a Sorted Matrix
81	622	Design Circular Queue
82	20	Valid Parentheses
83	2	Add Two Numbers
84	468	Validate IP Address
85	39	Combination Sum
86	22	Generate Parentheses
87	79	Word Search
88	75	Sort Colors
89	230	Kth Smallest Element in a BST
90	332	Reconstruct Itinerary
91	105	Construct Binary Tree from Preorder and Inorder Traversal
92	121	Best Time to Buy and Sell Stock
93	417	Pacific Atlantic Water Flow
94	74	Search a 2D Matrix
95	394	Decode String
96	567	Permutation in String
97	5	Longest Palindromic Substring
98	127	Word Ladder
99	442	Find All Duplicates in an Array
100	57	Insert Interval
101	449	Serialize and Deserialize BST
102	662	Maximum Width of Binary Tree
103	266	Palindrome Permutation
104	969	Pancake Sorting
105	695	Max Area of Island
106	148	Sort List
107	4	Median of Two Sorted Arrays
108	160	Intersection of Two Linked Lists
109	772	Basic Calculator III
110	128	Longest Consecutive Sequence
111	698	Partition to K Equal Sum Subsets
112	19	Remove Nth Node From End of List
113	93	Restore IP Addresses
114	46	Permutations
115	8	String to Integer (atoi)
116	240	Search a 2D Matrix II
117	91	Decode Ways
118	516	Longest Palindromic Subsequence
119	329	Longest Increasing Path in a Matrix
120	210	Course Schedule II
121	102	Binary Tree Level Order Traversal
122	13	Roman to Integer
123	208	Implement Trie (Prefix Tree)
124	16	3Sum Closest
125	41	First Missing Positive
126	317	Shortest Distance from All Buildings
127	17	Letter Combinations of a Phone Number
128	212	Word Search II
129	54	Spiral Matrix
130	37	Sudoku Solver
131	295	Find Median from Data Stream
132	48	Rotate Image
133	62	Unique Paths
134	73	Set Matrix Zeroes
135	153	Find Minimum in Rotated Sorted Array
136	443	String Compression
137	44	Wildcard Matching
138	287	Find the Duplicate Number
139	129	Sum Root to Leaf Numbers
140	445	Add Two Numbers II
141	117	Populating Next Right Pointers in Each Node II
142	509	Fibonacci Number
143	11	Container With Most Water
144	21	Merge Two Sorted Lists
145	703	Kth Largest Element in a Stream
146	112	Path Sum
147	300	Longest Increasing Subsequence
148	437	Path Sum III
149	92	Reverse Linked List II
150	81	Search in Rotated Sorted Array II
151	242	Valid Anagram
152	70	Climbing Stairs
153	113	Path Sum II
154	53	Maximum Subarray
155	63	Unique Paths II
156	387	First Unique Character in a String
157	116	Populating Next Right Pointers in Each Node
158	151	Reverse Words in a String
159	235	Lowest Common Ancestor of a Binary Search Tree
160	118	Pascal's Triangle
161	152	Maximum Product Subarray
162	108	Convert Sorted Array to Binary Search Tree
163	206	Reverse Linked List
164	7	Reverse Integer
165	101	Symmetric Tree
166	283	Move Zeroes
167	136	Single Number
168	104	Maximum Depth of Binary Tree
169	344	Reverse String
170	49	Group Anagrams