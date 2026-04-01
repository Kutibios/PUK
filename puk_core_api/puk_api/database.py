

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://puk_user:puk_secret@localhost:5433/puk_db"
)


engine = create_engine(DATABASE_URL, pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

# 5. get_db() — FastAPI Dependency (Bağımlılık)

def get_db():
    db = SessionLocal()
    try:
        yield db          # Bu noktada endpoint çalışır
    finally:
        db.close()        # İstek bitince (hata olsa bile) kapat
