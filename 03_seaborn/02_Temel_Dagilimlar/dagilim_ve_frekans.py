import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Veriyi yükle
try:
    df = pd.read_csv('../data/player_stats.csv', encoding='latin-1', low_memory=False)
    print("Veri başarıyla yüklendi!")
except FileNotFoundError:
    print("Dosya bulunamadı!")

# Seaborn Stil Ayarı (Kaan Can'ın rehberinde vurguladığı modern görünüm)
sns.set(style="whitegrid")

# --- GRAFİK 1: HEATMAP (Korelasyon Matrisi) ---
# Senin başladığın harika Heatmap analizi
cols_to_analyze = ['age', 'ball_control', 'dribbling', 'marking', 'slide_tackle', 'height', 'weight']
corr_matrix = df[cols_to_analyze].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Özellikler Arasındaki Korelasyon Isı Haritası', fontsize=15)
plt.show()

# --- GRAFİK 2: SCATTER PLOT (Hue Parametresi ile) ---
# Rehberdeki en önemli özellik: Üçüncü bir boyutu (Age) renk ile eklemek
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ball_control', y='dribbling', hue='age', palette='viridis', alpha=0.6)
plt.title('Ball Control vs Dribbling (Yaş Gruplarına Göre Renklendirilmiş)', fontsize=14)
plt.show()

# --- GRAFİK 3: JOINT PLOT (İlişki + Dağılım) ---
# Hem scatter hem histogramı birleştiren, kurstaki en havalı grafiklerden biri
# kind='hex' verinin yoğun olduğu yerleri altıgenlerle gösterir

sns.jointplot(data=df, x='height', y='weight', kind='hex', color='#4CB391', height=8)
plt.suptitle('Boy ve Kilo İlişkisi & Yoğunluğu', y=1.02)
plt.show()

# --- GRAFİK 4: VIOLIN PLOT (Keman Grafiği) ---
# Kutu grafiklerinden (Box plot) daha gelişmiş bir dağılım görseli
# Sadece en çok görülen yaşları filtreleyelim ki grafik temiz görünsün
top_ages = df['age'].value_counts().head(10).index
df_filtered = df[df['age'].isin(top_ages)]


plt.figure(figsize=(12, 6))
sns.violinplot(data=df_filtered, x='age', y='ball_control', palette='muted', split=True)
plt.title('Yaşlara Göre Ball Control Dağılımı (Violin Plot Analysis)', fontsize=14)
plt.show()

# --- GRAFİK 5: COUNT PLOT ---
# Kategorik verilerin sayısını göstermek için (Rehberdeki basit ama etkili grafik)
plt.figure(figsize=(10, 5))
sns.countplot(data=df_filtered, x='age', palette='magma')
plt.title('Veri Setindeki Yaş Dağılımı (Oyuncu Sayısı)', fontsize=14)
plt.show()