# AI 面试项目

## 项目结构

- `chat-web/`：通过 Dify API 对话的网页
- `yolo-web/`：YOLO 训练 + Streamlit 检测网页
- `notes/LOG.md`：工程日志

## 已完成

### chat-web
- Dify 创建对话型应用并发布，通过 API 调用
- 原生 HTML + JavaScript 聊天界面
- 双击 `chat-web/start.bat` 启动

### yolo-web
- Python 3.12 + ultralytics 8.4.185
- 用 coco8 跑通 yolo11n.pt 训练，生成 best.pt
- Streamlit 图片上传检测网页
- 双击 `yolo-web/start.bat` 启动

### 本地大模型部署

- 安装 Ollama，运行 `qwen2.5:7b`
- 在 Dify 模型供应商中接入 Ollama，基础 URL 填 `http://host.docker.internal:11434`
- chat-web 已切换到本地 Ollama 模型，因为本地的不好用又切了回去

### 桌面内嵌

- 用 Electron（html2exe / electron-builder）将 chat-web 打包为 Windows 桌面应用
- 打包产物在 `chat-web/release/`，不提交到仓库

## 工程日志

见 `notes/LOG.md`。