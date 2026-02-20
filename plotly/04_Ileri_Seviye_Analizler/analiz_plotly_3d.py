import pandas as pd
import plotly.express as px

# Veriyi yükle
df = pd.read_csv('player_stats.csv', encoding='latin-1')

# 3D Scatter Plot
# İlk 500 oyuncuyu alalım ki tarayıcı kasmadan dönebilsin
fig_3d = px.scatter_3d(df.head(500), 
                       x='height', 
                       y='weight', 
                       z='ball_control',
                       color='age', 
                       hover_name='player',
                       opacity=0.7,
                       title="3D Analiz: Boy, Kilo ve Yetenek İlişkisi")

fig_3d.update_layout(template="plotly_dark")
fig_3d.show()