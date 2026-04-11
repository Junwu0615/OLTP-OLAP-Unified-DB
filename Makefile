MAIN_COMPOSE =./docker/docker-compose.yaml

ALL_COMPOSE := $(wildcard ./docker/*/docker-compose.yaml)

SUB_SERVICES = ./docker/airflow/docker-compose.yaml \
			   ./docker/monitoring/docker-compose.yaml \
			   ./docker/portainer/docker-compose.yaml \
			   ./docker/postgresql/docker-compose.yaml

BUILD_SERVICES =./docker/postgresql/docker-compose.yaml

AIRFLOW_DIR = ./docker/airflow

.PHONY: build up down down-v ps fix-sock db-wait list-configs clear-force

init:
	@echo "* 針對子服務進行必要性 init"
	@echo "1. 正在建立 Airflow 必要目錄..."
	mkdir -p $(AIRFLOW_DIR)/config $(AIRFLOW_DIR)/dags $(AIRFLOW_DIR)/logs $(AIRFLOW_DIR)/plugins
	@echo "2. 修正 Airflow 目錄權限, 讓目錄及其子目錄歸屬給 UID 50000"
	sudo chown -R 50000:0 $(AIRFLOW_DIR)
	@echo "3. 確保權限足夠 (rwxr-xr-x)"
	sudo chmod -R 775 $(AIRFLOW_DIR)
	@echo "4. 執行 Airflow 資料庫初始化 (airflow-init)..."
	docker compose -f $(MAIN_COMPOSE) up airflow-init
	@echo "* 環境預熱完成 ..."

build:
	@echo "* 針對子服務進行必要性 build (no-cache)..."
	docker compose -f $(BUILD_SERVICES) build --no-cache

up: fix-sock db-wait
	@echo "* 正在啟動集群版服務..."
	@echo "* 修正 Airflow 目錄權限 (UID 50000)..."
	sudo chown -R 50000:0 $(AIRFLOW_DIR)
	docker compose -f $(MAIN_COMPOSE) up -d
	@echo "* 啟動完成 ..."

down:
	docker compose -f $(MAIN_COMPOSE) down

down-v:
	docker compose -f $(MAIN_COMPOSE) down --volumes --remove-orphans

ps:
	docker compose -f $(MAIN_COMPOSE) ps

fix-sock:
	sudo chmod 666 /var/run/docker.sock

db-wait:
	@echo "正在啟動資料庫..."
	docker compose -f $(MAIN_COMPOSE) up -d postgresql
	@echo "等待資料庫就緒..."
	sleep 10

list-configs:
	@echo "偵測到的子服務設定檔如下："
	@echo "$(ALL_COMPOSE)" | tr ' ' '\n'

clear-force:
	@echo "清理所有「已停止」的容器"
	docker container prune -f

	@echo "清理所有「未被掛載」的 Volume"
	docker volume prune -f