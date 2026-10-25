# 工程日志

## 2026-10-__ chat-web

- 部署 Dify，创建对话型应用并发布
- 写 HTML + JS 调用 Dify API
- 卡点：401（密钥格式错）、400（应用没发布）、Failed to fetch（跨域）
- 解决：改 `Bearer ` 格式、点发布、用本地 HTTP 服务器

## 2026-10-__ yolo-web

- Python 3.15 装 ultralytics 失败（numpy 编译错误）
- 改用 Python 3.12 虚拟环境，安装成功
- 跑通 coco8 训练，生成 best.pt
- 写 Streamlit 检测网页，上传图片能框出物体
- 卡点：`st.camera_input` 触发 removeChild 报错，改为单图上传 + 检测下一张