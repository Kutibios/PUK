# ============================================================
# routers/software.py — Software CRUD Endpoint'leri
# ============================================================


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models   import Software
from ..schemas  import SoftwareCreate, SoftwareResponse

router = APIRouter(prefix="/software", tags=["Software"])


@router.get("/", response_model=List[SoftwareResponse], summary="Tüm yazılımları listele")
def list_software(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Sertifikalı tüm yazılımları döndürür. Sayfalama destekler."""
    return db.query(Software).offset(skip).limit(limit).all()


@router.get("/{software_id}", response_model=SoftwareResponse, summary="Tek yazılım getir")
def get_software(software_id: int, db: Session = Depends(get_db)):
    """ID'ye göre tek bir yazılım kaydı döndürür."""
    sw = db.query(Software).filter(Software.id == software_id).first()
    if sw is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={software_id} olan yazılım bulunamadı."
        )
    return sw


@router.post("/", response_model=SoftwareResponse, status_code=status.HTTP_201_CREATED, summary="Yeni yazılım ekle")
def create_software(software: SoftwareCreate, db: Session = Depends(get_db)):
    """Yeni bir yazılım kaydı oluşturur."""
    db_software = Software(**software.model_dump())
    db.add(db_software)
    db.commit()
    db.refresh(db_software)
    return db_software


@router.delete("/{software_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Yazılım kaydını sil")
def delete_software(software_id: int, db: Session = Depends(get_db)):
    """ID'ye göre yazılım kaydını siler."""
    sw = db.query(Software).filter(Software.id == software_id).first()
    if sw is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={software_id} olan yazılım bulunamadı."
        )
    db.delete(sw)
    db.commit()
