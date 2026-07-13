# Risk Analytics Dashboard
This project is a real-time Fraud Detection and Risk Analysis dashboard developed to monitor financial transactions, cybersecurity logs, and user risk scores on a relational database (PostgreSQL) architecture.The system architecture is designed to be fully compatible with Microsoft Azure SQL / PostgreSQL flexible cloud server infrastructures for optimized data processing performance.FeaturesDynamic Corporate Filtering: Real-time data segmentation based on country.Statistical and Mathematical Summary: Tracking of total turnover, approval/decline ratios, and average risk score ($\mu$).Cybersecurity-Focused Customer Querying: Advanced anomaly analysis engine including User ID-based details such as merchant, spending category, country of transaction, date, time, and IP address.PostgreSQL Database Architecture and Sample QueryThe core data layer of the project contains optimized relational tables (users and transactions) in PostgreSQL. The following SQL query is used to analyze high-risk and declined transactions suspected of fraud:
```sql
SELECT 
    u.user_id,
    u.risk_score,
    u.country,
    t.transaction_id,
    t.amount,
    t.status,
    t.decline_reason
FROM users u
JOIN transactions t ON u.user_id = t.user_id
WHERE u.risk_score > 0.80 AND t.status = 'Declined'
ORDER BY u.risk_score DESC, t.amount DESC
LIMIT 10;
```
## Technologies
Python 3.13 PostgreSQL 18 (Relational Database Management)Streamlit (Interactive Web Interface)Plotly Express (Data Visualization)SQLAlchemy and Psycopg (Database Drivers)
## Developer Name: 
Larin Tok
Academic: Istanbul Kultur University - Mathematics and Computer Science (4rd Year)
Internship Competencies: Microsoft and Nurol Holding - Nurol Invesment Bank

-------------------------------------------------------------------------------------------------------------------------------------

# Risk Analytics Dashboard

Bu proje, ilişkisel veritabanı (PostgreSQL) mimarisi üzerinde dönen finansal hareketleri, siber güvenlik loglarını ve kullanıcı risk skorlarını analitik olarak izlemek amacıyla geliştirilmiş gerçek zamanlı bir Sahtekarlık (Fraud) Tespit ve Risk Analiz panelidir. 

Sistem mimarisi, veri işleme performansı açısından Microsoft Azure SQL / PostgreSQL esnek bulut sunucu altyapılarına tam uyumlu olarak kurgulanmıştır.

## Özellikler
- Dinamik Kurumsal Filtreleme: Ülke bazlı anlık veri segmentasyonu.
- İstatistiki ve Matematiksel Özet: Toplam cirolar, onay/red oranları ve ortalama risk skoru (\mu) takibi.
- Siber Güvenlik Odaklı Müşteri Sorgulama: Kullanıcı ID bazlı; işlem yapılan şirket (merchant), harcama kategorisi, işlem ülkesi, tarih, giriş saat/dakika ve IP adresi detaylarını içeren gelişmiş anomali analiz motoru.

## PostgreSQL Veritabanı Mimarisi ve Örnek Sorgu
Projenin temel veri katmanı, PostgreSQL üzerinde optimize edilmiş ilişkisel tablolar (users ve transactions) içermektedir. Yüksek riskli ve sahtekarlık şüphesiyle reddedilmiş işlemleri analiz etmek için kullanılan örnek SQL sorgusu aşağıdadır:

```sql
SELECT 
    u.user_id,
    u.risk_score,
    u.country,
    t.transaction_id,
    t.amount,
    t.status,
    t.decline_reason
FROM users u
JOIN transactions t ON u.user_id = t.user_id
WHERE u.risk_score > 0.80 AND t.status = 'Declined'
ORDER BY u.risk_score DESC, t.amount DESC
LIMIT 10;
```
## Teknolojiler
Python 3.13

PostgreSQL 18 (İlişkisel Veritabanı Yönetimi)

Streamlit (İnteraktif Web Arayüzü)

Plotly Express (Veri Görselleştirme)

SQLAlchemy ve Psycopg (Veritabanı Sürücüleri)

## Geliştirici
İsim: Larin Tok

Akademik: İstanbul Kültür Üniversitesi - Matematik ve Bilgisayar Bilimleri (4. Sınıf)

Staj Yetkinlikleri: Microsoft Bilgisayar Sistemleri ve Nurol Holding - Nurol Yatırım Bankası A.Ş.
