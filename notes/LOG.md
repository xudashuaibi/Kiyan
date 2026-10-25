# 工程日志

## 2026-10-23 chat-web

- 部署 Dify，创建对话型应用并发布
- 写 HTML + JS 调用 Dify API
- 卡点：401（密钥格式错）、400（应用没发布）、Failed to fetch（跨域）
- 解决：改 `Bearer ` 格式、点发布、用本地 HTTP 服务器

## 2026-10-24 yolo-web

- Python 3.15 装 ultralytics 失败（numpy 编译错误）
- 改用 Python 3.12 虚拟环境，安装成功
- 跑通 coco8 训练，生成 best.pt
- 写 Streamlit 检测网页，上传图片能框出物体
- 卡点：`st.camera_input` 触发 removeChild 报错，改为单图上传 + 检测下一张

## 2026-10-25 本地模型 + 桌面内嵌

- 安装 Ollama，拉取 qwen2.5 模型，验证 11434 端口可访问
- Dify 接入 Ollama 时遇到 Connection refused，原因是基础 URL 填了 localhost，改为 host.docker.internal:11434 后解决
- chat-web 切到本地模型，断网后仍能对话，确认推理在本地
- 用 Electron 将 chat-web 打包为桌面应用，产物在 release/ 下