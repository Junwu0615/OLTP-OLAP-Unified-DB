### *A.　Event Description*
```
# 以製造工廠為主題情境
  - 定義機台 [mach] : machines
  - 定義訂單 [prod] : products
  - 生產訂單 [prod_order] : production_orders <- [products]
  - 機台狀態 [mach_st_log] : machine_status_logs
  - 生產產出 [prod_recd] : production_records <- [production_orders, machines, products]


   建立訂單 [prod_order]
      │
      ▼
   開始生產 [prod_order.start_at]
      │
      ▼
  狀態發生變化 [mach_st_log.status]
      ▲
      │
      ▼
   持續生產 [prod_recd.quantity]
      │
      ▼
    達到 [prod_order.quantity]
      │
      ▼
   完成訂單 [prod_order.end_at]
```

<br>

### *B.　Table Features*
- #### *OLTP*
|**Name**|**Type**|**Streaming**|**Description**|**Remark**|
|--:|:--:|:--:|:--:|:--:|
| machines | 靜態 | - | 儲存機台基本資訊 | ⚠️預處理 |
| products | 靜態 | - | 儲存產品基本資訊 | ⚠️預處理 |
| 🗑️ machine_events | 動態 | 低頻 | 記錄機台運行過程中的各類事件 | - |
| machine_status_logs | 動態 | 低頻 | 持續記錄機台狀態變化 | - |
| production_orders | 動態 | 低頻 | 記錄生產訂單資訊 | - |
| production_records | 動態 | 高頻 | 記錄實際生產結果 | - |

- #### *OLAP*
|**Name**|**Description**|**Remark**|
|--:|:--:|:--:|
| dim_machine | 機台維度表 | - |
| dim_product | 產品維度表 | - |
| dim_time | 時間維度表 | - |
| fact_machine_status | 機台狀態事實表 | - |
| fact_production | 生產事實表 | - |

<br>

### *C.　Simulation Data Volume*
```
Products:            5
Machines:            20
Orders:              30
Status logs:         ~5000+
Production records:  500
Machine events:      100


# OLTP TPS
OFF_PEAK : ~3/sec
NORMAL   : ~10/sec
PEAK     : ~25/sec


# By Day
| table               | rows/day |
| ------------------- | -------- |
| machine_status_logs | ~200k    |
| production_records  | ~80k     |
| machine_events      | ~10k     |
```

<br>

### *D.　Startup Simulate Script*
- #### *D.1.　Go to Env*
    ```
    .\.venv\Scripts\activate
    ```
- #### *D.2.　Initialize Factory Data*
    ```
    python src/scripts/init_factory_data.py
    ```
- #### *D.3.　Simulate Factory Stream*
    ```
    python src/scripts/simulate_factory_stream.py
    ```

<br>

### *E.　Benchmark*

<br>

### *F.　Metrics*

<br>