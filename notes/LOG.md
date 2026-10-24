# 工程日志

## 2026-10-23 
- 安装 Ollama，下载 qwen2.5 模型，本地跑通
- 部署 Dify，创建 Chatflow 应用，连接 Ollama
- 写 HTML/JS 网页调用 Dify API，遇到 401 和 400，排查后解决
- 卡点：Dify 应用没发布导致 400，发布后正常

## 2026-10-24
- 安装 ultralytics 时遇到 numpy 编译错误，原因是 Python 3.15 太新
- 改用 Python 3.12 创建虚拟环境，安装成功
- 跑通 coco8 训练，生成 best.pt
- 写 Streamlit 检测网页，上传图片能框出物体