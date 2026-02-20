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

# --- OTOMATİK SÜTUN BULUCU (Hata Engelleyici) ---
# 'nationality' yerine geçebilecek isimleri kontrol et
possible_cols = ['nationality', 'nation', 'Country', 'country', 'country_name']
nation_col = next((c for c in possible_cols if c in df.columns), df.columns[0])
name_col = 'player' if 'player' in df.columns else df.columns[0]
# -----------------------------------------------

sns.set_theme(style="darkgrid")

# --- BÖLÜM 1: ÜLKE ANALİZİ (Gelişmiş Renklerle) ---
plt.figure(figsize=(12, 6))
top_nations = df[nation_col].value_counts().head(8)
sns.barplot(x=top_nations.values, y=top_nations.index, palette='mako')
plt.title(f'Ülkelere Göre Oyuncu Sayısı ({nation_col})', fontsize=14)
plt.show()

# --- BÖLÜM 2: ANNOTATIONS (Özel İşaretleme) ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='ball_control', alpha=0.3, color='gray')

# En yüksek ball_control değerine sahip oyuncuyu bulalım
top_idx = df['ball_control'].idxmax()
best_player = df.loc[top_idx]

# İşaretleyici (Ok ve Yazı)
plt.annotate(f"Yetenek Zirvesi: {best_player[name_col]}", 
             xy=(best_player['age'], best_player['ball_control']), 
             xytext=(best_player['age'] + 4, best_player['ball_control'] - 10),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10, fontweight='bold', color='red')

plt.title('Yaş ve Yetenek: Zirve Analizi', fontsize=14)
plt.show()

# --- BÖLÜM 3: PIVOT TABLE & HEATMAP (Kursun "Pro" Seviyesi) ---
# Bu bölüm Sani Kamal kursunun en can alıcı noktasıdır: Veriyi matrise çevirmek.
# Yaş ve Ülke bazında ortalama yeteneği görelim
top_5_nations = df[nation_col].value_counts().head(5).index
subset = df[df[nation_col].isin(top_5_nations)]

# Veriyi Heatmap için pivot tabloya çeviriyoruz
pivot_table = subset.pivot_table(index=nation_col, columns='age', values='ball_control', aggfunc='mean').fillna(0)



plt.figure(figsize=(14, 6))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=False)
plt.title('Ülke ve Yaşa Göre Ortalama Yetenek Matrisi')
plt.show()