import pandas as pd
import plotly.express as px
import sys

# 1. Veriyi yükle
try:
    df = pd.read_csv('player_stats.csv', encoding='latin-1')
    print("Veri yüklendi!")
except FileNotFoundError:
    print("HATA: player_stats.csv bulunamadı!")
    sys.exit()

# --- AKILLI SÜTUN BULUCU ---
# Senin verindeki gerçek sütun adını bulalım (Büyük-küçük harf duyarlılığını aşar)
possible_cols = ['nationality', 'Nation', 'Nationality', 'nation', 'Country', 'country']
nation_col = None

for col in possible_cols:
    if col in df.columns:
        nation_col = col
        break

if nation_col is None:
    print(f"HATA: Ülke sütunu bulunamadı! Mevcut sütunlar: {df.columns.tolist()}")
    sys.exit()
else:
    print(f"Bulunan ülke sütunu: '{nation_col}'")

# 2. Ülke bazlı oyuncu sayılarını hesapla
nation_counts = df[nation_col].value_counts().reset_index()
nation_counts.columns = ['Country', 'Count']

# 3. Dünya Haritası (Choropleth)


fig = px.choropleth(nation_counts, 
                    locations="Country", 
                    locationmode='country names', # Ülke isimlerini dünya haritasına eşler
                    color="Count", 
                    hover_name="Country", 
                    color_continuous_scale=px.colors.sequential.YlOrRd, # Sarıdan kırmızıya sıcaklık haritası
                    title="Dünya Haritası: Oyuncu Yoğunluğu Analizi")

fig.update_layout(
    template="plotly_dark",
    margin={"r":0,"t":50,"l":0,"b":0} # Haritayı tam ekran yapalım
)

fig.show()