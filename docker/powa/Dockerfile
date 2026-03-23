FROM postgres:15

# 安裝 PoWA 相關套件與開發工具
RUN apt-get update && apt-get install -y \
    postgresql-15-powa \
    postgresql-15-pg-stat-kcache \
    postgresql-15-pg-qualstats \
    && rm -rf /var/lib/apt/lists/*

# 修改啟動參數，預載監控擴充功能
CMD ["postgres", "-c", "shared_preload_libraries=pg_stat_statements,powa,pg_stat_kcache,pg_qualstats"]