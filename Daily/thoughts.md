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
 