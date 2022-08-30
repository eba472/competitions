## Chapter 1: Scale from 0 to mills of users

DNS: domain name service
IP address: Internet protocol
HTTP: HyperText Transfer Protocol
JSON: Javascript Object Notation

#### DB
Relational DB(RDBMS), (SQL DB): MySQL, Oracle, PostgreSQL
Non-relational DB: CouchDB, Neo4j, Cassandra, HBAse, Amazon DynamoDB | key-value | graph | column | document
- For super-low latency
- Unstructured data or no relationship
- Serialize & deserialize data (JSON, XML, YAML, etc)
- Massive amounts of data

Vertical scaling: Add more power to a server [Has hard limit][Simple to implement][When traffic is low]
Horizontal scaling (Scale out): Add more servers [Useful for large scale apps]

Load balancer: Evenly distributes incoming traffic among web servers (has public IP)

Public IP: Can be reachable through internet
Private IP: reachable only between servers in the same network

#### Database replication:
- master(original) : supports only write
- slave(copy) relationship : supports only read [Can be many DB to support large number of read operation]
  
Advantages:
- Better performance -> support more parallel queries (Because only read)
- Replication -> Reliability (Fault tolerance) : 100% Uptime : strong redundancy : High cost -> Zero downtime
- High availability : 99.99% Uptime : weak redundancy : minimal cost -> Accepts failure and recover fast

Redundancy: The practice of using of one or more additional configuration items to provide fault tolerance

#### Cache : read-through cache
- Temporary storage area: expensive responses & Frequently accessed data /JS/CSS/Image/Video etc
- Improves web page loading
- Reduce DB access load
-  Volatile memory => when restarts, all data will be lost
- Use when data is read frequently but modified infrequently.
- Appropriate expiration policy is needed
- Resolve inconsistency: DB & cache sync
- Single server : SPOF (Single point of failure)
- Eviction policy: Delete some data when it is full. LRU, LFU, FIFO etc

#### CDN: Content delivery network
- geographically dispersed servers used to deliver **static content** : Akamai, Varnish software etc
- Learn more about ***dynamic content*** caching
- Distance matters
- HTTP Header: TTL : Time to live (Kind of an eviction policy)
- Considerations
  - Cost: third party tech
  - Appropriate cache expiry date
  - CDN fallback: what happen if CDN fail?
  - Invalidate data before expiration: [version number or using their APIs etc]

#### Stateless Web Tier
Stateful architecture: bad
A stateful server remembers client data (state: session data, profile image etc) from one request to the next.
- Each server has one user's session
  - Cross server use is difficult
  - Server down => Session lost => user impact
Stateless architecture: good
- User request can go to any server => Simpler, more robust ans scalable
- Accomplished by storing session data in RedisDB(NoSQL: easy to scale)

#### Data centers
- GeoDNS: geo-routed to the closest data center splits traffic at load balancer (x% in US-East and (100 – x)% in US-West).
- Traffic redirection: GeoDNS can be used.
- Data synchronization: In failover cases, traffic might be routed to a data center where data is unavailable.
- Must need to test the app in different locations.

#### Message queue: more loosely coupled system
- Durable in memory component for asynchronous component (work as buffer).
- Producer --- Publish --> Message queue --- consume --> Consumer.
- Why: We need to decouple different components of the system so they can be scaled independently.
  
#### Logging, metrics and automation
- Logging: Monitoring error logs is important because it helps to identify problems early.
- Metrics: Gain business insights & Understand health status: 
  - Host level metrics: CPU, Memory, disk I/O
  - Aggregated level metrics: Entire DB tire, Cache tier
  - business: Daily active users, retention and revenue
- CI/CD: code check-in is verified through automation. Time save for build & save & deploy

#### Sharding: Horizontal DB scaling
- Same schema & different data
- Allocated by Hash function: **User_id % 4** (Here used_id is the sharding key)
  - Efficient data access
  - Distribute evenly
- Complexities:
  - Re-sharding (Chapter 5)
  - Celebrity problem (Katy Perry, Justin Bieber, and Lady Gaga all end up on the same shard)
  - Join and de-normalization: hard to perform join operation.

#### Beyond millions of users :  may decouple the system to even smaller services
- Keep web tier stateless
- Build redundancy at every tier
- Cache data as much as you can
- Support multiple data centers
- Host static assets in CDN
- Scale your data tier by sharding
- Split tiers into individual services
- Monitor your system and use automation tools
  