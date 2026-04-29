# ============================================================
# PUK Core API — Dockerfile
# ============================================================
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Bağımlılıkları kur (Poetry gerektirmez, direkt pip kullanır)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını içeri aktar
COPY . .

# FastAPI servisini 8000 portunda başlat
CMD ["uvicorn", "puk_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
