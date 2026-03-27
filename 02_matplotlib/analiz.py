import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 

# 1. Veriyi yükle
try:
    df = pd.read_csv('player_stats.csv', encoding='latin-1', low_memory=False)
    print("Veri başarıyla yüklendi!")
    print("\nVerindeki Sütun İsimleri:", df.columns.tolist()) # Hatanın kaynağını görmek için
except FileNotFoundError:
    print("Dosya bulunamadı!")

# --- HATA DÜZELTME BÖLÜMÜ ---
# Verinde 'nationality' yoksa, alternatif isimleri kontrol edelim
possible_nation_cols = ['nationality', 'nation', 'Country', 'country', 'country_name']
nation_col = None

for col in possible_nation_cols:
    if col in df.columns:
        nation_col = col
        break

if nation_col is None:
    print("\nUYARI: Uyruk (Nationality) sütunu bulunamadı! Lütfen yukarıdaki listeden uygun sütun ismini seç.")
    # Eğer hiçbiri yoksa hata vermemesi için ilk sütunu seçelim (geçici çözüm)
    nation_col = df.columns[0] 
# ----------------------------

plt.style.use('ggplot')

# --- FİGÜR 1: PASTA GRAFİĞİ ---
top_countries = df[nation_col].value_counts().head(5)

plt.figure(figsize=(10, 7))
explode = (0.1, 0, 0, 0, 0) 

plt.pie(top_countries, 
        labels=top_countries.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        explode=explode, 
        shadow=True, 
        colors=plt.cm.viridis(np.linspace(0, 1, 5)))

plt.title(f'En Çok Oyuncusu Olan İlk 5 Ülke ({nation_col})', fontsize=15, fontweight='bold')
plt.show()

# --- FİGÜR 2: 3D SAÇILIM GRAFİĞİ ---
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

x = df['age']
y = df['ball_control']
z = df['dribbling']

p3d = ax.scatter(x, y, z, c=z, cmap='magma', s=50, alpha=0.6, edgecolors='w')

ax.set_xlabel('Yaş')
ax.set_ylabel('Ball Control')
ax.set_zlabel('Dribbling')
ax.set_title('3 Boyutlu Yetenek Analizi')

fig.colorbar(p3d, ax=ax, label='Dribbling Puanı', shrink=0.5, aspect=10)
plt.show()