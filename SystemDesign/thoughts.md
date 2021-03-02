- 卧槽Leetcode超神：
  - https://leetcode.com/discuss/interview-question/system-design?currentPage=1&orderBy=most_votes&query=
  - 某模版：https://leetcode.com/discuss/career/229177/My-System-Design-Template

- 主要掌握几个组件，很多题目都可以出来，之前经常看一个大佬的视频，他说这就是跟积木一样的，当然知道的越多越好，
  
  - 时间有限的话， redis， kafka， sql， dynamo， s3这几个就够
  - 比如当时我说我选sql，不选dynamo，他问我为什么。我说因为
    - sql是master-slave， 
    - dynamo peer-to-peer， dynamo强势在于写强大，
    
    但是我设计这个系统，读多， 不需要，而且sql handle 100k做分布式是没问题的
  
  - 或者加cache，cache并不是100%可以加速的，要根据读写特点
    - 比如设计instagram， 我就加了cache， 是因为我觉得
      - 有一些user很活跃， lru的话， 命中率很高，
      - 而且cache其实有stale data的问题，但是intagram数据更改的概率很小，
    
    所以我觉得加一个可以提速不少
    
  - 还有gateway， lb，replication这些在educative说的还挺重要的，我感觉其实不太重要。特别gateway， lb这些我一般不提
  - 还是推荐大家看paper的(dynamodb)，看一篇可以吹好久
  
- 因为要面试aws找了udemy的课在上，强推。强推的几个组件里面都有讲，而且会把为什么用，怎么用讲的很清楚。一定要把pro and con记下来
  - https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c02/
  - https://www.udemy.com/course/aws-solutions-architect-professional/
  
- https://www.1point3acres.com/bbs/thread-559285-1-1.html
  - 举个例子，系统设计要用到message queue，大半会提到kafka。这个时候你得知道面试官会问kafka什么？他八成会问用kafka有什么问题。有啥问题？kafka只保证at least one time delivery。你最好给每个message加sequence number来防止duplictes
    - （是的我知道kafka后来promise了exact one time delivery的feature。不过没人用）
  - educative? 
    - 很多考点作者没有展开，比如考的最多的tinyurl，作者并没有提到cache部分的设计的考虑。在生产环境中如何refresh cache？如何invalidate一个cache中的url？用memcache还是redis？
    - 建议看五遍，建议把每个不懂的词都google出来完全完全看懂。比如常常常常考到的bloomfilter
  - 看Design Data Intensive Application这本书
    - 请一定把第二部分全部看完。有精力请看第三部分。第二部分请看3遍。第二部分能够解答40～50%你遇到的跟data有关的设计
  - 最重要的而且并没有多少人提到的，请看各个大公司的engineer blog。非常非常非常重要非常非常
    1. blog提到的系统就是现在在生产环境的系统
    2. blog会提到各种tradeoff以及做这种设计的原因
    3. 好的blog会给出各种详细的细节，甚至源代码（当然你不需要阅读源码这么深入）
    4. blog提到的系统很容易拿来举一反三
    - 举例： https://eng.uber.com/cherami/ 如果读懂了并且在读的过程中不停的问自己考点，那么这一篇文章可以解决不下10个不同的system design问题：
      - 如何设计一个job queue？
      - 如何保证job一定执行？
      - deadleatter咋设计（uber blog里还有单独一篇讲这个）
      - 如何设计一个分布式爬虫？等等等等
  - 多看看经典的presentation presentation presentation。请去youtube搜，
    - 例如： https://www.youtube.com/watch?v=UEJ6xq4frEw&t=667s
    - 例如： https://www.youtube.com/watch?v=cSFWlF96Sds （*****）
    - btw那些教你做system design的youtube视频（好多是印度人的）我全都看了。质量很一般很一般很一般阿西吧浪费我时间。
  - 去infoq看。举个（最好的）栗子：
    - https://www.infoq.com/presentations/pinterest/ 这一篇文章可以终结你对sharding问题的困惑。只靠shard用mysql也可以撑起billion级别的访问量的。
    - 我还很喜欢这篇： https://www.infoq.com/presentations/Twitter-Timeline-Scalability/
  - 你还能更屌一点么？能啊，请看论文。
    - dynamo的论文，
    - big table的论文，
    - cassandra的论文，
    - google doc系统的论文等等
    
- https://www.1point3acres.com/bbs/thread-683982-1-1.html 他的框架都更接近工业， 很多设计非常巧妙，又好记。
  - 强烈推荐火车票的设计和messager，看完messager的设计，马上变大佬
  
- https://github.com/donnemartin/system-design-primer
  - 已有的资料里面的grokking system design interview 极其混乱且很多不在点上， 已有的教材和课本的知识点或是片面，或是陈旧
