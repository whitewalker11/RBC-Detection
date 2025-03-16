```md
# RBC Cell Detection using YOLOv10

This project detects RBC (Red Blood Cells) in microscopic images using YOLOv10.

## Setup & Installation
```bash
git clone <repo_url>
cd rbc_detection
pip install -r requirements.txt
```

## Export Model
```bash
python scripts/export.py
```

## Run Inference
```bash
python scripts/inference.py
```

## Run with Docker
```bash
docker build -t rbc_detector .
docker run --gpus all rbc_detector
```