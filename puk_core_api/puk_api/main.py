from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FastAPI app
app = FastAPI(
    title="PUK Core API",
    description="Pardus Uyumluluk Kataloğu Merkezi Veritabanı ve Karar Destek Arayüzü",
    version="1.0.0",
)

# Security Settings (CORS) - it is neccessary for frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #  It is open for all requests in development stage   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test Uç Noktası (Root Route)
@app.get("/", tags=["Health"])
async def root():
    return {
        "status": "success",
        "message": "PUK Core API başarıyla çalışıyor!",
        "documentation": "Swagger arayüzü için /docs adresine gidin.",
    }

# hardware - software should be added (soon)
