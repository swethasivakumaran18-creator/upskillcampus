from ultralytics import YOLO

def main():
    # Load the pretrained YOLOv8 Nano model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=512,
        batch=16,
        name="crop_weed_detection",
        project="runs/train"
    )

if __name__ == "__main__":
    main()
