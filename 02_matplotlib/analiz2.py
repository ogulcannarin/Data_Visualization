import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Veriyi yükle
try:
    df = pd.read_csv('player_stats.csv', encoding='latin-1', low_memory=False)
    print("Veri başarıyla yüklendi!")
except FileNotFoundError:
    print("Dosya bulunamadı! Lütfen dosya yolunu kontrol et.")

# Sütun İsimleri
name_col = 'player'
attributes = ['ball_control', 'dribbling', 'marking', 'slide_tackle', 'age']

# --- FİGÜR 1: RADAR GRAFİĞİ (Senin Orijinal Kodun) ---
data_radar = df.nlargest(2, 'ball_control')[[name_col] + attributes]
labels = np.array(attributes)
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig_radar, ax_radar = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i, row in data_radar.iterrows():
    values = row[attributes].values.flatten().tolist()
    values += values[:1]
    ax_radar.plot(angles, values, linewidth=2, label=row[name_col])
    ax_radar.fill(angles, values, alpha=0.25)

ax_radar.set_theta_offset(np.pi / 2)
ax_radar.set_theta_direction(-1)
ax_radar.set_thetagrids(np.degrees(angles[:-1]), labels)
ax_radar.set_ylim(0, 100)
plt.title('Oyuncu Yetenek Karşılaştırması (Radar)', y=1.1, size=15)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))


# --- FİGÜR 2: ANALİZ PANELİ (Subplots - Kaggle Rehberi Mantığı) ---
# 1 Satır, 3 Sütunluk bir panel oluşturuyoruz
fig, axes = plt.subplots(1, 3, figsize=(20, 6))
fig.suptitle('Oyuncu Veri Analiz Paneli', fontsize=20)

# Grafik 1: Histogram (Yaş Dağılımı)

axes[0].hist(df['age'].dropna(), bins=15, color='skyblue', edgecolor='black')
axes[0].set_title('Yaş Dağılımı')
axes[0].set_xlabel('Yaş')
axes[0].set_ylabel('Oyuncu Sayısı')

# Grafik 2: Scatter Plot (Ball Control vs Dribbling)

scatter = axes[1].scatter(df['ball_control'], df['dribbling'], alpha=0.5, c=df['age'], cmap='viridis')
axes[1].set_title('Top Kontrolü vs Dribbling')
axes[1].set_xlabel('Ball Control')
axes[1].set_ylabel('Dribbling')
fig.colorbar(scatter, ax=axes[1], label='Yaş Ölçeği')

# Grafik 3: Bar Plot (En İyi 5 Oyuncu)

top_5 = df.nlargest(5, 'ball_control')
axes[2].bar(top_5[name_col], top_5['ball_control'], color='salmon')
axes[2].set_title('Zirvedeki 5 Oyuncu (Top Kontrolü)')
axes[2].set_ylabel('Puan')
plt.setp(axes[2].get_xticklabels(), rotation=45) # İsimleri eğik yap

# Grafiklerin birbirine girmemesi için düzenleme
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()