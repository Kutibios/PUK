from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models   import Hardware, CompatibilityLevel
from ..schemas  import HardwareCreate, HardwareResponse, HardwareUpdate

router = APIRouter(prefix="/hardware", tags=["Hardware"])


@router.get("/", response_model=List[HardwareResponse], summary="Donanımları listele ve filtrele")
def list_hardware(
    skip:                int                          = 0,
    limit:               int                          = 100,
    name:                Optional[str]                = Query(None, description="İsme göre ara (kısmi eşleşme)"),
    category:            Optional[str]                = Query(None, description="Kategoriye göre filtrele (örn: NIC, GPU)"),
    vendor_id:           Optional[str]                = Query(None, description="PCI Vendor ID'ye göre filtrele"),
    compatibility_level: Optional[CompatibilityLevel] = Query(None, description="Uyumluluk seviyesine göre filtrele"),
    db: Session = Depends(get_db)
):
    """
    Sertifikalı tüm donanımları döndürür.
    İsteğe bağlı query parametreleriyle filtreleme yapılabilir.
    """
    q = db.query(Hardware)

    if name:
        q = q.filter(Hardware.name.ilike(f"%{name}%"))
    if category:
        q = q.filter(Hardware.category.ilike(f"%{category}%"))
    if vendor_id:
        q = q.filter(Hardware.vendor_id == vendor_id)
    if compatibility_level:
        q = q.filter(Hardware.compatibility_level == compatibility_level)

    return q.offset(skip).limit(limit).all()


@router.get("/{hardware_id}", response_model=HardwareResponse, summary="Tek donanım getir")
def get_hardware(hardware_id: int, db: Session = Depends(get_db)):
    """ID'ye göre tek bir donanım kaydı döndürür. Bulunamazsa 404."""
    hw = db.query(Hardware).filter(Hardware.id == hardware_id).first()
    if hw is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={hardware_id} olan donanım bulunamadı."
        )
    return hw


@router.post("/", response_model=HardwareResponse, status_code=status.HTTP_201_CREATED, summary="Yeni donanım ekle")
def create_hardware(hardware: HardwareCreate, db: Session = Depends(get_db)):
    """Yeni bir donanım kaydı oluşturur."""
    db_hardware = Hardware(**hardware.model_dump())
    db.add(db_hardware)
    db.commit()
    db.refresh(db_hardware)
    return db_hardware


@router.patch("/{hardware_id}", response_model=HardwareResponse, summary="Donanım kaydını güncelle")
def update_hardware(hardware_id: int, payload: HardwareUpdate, db: Session = Depends(get_db)):
    """
    Belirtilen alanları günceller. Gönderilmeyen alanlar değişmez.
    Bulunamazsa 404 döndürür.
    """
    hw = db.query(Hardware).filter(Hardware.id == hardware_id).first()
    if hw is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={hardware_id} olan donanım bulunamadı."
        )

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(hw, field, value)

    db.commit()
    db.refresh(hw)
    return hw


@router.delete("/{hardware_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Donanım kaydını sil")
def delete_hardware(hardware_id: int, db: Session = Depends(get_db)):
    """ID'ye göre donanım kaydını siler. Başarılıysa 204, bulunamazsa 404."""
    hw = db.query(Hardware).filter(Hardware.id == hardware_id).first()
    if hw is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={hardware_id} olan donanım bulunamadı."
        )
    db.delete(hw)
    db.commit()
