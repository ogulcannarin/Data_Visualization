import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 1. VERİ YÜKLEME
try:
    df = pd.read_csv('player_stats.csv', encoding='latin-1')
    print("Veri başarıyla yüklendi!")
except FileNotFoundError:
    print("HATA: 'player_stats.csv' dosyası bulunamadı. Lütfen dosya yolunu kontrol et.")

# Sütun isimlerini kontrol edelim (Senin verine göre)
name_col = 'player' if 'player' in df.columns else df.columns[0]

# ---------------------------------------------------------
# KURS ADIMI 1: RADAR CHART (Senin Başladığın Bölüm)
# ---------------------------------------------------------
categories = ['ball_control', 'dribbling', 'marking', 'slide_tackle', 'age']
player1 = df.iloc[0]
player2 = df.iloc[1]

fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
      r=[player1[c] for c in categories],
      theta=categories,
      fill='toself',
      name=player1[name_col]
))
fig_radar.add_trace(go.Scatterpolar(
      r=[player2[c] for c in categories],
      theta=categories,
      fill='toself',
      name=player2[name_col]
))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    title=f"BÖLÜM 1: {player1[name_col]} vs {player2[name_col]} Radar Analizi",
    template="plotly_dark"
)
fig_radar.show()

# ---------------------------------------------------------
# KURS ADIMI 2: LINE CHART (Rehberdeki 'Citation vs Teaching' Mantığı)
# ---------------------------------------------------------
# İlk 20 oyuncunun yetenek değişimini çizgiyle görelim
top_20 = df.head(20)
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=top_20[name_col], y=top_20['ball_control'],
                    mode='lines+markers', name='Top Kontrolü',
                    marker=dict(color='rgba(16, 112, 2, 0.8)')))
fig_line.add_trace(go.Scatter(x=top_20[name_col], y=top_20['dribbling'],
                    mode='lines', name='Dribbling',
                    line=dict(color='rgba(255, 0, 0, 0.8)', dash='dash')))

fig_line.update_layout(title='BÖLÜM 2: Yetenek Değişim Trendi (Line Chart)',
                  xaxis_title='Oyuncular', yaxis_title='Puan',
                  template="plotly_white")
fig_line.show()

# ---------------------------------------------------------
# KURS ADIMI 3: SCATTER CHART (İlişki ve Balon Grafiği)
# ---------------------------------------------------------
# Boy ve Kilo arasındaki ilişkiyi, yetenek büyüklüğüyle görelim
fig_scatter = px.scatter(df.head(100), x="height", y="weight",
                 size="ball_control", color="age",
                 hover_name=name_col, 
                 title="BÖLÜM 3: Boy-Kilo İlişkisi (Boyut: Yetenek, Renk: Yaş)")
fig_scatter.show()

# Portfolyo için HTML olarak kaydet
fig_radar.write_html("1_radar_analizi.html")
print("Grafikler oluşturuldu ve HTML olarak kaydedildi!")