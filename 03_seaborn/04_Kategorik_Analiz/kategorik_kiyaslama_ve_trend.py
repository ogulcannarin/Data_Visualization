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

# Seaborn Stil Ayarı (Kursun vazgeçilmezi)
sns.set_theme(style="whitegrid")

# --- BÖLÜM 1: İSTATİSTİKSEL İLİŞKİLER (Correlation & Regression) ---
cols = ['age', 'ball_control', 'dribbling', 'marking', 'slide_tackle']
plt.figure(figsize=(10, 8))
sns.heatmap(df[cols].corr(), annot=True, cmap='RdYlGn', fmt=".2f")
plt.title('Korelasyon Isı Haritası')
plt.show()

# Lmplot: Regresyon ve Güven Aralığı

sns.lmplot(data=df, x='ball_control', y='dribbling', hue='age', palette='magma', height=6)
plt.title('Yetenekler Arası Regresyon ve Trend Analizi')
plt.show()

# --- BÖLÜM 2: DAĞILIM ANALİZİ (Joint & Violin) ---
# Jointplot: Hem scatter hem dağılım
sns.jointplot(data=df, x='height', y='weight', kind='kde', color="purple")
plt.suptitle('Boy ve Kilo Yoğunluk Analizi (KDE)', y=1.02)
plt.show()

# Violin Plot: Yoğunluk ve Yayılım
selected_ages = [20, 25, 30, 35]
df_filtered = df[df['age'].isin(selected_ages)]
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_filtered, x='age', y='ball_control', palette='Set2')
plt.title('Yaşlara Göre Yetenek Yoğunluğu (Violin Plot)')
plt.show()

# --- BÖLÜM 3: KATEGORİK ANALİZ (Bar, Point & Count Plot) ---
# En çok oyuncusu olan 5 ülkeyi filtrele
top_nations = df['nationality'].value_counts().head(5).index
df_nations = df[df['nationality'].isin(top_nations)]

# Bar Plot: Ortalamaları Kıyasla

plt.figure(figsize=(10, 6))
sns.barplot(data=df_nations, x='nationality', y='ball_control', palette='viridis')
plt.title('Ülkelere Göre Ortalama Yetenek Puanları')
plt.show()

# Point Plot: Değişim Trendini Gör

plt.figure(figsize=(10, 6))
sns.pointplot(data=df_filtered, x='age', y='ball_control', color='red', markers="o", linestyles="-")
sns.pointplot(data=df_filtered, x='age', y='dribbling', color='blue', markers="x", linestyles="--")
plt.title('Yaşa Bağlı Yetenek Değişim Trendi (Kırmızı: Ball Ctrl, Mavi: Dribbling)')
plt.show()

# --- BÖLÜM 4: ÇOKLU ANALİZ (Pair Plot & FacetGrid) ---
# Pair Plot: Tüm sayısal değişkenlerin matrisi

sns.pairplot(df[['age', 'ball_control', 'dribbling']], hue='age', palette='coolwarm')
plt.show()

# FacetGrid: Veriyi yaşlara göre bölüp histogram çizdirme
g = sns.FacetGrid(df_filtered, col="age", height=4)
g.map(sns.histplot, "ball_control", color="teal", kde=True)
plt.show()