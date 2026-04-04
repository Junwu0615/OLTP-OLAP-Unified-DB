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

# [可選] 如果想每次開機自動啟動 Docker
    # 法 1: 可把啟動指令加到 .bashrc
    echo "sudo service docker start" >> ~/.bashrc
    
    # [優雅] 法 2: 使用 systemd 啟動 (不過 WSL2 預設沒有 systemd，需先安裝並啟用)
    # sudo systemctl enable docker

# [可選] 若無設定 systemd，可在 /etc/wsl.conf 加入以下設定：
    - sudo nano /etc/wsl.conf
    - [boot]
      systemd=true

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

# [可選] 如果有設定自動啟動
    # 法 1: 刪除 .bashrc 新增的指令，避免下次打開又啟動
    nano ~/.bashrc
    
    # [優雅] 法 2: 使用 systemd 停止自動啟動
    # sudo systemctl disable docker

# [可選] 重新啟動 Docker 服務
sudo systemctl start docker
```

<br>