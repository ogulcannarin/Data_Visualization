import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Veriyi yükle
try:
    df = pd.read_csv('player_stats.csv', encoding='latin-1', low_memory=False)
    print("Veri başarıyla yüklendi!")
except FileNotFoundError:
    print("Dosya bulunamadı! Lütfen yolu kontrol et.")

# Sütun ayarları
name_col = 'player'
attributes = ['ball_control', 'dribbling', 'marking', 'slide_tackle', 'age']

# --- ANALİZ PANELİ OLUŞTURMA (Subplots) ---
# Kurs rehberlerindeki "Multiple Plots" mantığıyla 1 satır 3 sütun hazırlıyoruz
fig, axes = plt.subplots(1, 3, figsize=(22, 7))
fig.suptitle('Matplotlib Eğitim Projesi: Profesyonel Oyuncu Analizi', fontsize=20, fontweight='bold')

# --- 1. GRAFİK: Yaş Dağılımı (Histogram + Annotation) ---
axes[0].hist(df['age'].dropna(), bins=15, color='skyblue', edgecolor='black', alpha=0.7)
axes[0].set_title('Yaş Dağılımı ve Ortalama', fontsize=14)
axes[0].set_xlabel('Yaş')
axes[0].set_ylabel('Oyuncu Sayısı')

# İleri Seviye: Ortalama çizgisi ekleme (Customizing Plots)
yas_ort = df['age'].mean()
axes[0].axvline(yas_ort, color='red', linestyle='--', linewidth=2, label=f'Ort: {yas_ort:.1f}')
# İleri Seviye: Metin notu ekleme (Working with Legends & Text)
axes[0].text(yas_ort + 1, 800, f'Ortalama: {yas_ort:.1f}', color='red', fontweight='bold')
axes[0].legend()

# --- 2. GRAFİK: Yetenek İlişkisi (Scatter + Arrow Annotation) ---
# Sani Kamal rehberindeki "Data Visualization" teknikleriyle renklendirme
scatter = axes[1].scatter(df['ball_control'], df['dribbling'], alpha=0.5, c=df['age'], cmap='viridis')
axes[1].set_title('Top Kontrolü vs Dribbling İlişkisi', fontsize=14)
axes[1].set_xlabel('Ball Control')
axes[1].set_ylabel('Dribbling')
fig.colorbar(scatter, ax=axes[1], label='Yaş Ölçeği')

# İleri Seviye: En iyi oyuncuyu okla gösterme (Annotations)
top_player = df.loc[df['ball_control'].idxmax()]
axes[1].annotate(top_player[name_col], 
                 xy=(top_player['ball_control'], top_player['dribbling']),
                 xytext=(top_player['ball_control']-30, top_player['dribbling']+5),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=7),
                 fontsize=12, fontweight='bold', color='darkred')

# --- 3. GRAFİK: Zirvedeki 5 Oyuncu (Bar Plot + Value Labels) ---
top_5 = df.nlargest(5, 'ball_control')
bars = axes[2].bar(top_5[name_col], top_5['ball_control'], color='salmon', alpha=0.8)
axes[2].set_title('En İyi 5 Oyuncu (Top Kontrolü)', fontsize=14)
axes[2].set_ylabel('Yetenek Puanı')
plt.setp(axes[2].get_xticklabels(), rotation=30, ha='right')

# İleri Seviye: Sütun üzerine değerleri yazdırma (Customizing)
for bar in bars:
    yval = bar.get_height()
    axes[2].text(bar.get_x() + bar.get_width()/2, yval + 1, yval, ha='center', va='bottom', fontweight='bold')

# --- GENEL DÜZENLEME (Layout) ---
# Kurslarda vurgulanan grafiklerin birbirine girmemesi için "tight_layout"
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.grid(True, linestyle=':', alpha=0.3) # Arka plana hafif ızgara ekle
plt.show()