-- ==========================================================
-- 1. 安裝核心擴充功能 (Extensions)
-- 註：需搭配 docker-compose 中 shared_preload_libraries 的設定
-- ==========================================================

-- 追蹤所有 SQL 的執行統計 (次數、耗時、I/O)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- 強化約束能力，支援複合索引與排除約束
CREATE EXTENSION IF NOT EXISTS btree_gist;

-- 虛擬索引工具：在不實際建立索引(不鎖表/不耗空間)的情況下測試優化效果
CREATE EXTENSION IF NOT EXISTS hypopg;

-- 針對 32 核高併發環境，採樣並診斷「鎖等待 (Wait Events)」的來源
CREATE EXTENSION IF NOT EXISTS pg_wait_sampling;


-- ==========================================================
-- 2. 建立監控專用帳號 (Prometheus Exporter)
-- ==========================================================
-- 建立低權限帳號供 Grafana/Prometheus 體系使用
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_user WHERE usename = 'postgres_exporter') THEN
        CREATE USER postgres_exporter WITH PASSWORD 'exporter';
    END IF;
END
$$;

-- 授予 pg_monitor 核心權限：使其能讀取 pg_stat_statements 與系統活動狀態，而不需超級用戶權限
GRANT pg_monitor TO postgres_exporter;