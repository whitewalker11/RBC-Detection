FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

WORKDIR /app

COPY requirements.txt .
RUN apt update && apt install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY scripts/ ./scripts/
COPY models/ ./models/
COPY data/ ./data/

CMD ["python3", "scripts/inference.py"]