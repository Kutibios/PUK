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
| 2 | GG.AA - GG.AA | PUK Çekirdek Servisi API ve Veritabanı Şeması Tasarımı | %20 | 🔄 Devam Ediyor |
| 3 | GG.AA - GG.AA | İstek Uç Noktalarının (API Endpoints) ve CRUD İşlemlerinin Yazılması | %30 | ⬜ Başlamadı |
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

