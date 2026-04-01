

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, Base
from .routers  import hardware, software

# ----------------------------------------------------------
# Lifespan: Uygulama Yaşam Döngüsü Yöneticisi
# ----------------------------------------------------------

# (Sadece geliştirme kolaylığı; prod'da Alembic migration kullan!)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # == BAŞLANGIÇ ==
    Base.metadata.create_all(bind=engine)  # Tabloları oluştur
    print("✅ Veritabanı tabloları hazır.")
    yield
    
    print("🛑 PUK Core API kapanıyor.")


# ----------------------------------------------------------
# FastAPI App Nesnesi
# ----------------------------------------------------------
app = FastAPI(
    title="PUK Core API",
    description="Pardus Uyumluluk Kataloğu — Merkezi Veritabanı ve Karar Destek Arayüzü",
    version="1.0.0",
    lifespan=lifespan,  
)

# ----------------------------------------------------------
# CORS Middleware
# ----------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------------
# Router Kaydı
# ----------------------------------------------------------

app.include_router(hardware.router)
app.include_router(software.router)


# ----------------------------------------------------------
# Sağlık Kontrolü (Health Check)
# ----------------------------------------------------------
@app.get("/", tags=["Health"])
async def root():
    return {
        "status":        "success",
        "message":       "PUK Core API başarıyla çalışıyor!",
        "documentation": "Swagger için /docs, ReDoc için /redoc adresine gidin.",
        "endpoints": {
            "hardware": "/hardware/",
            "software": "/software/",
        }
    }
