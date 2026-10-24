import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(page_title="YOLO 物体检测", layout="centered")
st.title("YOLO 物体检测")
st.caption("上传一张图片，模型会框出检测到的物体。")

MODEL_PATH = "../runs/detect/train/weights/best.pt"

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

model = load_model()

uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="原图", width="stretch")

    if st.button("开始检测"):
        with st.spinner("检测中..."):
            results = model(image, conf=0.25)
            annotated = results[0].plot()
            annotated_image = Image.fromarray(annotated[:, :, ::-1])
            st.image(annotated_image, caption="检测结果", width="stretch")

            names = results[0].names
            boxes = results[0].boxes
            if boxes is not None and len(boxes) > 0:
                st.subheader("检测到的物体")
                for box in boxes:
                    cls_id = int(box.cls[0])
                    conf = float(box.conf[0])
                    st.write(f"- **{names[cls_id]}**，置信度 {conf:.2f}")
            else:
                st.write("没有检测到物体。")