# yolo-web

YOLO 训练脚本 + Streamlit 图片检测网页。

## 环境

Python 3.12 虚拟环境，已安装 ultralytics 和 streamlit。

## 训练

.\.venv\Scripts\python.exe train.py

## 运行检测网页

.\.venv\Scripts\python.exe -m streamlit run app.py

模型路径：`../runs/detect/train/weights/best.pt`