import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(page_title="YOLO 物体检测", layout="centered")
st.title("YOLO 物体检测")
st.caption("请先上传图片，然后点击「确认使用此图片」，最后点击「开始检测」。")

MODEL_PATH = "../runs/detect/train/weights/best.pt"

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

model = load_model()

# ===== 1. 初始化 session_state =====
if "confirmed_image" not in st.session_state:
    st.session_state.confirmed_image = None
if "detection_result" not in st.session_state:
    st.session_state.detection_result = None
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0

def run_detection(image):
    results = model(image, conf=0.25)
    annotated = results[0].plot()
    annotated_image = Image.fromarray(annotated[:, :, ::-1])
    names = results[0].names
    boxes = results[0].boxes
    items = []
    if boxes is not None and len(boxes) > 0:
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            items.append((names[cls_id], conf))
    return annotated_image, items

# ===== 2. 上传区域（每次清空后重新渲染） =====
uploaded_file = st.file_uploader(
    "上传一张图片", 
    type=["jpg", "jpeg", "png"], 
    key=f"file_uploader_{st.session_state.uploader_key}"
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="待检测图片", width="stretch")
    if st.button("确认使用此图片", type="primary"):
        st.session_state.confirmed_image = Image.open(uploaded_file).convert("RGB")
        st.session_state.detection_result = None
        st.rerun()

# ===== 3. 检测区域 =====
st.divider()
if st.session_state.confirmed_image is not None:
    st.image(st.session_state.confirmed_image, caption="已确认的图片", width="stretch")
    
    col_detect, col_next = st.columns(2)
    with col_detect:
        if st.button("开始检测", type="primary"):
            annotated_image, items = run_detection(st.session_state.confirmed_image)
            st.session_state.detection_result = (annotated_image, items)
    
    with col_next:
        if st.button("检测下一张"):
            st.session_state.confirmed_image = None
            st.session_state.detection_result = None
            st.session_state.uploader_key += 1  # 强制重建上传组件
            st.rerun()

# ===== 4. 显示结果 =====
if st.session_state.detection_result is not None:
    st.divider()
    annotated_image, items = st.session_state.detection_result
    st.image(annotated_image, caption="检测结果", width="stretch")
    if items:
        st.subheader("检测到的物体")
        for name, conf in items:
            st.write(f"- **{name}**，置信度 {conf:.2f}")
    else:
        st.write("没有检测到物体。")