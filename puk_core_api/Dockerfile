# ============================================================
# PUK Core API — Dockerfile
# ============================================================
FROM python:3.12-slim

# Çevresel Değişkenleri Ayarlama (Python ve Poetry için optimum ayarlar)
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Sistem bağımlılıkları ve curl'ün kurulması
RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# Poetry'nin kurulması
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

# Sadece dependency dosyalarını kopyala (Docker build önbelleğinden maksimum yararlanmak için)
COPY pyproject.toml poetry.lock ./

# Sadece prod bağımlılıklarını kur (--no-root, projenin kendisini kurmaz)
RUN poetry install --no-root

# Projenin tamamını içeri aktar
COPY . .

# FastAPI servisini 8000 portunda başlat
CMD ["poetry", "run", "uvicorn", "puk_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
