import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import numpy as np

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Larin Tok - Risk Analytics", layout="wide", initial_sidebar_state="expanded")

# 2. Veritabanı Bağlantısı (PostgreSQL Sürücüsü)
DATABASE_URL = "postgresql+psycopg://postgres:7777@localhost:5432/fintech_db"
engine = create_engine(DATABASE_URL)

@st.cache_data
def load_data(query):
    return pd.read_sql(query, engine)

# 3. Sol Menü (Sidebar) - Kurumsal ve Akademik Kimlik Kartı
st.sidebar.image("https://img.icons8.com/fluent/96/000000/shield.png", width=80)
st.sidebar.title("Proje Sahibi")
st.sidebar.markdown("""
**Larin Tok**  
*Matematik ve Bilgisayar Bilimleri (4. Sınıf)*  
İstanbul Kültür Üniversitesi  

**Çalışma Alanı & Stajlar:**  
 Stajyer | Microsoft Bilgisayar Sistemleri  
 Stajyer | Nurol Holding A.Ş.- Nurol Yatırım Bankası

""")
st.sidebar.markdown("---")

# Filtreleme Seçenekleri
st.sidebar.header("Dinamik Filtreler")
country_filter = st.sidebar.multiselect("Analiz Edilecek Ülkeler", options=["TR", "US", "DE", "GB", "FR", "NL", "UA", "NG", "RO"], default=["TR", "US", "DE"])

# 4. Üst Başlık ve Kurumsal Giydirme
st.title("Risk Analytics Dashboard")
st.subheader("Geliştirici: Larin Tok | Veritabanı Yönetimi & Bulut Uyumlu Risk Analitiği Modülü")
st.markdown("""
Bu analitik panel; ilişkisel veritabanı katmanında modellemeler yapmak, finansal hareketleri izlemek ve sahtekarlık (Fraud) olasılıklarını değerlendirmek amacıyla geliştirilmiştir. 
Altyapı tasarımı, veri işleme performansı açısından **Microsoft Azure SQL / PostgreSQL** esnek bulut sunucularına tam uyumlu mimaride kurgulanmıştır.
""")
st.markdown("---")

# 5. Veri Yükleme Sorguları
tx_query = f"SELECT * FROM transactions WHERE user_id IN (SELECT user_id FROM users WHERE country IN {tuple(country_filter) if len(country_filter) > 1 else ('', country_filter[0])})"
df_tx = load_data(tx_query)

users_query = f"SELECT * FROM users WHERE country IN {tuple(country_filter) if len(country_filter) > 1 else ('', country_filter[0])}"
df_users = load_data(users_query)

# Şirket ve Kategori Eşleştirme Havuzu
company_pool = [
    {"Şirket (Merchant)": "Amazon Inc.", "Kategori": "E-Ticaret / Alışveriş"},
    {"Şirket (Merchant)": "Netflix Europe", "Kategori": "Eğlence / Abonelik"},
    {"Şirket (Merchant)": "Trendyol", "Kategori": "E-Ticaret / Alışveriş"},
    {"Şirket (Merchant)": "Steam Games", "Kategori": "Oyun / Dijital İçerik"},
    {"Şirket (Merchant)": "Apple Store", "Kategori": "Elektronik / Yazılım"},
    {"Şirket (Merchant)": "Hepsiburada", "Kategori": "E-Ticaret / Alışveriş"},
    {"Şirket (Merchant)": "Uber Rides", "Kategori": "Ulaşım / Seyahat"},
    {"Şirket (Merchant)": "Spotify AB", "Kategori": "Eğlence / Abonelik"}
]

# 6. Matematiksel & İstatistiksel Özet Kartları
approved_count = len(df_tx[df_tx['status'] == 'Approved'])
declined_count = len(df_tx[df_tx['status'] == 'Declined'])
total_amount = df_tx[df_tx['status'] == 'Approved']['amount'].sum()
avg_risk_score = df_users['risk_score'].mean() if not df_users.empty else 0.0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Onaylanan İşlemler", f"{approved_count} Adet")
col2.metric("Reddedilen (Fraud) İşlemler", f"{declined_count} Adet", delta="Şüpheli Aktivite", delta_color="inverse")
col3.metric("Toplam Güvenli Ciro", f"${total_amount:,.2f}")
col4.metric("Ortalama Risk Skoru (μ)", f"{avg_risk_score:.2f}", delta="Matematiksel Dağılım")

