from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolo11n.pt")
    model.train(data="coco8.yaml", epochs=10, imgsz=640)