import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import sys

# 1. Veriyi yükle
try:
    df = pd.read_csv('player_stats.csv', encoding='latin-1')
    print("Veri başarıyla yüklendi!")
except FileNotFoundError:
    print("HATA: Dosya bulunamadı!")
    sys.exit()

# --- OTOMATİK SÜTUN BULUCU (Hata Engelleyici) ---
possible_nation_cols = ['nationality', 'nation', 'Country', 'country']
nation_col = next((c for c in possible_nation_cols if c in df.columns), df.columns[0])
print(f"Kullanılan ülke sütunu: {nation_col}")

# --- KURS ADIMI: BUBBLE CHART (Kabarcık Grafiği) ---
# Kaan Can rehberinde "World Rank vs Teaching" gibi ilişkileri balonlarla anlatır.
# Biz: Boy vs Kilo ilişkisini, top kontrolü (balon boyutu) ile görelim.
fig_bubble = px.scatter(df.head(100), x="height", y="weight",
                 size="ball_control", color="age",
                 hover_name=df.columns[0], # İlk sütun genelde isimdir
                 size_max=30,
                 title="Bubble Chart: Boy-Kilo İlişkisi (Boyut=Yetenek)")
fig_bubble.show()

# --- KURS ADIMI: HISTOGRAM (İstatistiksel Dağılım) ---
# Oyuncuların yaş dağılımını görmek için kullanılır.

fig_hist = px.histogram(df, x="age", 
                   nbins=20, 
                   title='Oyuncu Yaş Dağılımı (Histogram)',
                   color_discrete_sequence=['indianred'],
                   marginal="rug") # Alt kısma barkod çizgileri ekler
fig_hist.show()

# --- KURS ADIMI: GÜNCELLENMİŞ BAR CHART (Hata Vermeyen Versiyon) ---
top_5_nations = df.groupby(nation_col)[['ball_control', 'dribbling']].mean().sort_values(by='ball_control', ascending=False).head(5)

fig_bar = go.Figure(data=[
    go.Bar(name='Ort. Ball Control', x=top_5_nations.index, y=top_5_nations['ball_control']),
    go.Bar(name='Ort. Dribbling', x=top_5_nations.index, y=top_5_nations['dribbling'])
])
fig_bar.update_layout(barmode='group', title='Ülkelere Göre Yetenek Ortalamaları')