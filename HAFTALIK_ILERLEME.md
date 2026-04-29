# Bitirme Projesi Haftalık İlerleme Raporu

## Proje Bilgileri

| Alan | Bilgi |
|------|-------|
| **Öğrenci Adı Soyadı** | Levent Kutay Sezer |
| **Öğrenci No** | 22360859013|
| **Proje Başlığı** | PUK (Pardus Uyumluluk Kataloğu)|
| **Danışman** | Prof. Dr. Turgay Tugay Bilgin |
| **Dönem** | 2025-2026 Bahar |

---

## İş Planı



| Hafta | Tarih Aralığı | Planlanan İş | Tahmini Tamamlanma (%) | Durum |
|-------|---------------|--------------|------------------------|-------|
| 1 | 30.03.2026 - 05.04.2026 | Altyapı ve İzleme Sistemlerinin Kurulumu (OCS, Grafana vb.) | %10 | ✅ Tamamlandı |
| 2 | 06.04.2026 - 12.04.2026 | PUK Çekirdek Servisi API ve Veritabanı Şeması Tasarımı | %20 | ✅ Tamamlandı |
| 3 | 13.04.2026 - 29.04.2026 | İstek Uç Noktalarının (API Endpoints) ve CRUD İşlemlerinin Yazılması | %30 | ✅ Tamamlandı |
| 4 | GG.AA - GG.AA | Entegrasyon ve Analiz Motoru: OCS Verilerinin Çekilmesi | %40 | ⬜ Başlamadı |
| 5 | GG.AA - GG.AA | Karar Destek Sistemi: Uyumluluk ve Skorlama Algoritmasının Yazılması | %50 | ⬜ Başlamadı |
| 6 | GG.AA - GG.AA | Web Portalı GUI Geliştirimi: Kullanıcı Arama Motoru (Donanım-Yazılım Uyumlu mu?) | %60 | ⬜ Başlamadı |
| 7 | GG.AA - GG.AA | Kurum Yöneticileri Panosu GUI Geliştirimi (Karar Destek Ekranları) | %70 | ⬜ Başlamadı |
| 8 | GG.AA - GG.AA | Toplu Ajan Yükleme Modülü GUI ve Entegrasyonu | %80 | ⬜ Başlamadı |
| 9 | GG.AA - GG.AA | Uçtan Uca Sistem Testleri ve Arayüz Optimizasyonları | %90 | ⬜ Başlamadı |
| 10 | GG.AA - GG.AA | Performans Darboğazlarının Giderilmesi ve Projenin Teslimi | %100 | ⬜ Başlamadı |

**Durum simgeleri:** ⬜ Başlamadı | 🔄 Devam Ediyor | ✅ Tamamlandı | ⚠️ Gecikti

---

## Haftalık İlerleme Kayıtları


---


---

### Hafta 1 *(Tarih: 30.03.2026 - 05.04.2026)*

**Plandaki hedef:**
- Proje altyapısının kurulması, OCS Inventory ve izleme/monitoring araçlarının yapılandırılması ve analizi. (OCS Inventory, Grafana, Node Exporter) Ocs Inventory GUI'sinin içindeki configuration ayarlarının incelenmesi ve Agent'ların yapılandırılması. 

**Bu hafta yaptıklarım:**
- OCS Inventory docker-compose ile kurulumu tamamlandı.
- Grafana ve Node Exporter kurulumu başarıyla gerçekleştirildi ve Dashboard'lar oluşturuldu.
- OCS Agent'ların (Windows/Linux) cihazlara test kurulumu yapıldı ve sunucuya veri akışı doğrulandı.

**Plana göre durumum:**
- Altyapı sorunsuz olarak tamamlandı, hedeflere tam anlamıyla ulaşıldı. Container'lar birbirleri ile de sorunsuz bir şekilde iletişim halinde.

**Karşılaştığım sorunlar / zorluklar:**
- Projenin başlangıç aşamasında servisleri Docker CLI üzerinden manuel olarak yönetirken; servis sayısının artmasıyla beraber ortaya çıkan ağ konfigürasyonu, bağımlılık yönetimi ve sürdürülebilirlik ihtiyaçlarını karşılamak adına Docker Compose yapısına geçiş yaptım. Bu sayede tüm monitoring stack’ini (Prometheus, Grafana, Node Exporter) ve envanter yönetimini (OCS Inventory) tek bir merkezden, modern bir yaklaşımla standardize ettim. Son olarak network ayarlarında ufak tefek sorunlar yaşadım fakat bind mount ve port mapping ayarlarını doğru yaparak çözüme ulaştım.

**Gelecek hafta hedefim:**
- Veritabanı şemasının (PostgreSQL) oluşturulması ve API projesinin temelinin atılması ve geliştirilmesi.

---

### Hafta 2 *(Tarih: 06.04.2026 - 12.04.2026)*

