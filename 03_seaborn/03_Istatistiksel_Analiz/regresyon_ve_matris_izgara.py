import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Veriyi yükle
try:
    df = pd.read_csv('../data/player_stats.csv', encoding='latin-1', low_memory=False)
    print("Veri başarıyla yüklendi!")
except FileNotFoundError:
    print("Dosya bulunamadı! Lütfen dosya yolunu kontrol et.")

# Seaborn varsayılan stilini ayarla (Rehberdeki ilk adım)
sns.set(style="whitegrid")

# --- 1. BÖLÜM: KORELASYON ANALİZİ (Heatmap) ---
# Özellikler arasındaki sayısal ilişkiyi görmek için
cols = ['age', 'ball_control', 'dribbling', 'marking', 'slide_tackle', 'height', 'weight']
plt.figure(figsize=(10, 8))
sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Özellikler Arasındaki Korelasyon (Heatmap)')
plt.show()

# --- 2. BÖLÜM: İLİŞKİ VE TAHMİN (Scatter & Lmplot) ---
# Ball Control ve Dribbling arasındaki ilişkiyi regresyon çizgisiyle görelim

sns.lmplot(data=df, x='ball_control', y='dribbling', hue='age', 
           palette='viridis', height=7, aspect=1.2)
plt.title('Yetenek İlişkisi ve Regresyon Tahmini (Lmplot)')
plt.show()

# --- 3. BÖLÜM: YOĞUNLUK VE DAĞILIM (Joint Plot) ---
# Hem saçılım hem de histogramları tek grafikte birleştirme

sns.jointplot(data=df, x='ball_control', y='dribbling', kind='hex', color='#4CB391')
plt.suptitle('Yetenek Yoğunluğu (Hexbin Joint Plot)', y=1.02)
plt.show()

# --- 4. BÖLÜM: KATEGORİK ANALİZ (Violin Plot) ---
# Belirli yaşlardaki yetenek dağılımını "Keman" grafiğiyle görelim
selected_ages = [20, 25, 30, 35]
df_sub = df[df['age'].isin(selected_ages)]

plt.figure(figsize=(12, 6))
sns.violinplot(data=df_sub, x='age', y='ball_control', inner="quart", palette="pastel")
plt.title('Seçili Yaşlara Göre Yetenek Dağılımı (Violin Plot)')
plt.show()

# --- 5. BÖLÜM: DEĞİŞKEN MATRİSİ (Pair Plot) ---
# Rehberdeki en güçlü araç: Her şeyin her şeyle ilişkisi

small_cols = ['age', 'ball_control', 'dribbling']
sns.pairplot(df[small_cols], hue='age', palette='husl', diag_kind="kde")
plt.suptitle('Tüm Değişkenlerin İlişki Matrisi (Pair Plot)', y=1.02)
plt.show()

# --- 6. BÖLÜM: BÖL VE YÖNET (FacetGrid) ---
# Veriyi yaş gruplarına göre yan yana kutucuklarda inceleyelim
g = sns.FacetGrid(df_sub, col="age", height=4, aspect=1)
g.map(sns.histplot, "ball_control", kde=True, color="orange")
plt.show()