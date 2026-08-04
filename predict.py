from ultralytics import YOLO

def main():
    # Load your trained model
    model = YOLO("runs/detect/runs/train/crop_weed_detection/weights/best.pt")

    # Run prediction on test images
    results = model.predict(
        source="dataset/test/images",
        save=True,
        imgsz=512,
        conf=0.25
    )

    print("✅ Prediction completed successfully!")

if __name__ == "__main__":
    main()