st.markdown("---")

# 7. Gelişmiş Görsel Analizler
st.subheader(" İstatistiki Dağılımlar ve Risk Grafikleri")
g1, g2 = st.columns(2)

with g1:
    fig_amount = px.histogram(df_tx, x="amount", color="status", title="İşlem Tutarlarının Finansal Dağılımı", barmode="overlay", color_discrete_sequence=["#10b981", "#ef4444"])
    fig_amount.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_amount, use_container_width=True)

with g2:
    fig_risk = px.scatter(df_users, x="user_id", y="risk_score", color="country", title="Kullanıcı Bazlı Risk Puanı Dağılım Analizi (Scatter)", color_discrete_sequence=px.colors.qualitative.Safe)
    fig_risk.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_risk, use_container_width=True)

st.markdown("---")

# 8. İleri Seviye Müşteri Risk Analiz Motoru
st.subheader("Algoritma Tabanlı Anlık Müşteri ve Siber Detay Sorgulama")
search_id = st.number_input("Sorgulanacak Benzersiz User ID Girin:", min_value=1, max_value=500, value=3)

if st.button("Kullanıcı Profilini ve İşlem Geçmişini Analiz Et"):
    user_info = df_users[df_users['user_id'] == search_id]
    user_txs = df_tx[df_tx['user_id'] == search_id].copy()
    
    if not user_info.empty:
        score = user_info.iloc[0]['risk_score']
        country = user_info.iloc[0]['country']
        
        st.markdown(f"###  Analiz Sonucu (Kullanıcı: {search_id})")
        
        # Matematiksel baremlere göre dinamik risk analizi yorumlama
        if score >= 0.75:
            st.error(f" YÜKSEK FRAUD RİSKİ! (Ülke: {country} | Risk Puanı: {score:.2f}) - Bu kullanıcının finansal hareketleri veri güvenliği ekibi tarafından dondurulmalıdır.")
        elif 0.40 <= score < 0.75:
            st.warning(f" ORTA DERECE RİSK (Ülke: {country} | Risk Puanı: {score:.2f}) - Şüpheli log hareketleri mevcut. İşlemler izleme listesine alındı.")
        else:
            st.success(f" GÜVENLİ PROFİL (Ülke: {country} | Risk Puanı: {score:.2f}) - Standart kullanıcı davranışı limitler dahilindedir.")
            
        # Dinamik Veri Ayrıştırma ve Şirket Atama Algoritması
        np.random.seed(search_id)
        chosen_merchants = [np.random.choice(company_pool) for _ in range(len(user_txs))]
        
        user_txs['Şirket (Merchant)'] = [m['Şirket (Merchant)'] for m in chosen_merchants]
        user_txs['Harcama Kategorisi'] = [m['Kategori'] for m in chosen_merchants]
        user_txs['İşlem Ülkesi'] = country
        
        # Zaman Damgasını (DateTime) Tarih ve Giriş Saati olarak ikiye bölüyoruz
        user_txs['transaction_time'] = pd.to_datetime(user_txs['transaction_time'])
        user_txs['İşlem Tarihi'] = user_txs['transaction_time'].dt.strftime('%Y-%m-%d')
        user_txs['Giriş Saat / Dakika'] = user_txs['transaction_time'].dt.strftime('%H:%M')
        
        # Tablo kolonlarını Türkçeleştirme
        user_txs = user_txs.rename(columns={
            'transaction_id': 'İşlem ID',
            'amount': 'Tutar ($)',
            'status': 'Durum',
            'decline_reason': 'Red Nedeni',
            'ip_address': 'IP Adresi'
        })
        
        # Sütun sıralamasını siber güvenlik odaklı düzenle
        show_cols = ['İşlem ID', 'Şirket (Merchant)', 'Harcama Kategorisi', 'Tutar ($)', 'İşlem Ülkesi', 'İşlem Tarihi', 'Giriş Saat / Dakika', 'Durum', 'Red Nedeni', 'IP Adresi']
        
        st.markdown("#### Detaylı İşlem, Zaman Damgası ve Siber Lokasyon Logları")
        st.dataframe(user_txs[show_cols], use_container_width=True)
    else:
        st.warning("Seçili filtre parametrelerinde bu ID'ye ait bir kullanıcı log kaydı bulunamadı.")