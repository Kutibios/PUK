from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models   import Software, CompatibilityLevel
from ..schemas  import SoftwareCreate, SoftwareResponse, SoftwareUpdate

router = APIRouter(prefix="/software", tags=["Software"])


@router.get("/", response_model=List[SoftwareResponse], summary="Yazılımları listele ve filtrele")
def list_software(
    skip:                int                          = 0,
    limit:               int                          = 100,
    name:                Optional[str]                = Query(None, description="İsme göre ara (kısmi eşleşme)"),
    publisher:           Optional[str]                = Query(None, description="Yayıncıya göre filtrele"),
    compatibility_level: Optional[CompatibilityLevel] = Query(None, description="Uyumluluk seviyesine göre filtrele"),
    db: Session = Depends(get_db)
):
    """
    Sertifikalı tüm yazılımları döndürür.
    İsteğe bağlı query parametreleriyle filtreleme yapılabilir.
    """
    q = db.query(Software)

    if name:
        q = q.filter(Software.name.ilike(f"%{name}%"))
    if publisher:
        q = q.filter(Software.publisher.ilike(f"%{publisher}%"))
    if compatibility_level:
        q = q.filter(Software.compatibility_level == compatibility_level)

    return q.offset(skip).limit(limit).all()


@router.get("/{software_id}", response_model=SoftwareResponse, summary="Tek yazılım getir")
def get_software(software_id: int, db: Session = Depends(get_db)):
    """ID'ye göre tek bir yazılım kaydı döndürür. Bulunamazsa 404."""
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


@router.patch("/{software_id}", response_model=SoftwareResponse, summary="Yazılım kaydını güncelle")
def update_software(software_id: int, payload: SoftwareUpdate, db: Session = Depends(get_db)):
    """
    Belirtilen alanları günceller. Gönderilmeyen alanlar değişmez.
    Bulunamazsa 404 döndürür.
    """
    sw = db.query(Software).filter(Software.id == software_id).first()
    if sw is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={software_id} olan yazılım bulunamadı."
        )

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(sw, field, value)

    db.commit()
    db.refresh(sw)
    return sw


@router.delete("/{software_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Yazılım kaydını sil")
def delete_software(software_id: int, db: Session = Depends(get_db)):
    """ID'ye göre yazılım kaydını siler. Başarılıysa 204, bulunamazsa 404."""
    sw = db.query(Software).filter(Software.id == software_id).first()
    if sw is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID={software_id} olan yazılım bulunamadı."
        )
    db.delete(sw)
    db.commit()
