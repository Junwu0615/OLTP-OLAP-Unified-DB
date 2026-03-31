### *A.　Benchmark Methods*
- #### *1.　OLTP 壓力測試 ( Write )*
  ```
  測試特徵 :
  大量 INSERT / UPDATE
  短 transaction
  高 concurrency
  
  指標 :
  TPS (Transactions Per Second)
  p95 / p99 latency
  lock wait
  WAL write rate
  CPU usage
  IO write throughput
  
  常用工具 :
  ⭐ pgbench
  sysbench
  HammerDB
  
  常見 benchmark :
  TPC-C
  ```
- #### *2.　OLAP 壓力測試 ( Read )*
  ```
  測試特徵 :
  大量 SELECT
  complex query
  aggregation
  scan / join
  
  指標 :
  QPS (Queries Per Second)
  query latency
  scan throughput
  CPU utilization
  memory usage
  
  常見 benchmark :
  ⭐ TPC-H
  TPC-DS
  ```
- #### *3.　HTAP 壓力測試 ( Mix )*
  ```
  同時跑 :
  transaction workload
  analytic workload
  
  觀察 :
  OLTP TPS drop
  OLAP latency spike
  buffer cache eviction
  IO contention
  
  常見 benchmark :
  ⭐ CH-BenCHmark
  ```

<br>

### *B.　Generic DB Benchmark*
| **Step** | **Description** | **Tool** |
| :--: | :-- | :--: |
| 1 | Query Benchmark | - |
| 2 | OLTP Workload Benchmark | pgbench |
| 3 | OLAP Workload Benchmark | - |
| 4 | HTAP Workload Benchmark | - |
| 5 | Saturation Benchmark | - |

- #### *1.　Query Benchmark*

- #### *2.　OLTP Workload Benchmark*
  ```
  -- c: client 數量
  -- j: thread 數量
  -- T: 測試秒數
    
  pgbench \
  -c 50 \
  -j 10 \
  -T 300 \
  postgres
  ```
- #### *3.　OLAP Workload Benchmark*

- #### *4.　HTAP Workload Benchmark*

- #### *5.　Saturation Benchmark*

<br>