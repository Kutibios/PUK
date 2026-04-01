# ============================================================
# routers/hardware.py — Hardware CRUD Endpoint'leri
# ============================================================


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db       # Veritabanı bağlantısı (dependency)
from ..models   import Hardware     # SQLAlchemy ORM modeli
from ..schemas  import HardwareCreate, HardwareResponse  # Pydantic şemaları

# ----------------------------------------------------------
# Router Oluşturma
# ----------------------------------------------------------

router = APIRouter(prefix="/hardware", tags=["Hardware"])


# ----------------------------------------------------------
# GET /hardware/ — Tüm Kayıtları Listele
# ----------------------------------------------------------

@router.get("/", response_model=List[HardwareResponse], summary="Tüm donanımları listele")
def list_hardware(
    skip:  int = 0,    # Kaç kayıt atlanacak (sayfalama için)
    limit: int = 100,  # En fazla kaç kayıt döndürülecek
    db: Session = Depends(get_db)  # FastAPI otomatik inject eder
):
    """
    Sertifikalı tüm donanımları döndürür.
    `skip` ve `limit` parametreleriyle sayfalama yapılabilir.
    """
    hardware_list = db.query(Hardware).offset(skip).limit(limit).all()
    return hardware_list


# ----------------------------------------------------------
# GET /hardware/{hardware_id} — Tek Kayıt Getir
# ----------------------------------------------------------
@router.get("/{hardware_id}", response_model=HardwareResponse, summary="Tek donanım getir")
def get_hardware(hardware_id: int, db: Session = Depends(get_db)):
    """
    ID'ye göre tek bir donanım kaydı döndürür.
    Bulunamazsa 404 hatası fırlatır.
    """
    hw = db.query(Hardware).filter(Hardware.id == hardware_id).first()

    if hw is None:
        # HTTPException: FastAPI'ye özel hata sınıfı.
        # status_code=404 → "Not Found" HTTP kodu
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={hardware_id} olan donanım bulunamadı."
        )
    return hw


# ----------------------------------------------------------
# POST /hardware/ — Yeni Kayıt Ekle
# ----------------------------------------------------------
# status_code=201 → "Created" (başarılı kayıt oluşturma kodu)
@router.post("/", response_model=HardwareResponse, status_code=status.HTTP_201_CREATED, summary="Yeni donanım ekle")
def create_hardware(hardware: HardwareCreate, db: Session = Depends(get_db)):
    """
    Yeni bir donanım kaydı oluşturur.
    Request body'si HardwareCreate şemasına göre doğrulanır.
    """
    # Pydantic modelini SQLAlchemy modeline dönüştür
    # model_dump() → Pydantic v2'de dict() yerine kullanılır
    db_hardware = Hardware(**hardware.model_dump())

    db.add(db_hardware)    # Session'a ekle (henüz DB'ye yazmadı)
    db.commit()            # Değişikliği veritabanına kalıcı yaz
    db.refresh(db_hardware)  # DB'den güncel hali (id, created_at) çek
    return db_hardware


# ----------------------------------------------------------
# DELETE /hardware/{hardware_id} — Kayıt Sil
# ----------------------------------------------------------
@router.delete("/{hardware_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Donanım kaydını sil")
def delete_hardware(hardware_id: int, db: Session = Depends(get_db)):
    """
    ID'ye göre donanım kaydını siler.
    Başarılıysa 204 (No Content) döndürür, bulunamazsa 404.
    """
    hw = db.query(Hardware).filter(Hardware.id == hardware_id).first()

    if hw is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={hardware_id} olan donanım bulunamadı."
        )

    db.delete(hw)
    db.commit()
    # 204 response'ta body olmaz, return None yeterli
