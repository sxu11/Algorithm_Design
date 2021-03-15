https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR

1. What: Create shorter alias for long URLs.
- Hard (functional) require:
    - fixed length
    - unique
- Optional Hard:
    - pick custom short link
    - expire
    - accessible by API call
- Soft (non-functional) require:
    - resilient (to attack; not guessable)
    - highly available
    - low latency

1.1 What hard

1.2 What soft
- Assumptions:
    - read:write = 100:1
    - 500M new URL shortening / month
    - store each new for 5 years
    - Each object ~ 0.5 kb
    - hotspot: 80-20 rule

- Calculations:
    - QPS:
        - QPMonth = 500M * 100 = 50B
        - Write QPS = 500M / (30*24*3600) = 200
        - Write size = 200 * 0.5 kb = 100 kb
        - Read QPS: 20K
        - Read size = 10 Mb
    - Storage:
        - Total number = 500M * 5 * 12 = 30B
        - Total size = 30B * 0.5 kb = 15 Tb
    - Memory:
        - Per day (?) Read QPS: 20K * 3600 * 24 = 1.7B
        - To cache 20%, we need 0.2 * 1.7B * 0.5kb = 170GB

- API:
    - CreateURL(api_dev_key, original_url,
    custom_alias=None, user_name=None, expire_date=None)
    - deleteURL(api_dev_key, url_key)

- DB:
    - Type
        - NoSQL like DynamoDB, Cassandra, Riak because:
            - we anticipate billions of rows
                - easier to scale
            - don't need to use relationships between objects

    - Set up
        - URL mapping
            - Hash
            - OriginalURL
            - CreateDate
            - ExpireDate
            - UserID
        - User
            - UserID
            - Name
            - Email
            - CreateDate
            - LastLogin

    - Cache (use off-the-shelf Memcached?)
        - How much cache memory?
            - 170GB for 20%. 1 server (~256GB) enough
        - Cache eviction policy?
            - LRU (linked hash map)
        - replicate caching server to distribute load
            - update on reading miss
    - Data Partitioning and Replication:
        - partitioning schema:
            - based on initial letter?
                - unbalanced
            - hash-based (map any key to a num between [1...256])
                - can still overload, use Consistent Hashing
    - Clean up:
        - slowly remove expired links & do lazy cleanup (it's ok for some old ones to stay)
            - delete upon read
            - a separate light-weighted cleanup service, run only when traffic low

- Encoding Algo:
    - hashing (MD5, SHA256, can then be encoded for display?)
        - question: what would be the length?
            - With base64, [A-Z,a-z,0-9,+,/]:
                - 6 letter: 64^6 ~ 68.7 billion (suffice)
                - 8 letter: 64^8 ~ 281 trillion
            - With MD5 (128-bit, after base64, we'll get > 21 chars)
                - Now we only have space for 8 chars per short key
                - We can take first 6 or 8 letters
    - issues:
        - multiple user enter same URL, but get same shortened (not good)
        - what if parts of URL are URL-encoded? (id=design & %3Fid%3Ddesign are identical)
    - solve:
        - append an increasing num to each URL to make it unique, but:
            - overflow?
            - performance?
        - append user id, but:
            - have to sign in?
            - still conflict?
        - generate keys offline (Key Generation Service, stored in key-DB)
            - simple and fast and unique
            - concurrency?
                - unused/used key tables
                - cache
                - lock
            - key-DB size?
                - With base64, have 68.7B unique 6-letter keys.
                    - If use 1 byte to store 1 alpha-numeric char, we can store all in 6 * 68.7B = 412 GB
            - single pt of failure?
                - use replica

- Load Balancer
    - Where to add:
        - Clients & Application servers
        - App servers & DB servers
        - App servers & Cache servers
    - Method:
        - Round Robin
            - simple, no overhead
            - LB will take out dead server
            - but can be overloaded
                - handle by periodically queries the backend server about load and adjust traffic

- Telemetry
    - usage, traffic (date, time)
    - user geology (country, referring page)
    - hotspot URL

- Security & Permission
    - private/protected shortURL?
        - add permission level (public/private) in URL DB, or
        - create separate table for UserID, permissions
            - for NoSQL wide-column DB like Cassandra, key is Hash, columns are permitted UserIDs.