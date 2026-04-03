## *WSL2 原生 Docker 安裝方式*
### *A.　解除安裝舊版*
```
sudo apt-get remove docker docker-engine docker.io containerd runc
```

<br>

### *B.　安裝 Docker Engine*
```
# 解除安裝舊版
sudo apt-get remove docker docker-engine docker.io containerd runc


# 更新索引 + 安裝依賴
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release


# 加入 Docker 官方 GPG 金鑰
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg


# 設定 Docker 來源儲存庫
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


# 更新索引 + 安裝 Docker 核心組件
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

<br>

### *C.　啟動 Docker 並設定權限*
```
# 啟動 Docker 服務
sudo service docker start

# [可選] 如果你想要每次開機自動啟動 Docker，可以把啟動指令加到 .bashrc
echo "sudo service docker start" >> ~/.bashrc

# 將當前使用者加入 docker 群組，允許不使用 sudo 執行 docker 命令
sudo usermod -aG docker $USER
```

<br>

### *D.　停止 Docker Engine*
```
# 1. 停止服務
sudo service docker stop

# 2. 徹底關閉，連自動觸發都不想要
sudo systemctl stop docker.socket

# 3. 確認沒有任何 docker 相關進程在跑
ps aux | grep docker

# [可選] 如果你之前有把啟動指令加到 .bashrc，請去刪除它，避免下次打開又啟動
nano ~/.bashrc

# [可選] 重新啟動 Docker 服務
sudo systemctl start docker
```

<br>