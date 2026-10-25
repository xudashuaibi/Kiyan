@echo off
chcp 65001 >nul
cd /d "%~dp0"
title chat-web 一键启动 (含 Docker & Dify)

REM ===== 需要你修改这里：Dify 的 docker-compose.yaml 所在目录 =====
set "DIFY_PATH=D:\dify\docker"
REM =============================================================

echo ========================================
echo   chat-web 一键启动
echo ========================================
echo.

REM ===== 1. 启动 Docker Desktop (如果没在运行) =====
echo [1/3] 检查 Docker Desktop...
tasklist /FI "IMAGENAME eq Docker Desktop.exe" 2>NUL | find /I "Docker Desktop.exe" >NUL
if errorlevel 1 (
    echo    正在启动 Docker Desktop...
    start "" "C:\Users\ROG\AppData\Local\Programs\DockerDesktop\Docker Desktop.exe"
) else (
    echo    Docker Desktop 已在运行
)

REM ===== 2. 等待 Docker 引擎就绪 (核心步骤) =====
echo [2/3] 等待 Docker 引擎就绪...
:wait_for_docker
docker info >nul 2>&1
if errorlevel 1 (
    timeout /t 3 /nobreak >nul
    goto wait_for_docker
)
echo    Docker 引擎已就绪
echo.

REM ===== 3. 启动 Dify 容器 =====
echo [3/3] 启动 Dify 容器...
if exist "%DIFY_PATH%\docker-compose.yaml" (
    pushd "%DIFY_PATH%"
    docker compose up -d
    popd
    echo    Dify 容器启动完成
) else (
    echo    [!] 未找到 Dify 的 docker-compose.yaml，跳过自动启动。
    echo        请确认 DIFY_PATH 变量设置正确。
    echo        路径: %DIFY_PATH%
)
echo.

REM ===== 4. 启动本地服务器并打开浏览器 =====
echo 启动本地服务器 http://localhost:8000
start "" http://localhost:8000
python -m http.server 8000
pause