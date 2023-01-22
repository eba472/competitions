Rate Limiter: HTTP 429 (too many requests sent)
- Block excess calls to protect the server and resources
- Create max 10 accounts & claim reward only 5 times a week etc

Benefits:
- Prevent DenialOfService attack
- Reduce cost (third party service)
- Prevent server overload

Questions
- ClientSide (Unreliable: can be forged) vs ServerSide vs middleware?
  - Usually implemented in API gateway
  - Is current programming language efficient enough?
  - third-party: limited algorithm & expensive but saves time & resources?
- Throttle based on what? IP address, userID, or others?
- Scale? Number of users?
- Is it a distributed system?
- Inform the throttled user?

Requirements
- Accuracy
- Low latency (efficient: speed & memory)
- Distributed
- Exception handling
- High fault tolerance

Algos:
- Token bucket
  - Whenever there is token, pass
  - (easy and efficient) Bucket size and token refill rate
  - Diff buckets for diff endpoints && Need bucket for each IP address
- Leaking bucket (Queue size and outflow rate)
  - If room in queue: put it else: drop 
  - queue is processed at fixed rate
  - Suitable when stable outflow rate is needed
- Fixed window counter algorithm
  - $$  $$

Footnote
API gateway: (RateLimit, SSL termination, authentication, IP whitelisting, serve static content)

