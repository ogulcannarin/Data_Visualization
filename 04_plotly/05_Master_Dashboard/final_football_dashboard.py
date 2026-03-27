import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys

# 1. Veriyi yükle ve sütunu bul
try:
    df = pd.read_csv('player_stats.csv', encoding='latin-1')
    possible_cols = ['nationality', 'Nation', 'Nationality', 'nation', 'Country']
    nation_col = next((c for c in possible_cols if c in df.columns), df.columns[0])
except:
    print("Hata: Veri dosyası bulunamadı!")
    sys.exit()

# --- DASHBOARD TASARIMI ---
# 2 satır, 2 sütunluk dev bir yapı kuruyoruz
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}],  # Üst: Bar ve Pie
           [{"type": "scattergeo"}, {"type": "scatter3d"}]], # Alt: Harita ve 3D
    subplot_titles=("Ülke Bazlı Yetenek", "Oyuncu Dağılımı", 
                    "Dünya Oyuncu Haritası", "Fiziksel Analiz (3D)")
)

# 1. Bar Chart: Ülke Yetenekleri
top_nations = df.groupby(nation_col)['ball_control'].mean().sort_values(ascending=False).head(10)
fig.add_trace(go.Bar(x=top_nations.index, y=top_nations.values, name="Yetenek"), row=1, col=1)

# 2. Pie Chart: Oyuncu Dağılımı
nation_counts = df[nation_col].value_counts().head(10)
fig.add_trace(go.Pie(labels=nation_counts.index, values=nation_counts.values, name="Dağılım"), row=1, col=2)

# 3. Harita: Dünya Geneli
nation_map = df[nation_col].value_counts().reset_index()
nation_map.columns = ['Country', 'Count']
fig.add_trace(go.Choropleth(locations=nation_map['Country'], z=nation_map['Count'], 
                            locationmode='country names', showscale=False), row=2, col=1)

# 4. 3D Scatter: Boy-Kilo-Yetenek
fig.add_trace(go.Scatter3d(x=df['height'].head(200), y=df['weight'].head(200), z=df['ball_control'].head(200),
                           mode='markers', marker=dict(size=4, color=df['age'])), row=2, col=2)

# Görünüm Ayarları
fig.update_layout(height=900, title_text="Kaggle Plotly Kursu: Master Dashboard", template="plotly_dark")
fig.show()

# Final Çıktısı: Bu dosyayı patronuna gönderebilirsin!
fig.write_html("futbol_master_rapor.html")
print("Tebrikler! 'futbol_master_rapor.html' dosyası oluşturuldu.")