Template: https://leetcode.com/discuss/career/229177/My-System-Design-Template

(1) FEATURE EXPECTATIONS [5 min]
        (1.1) Use cases
        (1.2) Scenarios that will not be covered
        (1.3) Who will use
        (1.4) How many will use
        (1.5) Usage patterns

twitter use case:
  发文，看文（邮件提醒，安全，注册）；TODO: 转发、评论？
  注册提醒不管
  发的比看的少的多，1:100?
  多少人？regional, 美国人300m, 大概10m有账户？
  大概1m活跃用户？一天登一次，看20个twitter, 发1个twitter
  白天多，晚上少。工作时间少，下班多。周末多。


(2) ESTIMATIONS [5 min]
        (2.1) Throughput (QPS for read and write queries)
        (2.2) Latency expected from the system (for read and write queries)
        (2.3) Read/Write ratio
        (2.4) Traffic estimates
                - Write (QPS, Volume of data)
                - Read  (QPS, Volume of data)
        (2.5) Storage estimates
        (2.6) Memory estimates
                - If we are using a cache, what is the kind of data we want to store in cache
                - How much RAM and how many machines do we need for us to achieve this ?
                - Amount of data you want to store in disk/ssd

(2.1) twitter throughput:
  - QPS读：(1d = 24*3600 ~ 10**5s)
    - 20 * 10**6 / day = 2 * 10**7 / 10**5 = 200
  - QPS写：10

(2.2) Latency expected:
  - 写之后：1s就出来
  - 读：1s
(2.3) Read/Write ratio: 20:1
(2.4) Traffic estimates:
      读/写一条：140 words (2 byte * 140 ~ 300 byte) + pic (0.3M byte ~ 1000 times of text),
      读一共：
        text: 300 * 20 * 10**6 = 6 * 10**9 bytes = 6 GB / day  = 60KB / s
        pic: 6 TB / day = 60MB / s
      写一共：
        text: 3KB / s
        pic: 3MB / s
(2.5) Storage estimates: 多级储存
    2周以内：某种storage. 6 TB * 14 = 64 TB
    2周以外、一年以内：archive. 6 TB * 365 = 2200 TB

(2.6) Memory estimates: ?


(3) DESIGN GOALS
        (3.1) Latency and Throughput requirements
        (3.2) Consistency vs Availability  [Weak/strong/eventual => consistency | Failover/replication => availability]


(3.1)
- Latency: 1s for both read/write
- Throughput: ?

- Availability > Consistency
  - Use what?

(4) HIGH LEVEL DESIGN [5-10 min]
        (4.1) APIs for Read/Write scenarios for crucial components
        (4.2) Database schema
        (4.3) Basic algorithm
        (4.4) High level design for Read/Write scenario

(5) DEEP DIVE [15-20 min]
        (5.1) Scaling the algorithm
        (5.2) Scaling individual components:
                -> Availability, Consistency and Scale story for each component
                -> Consistency and availability patterns
        (5.3) Think about the following components, how they would fit in and how it would help
                a) DNS
                b) CDN [Push vs Pull]
                c) Load Balancers [Active-Passive, Active-Active, Layer 4, Layer 7]
                d) Reverse Proxy
                e) Application layer scaling [Microservices, Service Discovery]
                f) DB [RDBMS, NoSQL]
                        > RDBMS
                            >> Master-slave, Master-master, Federation, Sharding, Denormalization, SQL Tuning
                        > NoSQL
                            >> Key-Value, Wide-Column, Graph, Document
                                Fast-lookups:
                                -------------
                                    >>> RAM  [Bounded size] => Redis, Memcached
                                    >>> AP [Unbounded size] => Cassandra, RIAK, Voldemort
                                    >>> CP [Unbounded size] => HBase, MongoDB, Couchbase, DynamoDB
                g) Caches
                        > Client caching, CDN caching, Webserver caching, Database caching, Application caching, Cache @Query level, Cache @Object level
                        > Eviction policies:
                                >> Cache aside
                                >> Write through
                                >> Write behind
                                >> Refresh ahead
                h) Asynchronism
                        > Message queues
                        > Task queues
                        > Back pressure
                i) Communication
                        > TCP
                        > UDP
                        > REST
                        > RPC

(6) JUSTIFY [5 min]
	(6.1) Throughput of each layer
	(6.2) Latency caused between each layer
	(6.3) Overall latency justification