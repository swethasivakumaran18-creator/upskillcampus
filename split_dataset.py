import os
import random
import shutil
from pathlib import Path

# ========= CHANGE THIS PATH =========
SOURCE_DIR = Path("agri_data/data")
# ====================================

DEST_DIR = Path("dataset")

random.seed(42)

# Create folders
for split in ["train", "valid", "test"]:
    (DEST_DIR / split / "images").mkdir(parents=True, exist_ok=True)
    (DEST_DIR / split / "labels").mkdir(parents=True, exist_ok=True)

# Get all images
images = list(SOURCE_DIR.glob("*.jpeg"))

print(f"Found {len(images)} images")

random.shuffle(images)

train_end = int(0.7 * len(images))
valid_end = int(0.9 * len(images))

train = images[:train_end]
valid = images[train_end:valid_end]
test = images[valid_end:]

splits = {
    "train": train,
    "valid": valid,
    "test": test
}

for split_name, image_list in splits.items():

    for img in image_list:

        label = img.with_suffix(".txt")

        shutil.copy(img, DEST_DIR / split_name / "images" / img.name)

        if label.exists():
            shutil.copy(label, DEST_DIR / split_name / "labels" / label.name)

print("\nDataset split completed!\n")

print(f"Training Images   : {len(train)}")
print(f"Validation Images : {len(valid)}")
print(f"Testing Images    : {len(test)}")
