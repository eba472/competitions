## Chapter 2: BACK-OF-THE-ENVELOPE ESTIMATION

####
Good feel = thought experiment + common performance numbers
2^10 = 10^3 = 1KB
2^20 = 10^6 = 1MB
2^30 = 10^9 = 1GB
2^40 = 10^12 = 1TB
2^50 = 10^15 = 1PB

Latency numbers:
Compress 1KB with zippy | 10,000ns = 10mus
Send 2Kb bytes over 1Gbps network | 20mus
Read 1MB sequentially from memory | 250mus
Read 1MB sequentially from the network | 10ms
Read 1MB sequentially from disk | 30ms
Disk seek | 10ms
Send Packet CA -> Neth -> CA | 150ms

Memory is fast. Disk is slow => Avoid disk seek
Simple compression is fast

Availability

99% -> 14.4 min/day
99.99% -> 8.64 sec/day
Peak QPS = 2 * QPS

Tips:
- Rounding & Approximation
- Write down my assumptions
- Label my units
- Common questions: QPS, Peak QPS, Storage, cache, number of servers
