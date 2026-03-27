import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys

# 1. Veriyi yükle
try:
    df = pd.read_csv('player_stats.csv', encoding='latin-1')
    print("Veri yüklendi!")
except FileNotFoundError:
    print("HATA: Dosya bulunamadı!")
    sys.exit()

# --- KURS ADIMI: BOX PLOT (Kutu Grafiği) ---
# Kaan Can rehberinde gelir dağılımı veya puanları kıyaslamak için kullanılır.
# Biz: Farklı yaşlardaki oyuncuların 'ball_control' dağılımını görelim.
# (Sadece en çok oyuncu olan 4 yaşı seçelim ki grafik sade olsun)
top_ages = df['age'].value_counts().head(4).index
df_box = df[df['age'].isin(top_ages)]

fig_box = px.box(df_box, x="age", y="ball_control", 
             color="age", 
             points="all", # Tüm oyuncuları nokta olarak yanına ekler
             title="Yaş Gruplarına Göre Yetenek Dağılımı ve Aykırı Değerler")
fig_box.show()

# --- KURS ADIMI: WORD CLOUD (Kelime Bulutu) ---
# Rehberde ülkelerin isimlerini frekansına göre görselleştirir.
# Bu grafik için WordCloud kütüphanesi gerekir (pip install wordcloud)


# Ülkeleri bir metin haline getirelim
text = " ".join(df['nationality'].dropna())

wordcloud = WordCloud(width=800, height=400, 
                      background_color='white',
                      colormap='viridis').generate(text)

# WordCloud bir Plotly grafiği değildir, Matplotlib ile gösterilir
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Ülke Popülasyonu Kelime Bulutu')
plt.show()