# ============================================================
# schemas.py — Pydantic Şemaları (API Giriş/Çıkış Sözleşmeleri)
# ============================================================


from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .models import CompatibilityLevel

# ============================================================
# HARDWARE ŞEMALARI
# ============================================================

class HardwareBase(BaseModel):
    """
    Hardware için ortak alanlar.
    Hem Create hem de Read şemaları buradan miras alır.
    """
    vendor_id:           str            = Field(..., example="8086",       description="PCI Vendor ID (üretici kodu)")
    device_id:           str            = Field(..., example="1502",       description="PCI Device ID (ürün kodu)")
    name:                str            = Field(..., example="Intel 82579LM Gigabit NIC")
    category:            Optional[str]  = Field(None, example="NIC")
    compatibility_level: CompatibilityLevel = Field(CompatibilityLevel.bronze, example="gold")


class HardwareCreate(HardwareBase):
    """
    POST /hardware/ için request body şeması.
    HardwareBase'den miras alır, 'id' ve 'created_at' YOK
    çünkü bunları veritabanı otomatik oluşturur.
    """
    pass  # Şu an ekstra alan yok, Base yeterli


class HardwareResponse(HardwareBase):
    """
    GET /hardware/ yanıtı için şema.
    Veritabanından gelen 'id' ve 'created_at' de dahil edilir.
    """
    id:         int
    created_at: datetime

    class Config:
        # SQLAlchemy model nesnelerini Pydantic'e çevirmeyi sağlar.
        # Olmadan: orm_obj.name → hata verir.
        # Olunca:  Pydantic orm_obj'dan otomatik okur.
        from_attributes = True


# ============================================================
# SOFTWARE ŞEMALARI
# ============================================================

class SoftwareBase(BaseModel):
    """Software için ortak alanlar."""
    name:                str                 = Field(...,  example="LibreOffice")
    version:             Optional[str]       = Field(None, example="7.4.2")
    publisher:           Optional[str]       = Field(None, example="The Document Foundation")
    compatibility_level: CompatibilityLevel  = Field(CompatibilityLevel.bronze, example="silver")


class SoftwareCreate(SoftwareBase):
    """POST /software/ için request body şeması."""
    pass


class SoftwareResponse(SoftwareBase):
    """GET /software/ yanıtı için şema."""
    id:         int
    created_at: datetime

    class Config:
        from_attributes = True