**Plandaki hedef:**
- Veritabanı şemasının (PostgreSQL) oluşturulması ve API projesinin (PUK Core API) temelinin atılması ve geliştirilmesi.

**Bu hafta yaptıklarım:**
- PUK Core API projesi modern bir yaklaşımla, FastAPI framework'ü kullanılarak başlatıldı.
- Veritabanı modelleri ve şemaları (SQLAlchemy ORM kullanılarak) tasarlandı ve PostgreSQL bağlantısı başarıyla kuruldu.
- Veritabanı versiyon kontrolü ve migrasyon işlemleri için Alembic entegrasyonu sağlandı.
- Geliştirme ortamının otomatize edilmesi ve standartlaştırılması adına proje Nix-shell ve Taskfile (otomasyon aracı) kullanarak yapılandırıldı.
- Projenin veri akışını yönetecek API yönlendirmelerinin (routing) ve CRUD (Oluşturma, Okuma, Güncelleme, Silme) işlemlerinin temelleri atıldı.
- Yapılan tüm değişiklikler ve geliştirmeler git kullanılarak versiyonlandı ve anlamlı commit mesajlarıyla kayıt altına alındı.

**Plana göre durumum:**
- PUK Core API'nın temel yapısı ve veritabanı bağlantısı başarılı bir şekilde tasarlandı. Planlanan "PUK Çekirdek Servisi API ve Veritabanı Şeması Tasarımı" adımı tamamlanmış olup API geliştirme adımları takvime uygun biçimde ilerlemektedir.

**Karşılaştığım sorunlar / zorluklar:**
- Geliştirme ortamında (Nix) ve veritabanı migrasyonlarında (Alembic) başlangıçta ufak entegrasyon ayarlarıyla zaman kaybedilse de dökümantasyonlar eşliğinde doğru ortam değişkenlerinin (environment variables) konfigüre edilmesiyle sorun aşıldı. Ayrıca projenin uzun vadeli sürdürülebilirliği düşünülerek modüler bir klasör hiyerarşisi (routers, models, schemas vb.) kurmak için iyi bir tasarım planlaması yapıldı.

**Gelecek hafta hedefim:**
- İstek uç noktalarının (API Endpoints) ve CRUD işlemlerinin tamamlanması, ayrıca geliştirilen uç noktaların test edilip hazır hale getirilmesi.

---
### Hafta 3 *(Tarih: 13.04.2026 - 29.04.2026)*

**Plandaki hedef:**
- İstek uç noktalarının (API Endpoints) ve CRUD işlemlerinin tamamlanması, geliştirilen uç noktaların test edilip hazır hale getirilmesi.

**Bu hafta yaptıklarım:**
- 13.04 - 26.04 tarihleri arasında vize sınavları nedeniyle proje çalışmalarına ara verildi.
- Hardware ve Software router'larına PATCH (güncelleme) endpoint'leri eklendi.
- GET endpoint'lerine arama ve filtreleme desteği getirildi (`name`, `category`, `vendor_id`, `compatibility_level`, `publisher` parametreleri).
- `HardwareUpdate` ve `SoftwareUpdate` Pydantic şemaları oluşturuldu; kısmi güncelleme (partial update) desteği sağlandı.
- Docker build süreci optimize edildi: Poetry bağımlılığı kaldırılarak `requirements.txt` + `pip` tabanlı daha hızlı ve sade bir Dockerfile yazıldı.
- pgAdmin konfigürasyonu düzeltildi (e-posta doğrulama hatası giderildi).
- Taskfile güncellendi; `dev` görevi artık API'yi Docker Compose üzerinden yönetiyor, `logs` görevi eklendi.
- Tüm endpoint'ler Swagger UI üzerinden başarıyla test edildi.

**Plana göre durumum:**
- Vize dönemi nedeniyle gecikme yaşansa da hafta 3 hedefleri 29.04 itibarıyla tam olarak tamamlandı. API katmanı production-ready bir yapıya kavuştu.

**Karşılaştığım sorunlar / zorluklar:**
- Poetry kurulum scripti Docker build sürecinde çok uzun süre aldığından `pip` + `requirements.txt` yaklaşımına geçildi.
- pgAdmin'in yeni sürümünde `.local` uzantılı e-posta adresleri geçersiz sayıldığından `docker-compose.yml` güncellendi.
- `poetry.lock` dosyasının Poetry 2.2.1 ile oluşturulmuş olmasına karşın Dockerfile'ın 1.8.2 pinlemiş olması uyumsuzluk yarattı ve düzeltildi.

**Gelecek hafta hedefim:**
- OCS Inventory veritabanından donanım ve yazılım verilerinin otomatik olarak çekilmesi; Pardus uyumluluk skorlama algoritmasının tasarlanması ve geliştirilmesi.

---
