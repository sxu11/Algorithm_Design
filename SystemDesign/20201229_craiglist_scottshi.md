API:
- Reader:
- Write:

DB:
- User: SQL
- Post: SQL + S3
  - postId, time, ind1, ind2, …, status, jpg

QPS:
- Write: 46*10^3*10*200/(3.6k*24)=10^3, peak 2~3*10^3, 1 machine?
- Read: 100 times,  100 machines

User token, not registration (auth)

CRUD      Text 2kb, jpg 200kb

Use category to replace ind1, ind2, ...

Storage? (7 days to expire)
- Me: 7*10^5 ~ 10^6, 10^7mb=10tb

Region?

Search?

CDN cache (to reduce Read bottleneck)

LB
