import pandas as pd
import plotly.graph_objects as go

# 1. Veriyi yükle
df = pd.read_csv('player_stats.csv', encoding='latin-1')

# 2. Analiz edilecek özellikleri seç (Daha önce öğrendiğimiz sütun isimleri)
categories = ['ball_control', 'dribbling', 'marking', 'slide_tackle', 'age']

# 3. İki oyuncu seçelim (Senin verindeki ilk 2 oyuncu veya isimle filtreleme yapabilirsin)
player1 = df.iloc[0]
player2 = df.iloc[1]

# 4. Plotly ile Radar Grafiği Oluşturma
fig = go.Figure()

# Birinci Oyuncu
fig.add_trace(go.Scatterpolar(
      r=[player1[c] for c in categories],
      theta=categories,
      fill='toself',
      name=player1['player']
))

# İkinci Oyuncu
fig.add_trace(go.Scatterpolar(
      r=[player2[c] for c in categories],
      theta=categories,
      fill='toself',
      name=player2['player']
))

# Grafik Düzenlemeleri
fig.update_layout(
  polar=dict(
    radialaxis=dict(visible=True, range=[0, 100])),
  showlegend=True,
  title=f"{player1['player']} vs {player2['player']} Karşılaştırması"
)

# 5. Göster ve HTML olarak kaydet (Portfolyo için çok önemli!)
fig.show()
fig.write_html("oyuncu_kiyaslama.html")