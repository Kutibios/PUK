# ============================================================
# models.py — SQLAlchemy ORM Modelleri (Veritabanı Tabloları)
# ============================================================
# ORM (Object Relational Mapper): SQL yazmak yerine Python sınıfı
# yazarak veritabanı tablolarını tanımlamana olanak sağlar.
# Örneğin Hardware sınıfı → "hardware" tablosuna karşılık gelir.
# ============================================================

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql import func
from sqlalchemy import DateTime
import enum

from .database import Base  # database.py'deki Base'i içe aktar

# ----------------------------------------------------------
# Enum: Uyumluluk Seviyeleri
# ----------------------------------------------------------

class CompatibilityLevel(str, enum.Enum):
    bronze = "bronze"   # Temel çalışıyor
    silver = "silver"   # Önerilen
    gold   = "gold"     # Tam uyumlu & test edilmiş

# ----------------------------------------------------------
# Tablo 1: Hardware
# ----------------------------------------------------------
# Pardus ile uyumlu olduğu sertifikalanmış donanımları tutar.
# Her satır bir (vendor_id, device_id) çiftini temsil eder.
# Örnek: Intel NIC — VendorID=8086, DeviceID=1502
class Hardware(Base):
    __tablename__ = "hardware"  # Veritabanındaki tablo adı

    id         = Column(Integer, primary_key=True, index=True)
    # vendor_id: Donanımı üreten şirketin PCI/USB kimliği (hex string)
    vendor_id  = Column(String(10), nullable=False, index=True)
    # device_id: O şirkete ait spesifik ürünün kimliği
    device_id  = Column(String(10), nullable=False, index=True)
    # Kullanıcı dostu ürün adı
    name       = Column(String(255), nullable=False)
    # Kategori: "NIC", "GPU", "Audio Controller" vb.
    category   = Column(String(100), nullable=True)
    # Sertifika seviyesi — yukarıdaki Enum ile kısıtlandı
    compatibility_level = Column(
        Enum(CompatibilityLevel), nullable=False, default=CompatibilityLevel.bronze
    )
    # Kaydın ne zaman eklendiğini otomatik olarak yazar
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# ----------------------------------------------------------
# Tablo 2: Software
# ----------------------------------------------------------

class Software(Base):
    __tablename__ = "software"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(255), nullable=False, index=True)
    version     = Column(String(50),  nullable=True)  
    publisher   = Column(String(255), nullable=True)   # Yazılımı yapan şirket
    compatibility_level = Column(
        Enum(CompatibilityLevel), nullable=False, default=CompatibilityLevel.bronze
    )
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
