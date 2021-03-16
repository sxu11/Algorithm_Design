20210301 Would have been easier if I noticed it's a BST (not just any tree) and there must exist solution. 

Concurrency
20210302 
- Think of "handle" as a wrapper of resource pointer... 
- Good reading TODO: [Threading in C#](http://www.albahari.com/threading/part4.aspx#_Signaling_with_Wait_and_Pulse)
- [AutoResetEvent, ManualResetEvent vs Monitor](https://stackoverflow.com/questions/1717194/autoresetevent-manualresetevent-vs-monitor)
  - WaitHandles.Set()
    - sets the Signal even if no thread is waiting. This means if you call Set in a thread and then call WaitOne in another thread on the same waithandle afterwards, the second thread will continue. 
  - Wait and Pulse are different
    - Pulse only signals a thread that is already in the waiting queue. This means if you call Pulse in a thread and then call Wait in another thread on the same object afterwards, the second thread will wait forever (deadlock).
    - I for myself used wait/pulse as well as lock-free algorithms using CAS operations
- Do not use AutoResetEvent as lock, as there is no [Fairness](https://stackoverflow.com/questions/17273933/autoresetevent-as-a-lock-replacement-in-c)
- [Use Monitor](https://leetcode.com/problems/print-in-order/discuss/432149/C-Monitor)
  - The volatile keyword indicates that a field might be modified by multiple threads that are executing at the same time. 
- [Use Semaphore](https://leetcode.com/problems/print-in-order/discuss/856697/C-Semaphore-based-solution)

20210304 Today's daily really interesting!
- Have a centralized "i" makes it much simpler
- Detail: Odd and Even have different last numbers. Need to clear

20210305 Key is really:
- Monitor.PulseAll(m_lock);
  - Reason is that Monitor.Enter(m_lock) waits:
    - not like frequently re-checking if m_lock is available?
    - but like needs to be notified if m_lock is available...
        
20210310 Fizz Buzz 
- old: 
    - Multithreaded这题就是弄个优先级：
        - fizzbuzz先看，不行release lock
        - fizz和buzz再看
        - number
    - 难点是高优先级的弄完后，就通知其它的别等了！
- 关键：
    - while(this.fbEvent.WaitOne() && this.i <= this.n) 这个太值得玩味了，包括顺序！
- 细节：
    - 用来iter的i是global的！这样才最后会 > n
    - number出for循环后要把其它几个event都Set()了！

20210315
1. 我自己的正向想法不是全局最优，不能handle: [0,2], [1,3], [2,4], [3,5], [4,6]
    - 一个错误的贪心法，
         1. For each interval, find how many intervals are overlapped with it (like nodes "linked" in a graph)
             - define Class
         2. sort nodes by degree of links. Remove from the biggest (and de-link neighbors accordingly)
             - use heap
         3. util all degrees are 0.
        - 证明也错误（任意俩interval之间的关系不影响其它intervals）
2. 太巧妙了，求最少去掉的，反过来求最大集合
3. 为什么按照end来排序的贪心法能行
    -贪心法往往需要证明：
    -首先，其它的end都比它大
    -其次，如果一些intervals跟它有overlap, 那么在这所有这些intervals中能且只能选一个
    -那么，就选第一个好了，对后面的选取更有利

