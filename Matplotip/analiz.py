import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Veriyi yükle
df = pd.read_csv('player_stats.csv', encoding='latin-1', low_memory=False)
print("Veri başarıyla yüklendi!")

# 2. Sütun İsimlerini Ayarla (Senin terminal çıktına göre)
name_col = 'player'

# Radar grafiğinde göstermek istediğimiz yetenekler
# Terminal çıktındaki mevcut sütunlara göre bir liste oluşturdum:
attributes = ['ball_control', 'dribbling', 'marking', 'slide_tackle', 'age'] 

# Not: Eğer 'pace', 'shooting' gibi sütunlar dosyanın ilerleyen kısımlarında varsa 
# listeye onları da ekleyebilirsin.

# 3. Oyuncuları Seç (Verideki isimlerin tam halini bulalım)
# Messi ve Ronaldo'nun senin verinde nasıl yazıldığını kontrol ediyoruz
print("\nVerideki bazı oyuncu isimleri:")
print(df[name_col].head(10).tolist())

# Örnek isimleri senin verine göre güncelleyebilirsin
# Şimdilik en yüksek ball_control değerine sahip 2 oyuncuyu otomatik seçelim
data = df.nlargest(2, 'ball_control')[[name_col] + attributes]
print(f"\nKarşılaştırılan Oyuncular: {data[name_col].tolist()}")

# 4. Radar Grafiği Oluşturma
labels = np.array(attributes)
num_vars = len(labels)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i, row in data.iterrows():
    values = row[attributes].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, label=row[name_col])
    ax.fill(angles, values, alpha=0.25)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)

# Değer aralığını verine göre ayarla (Örn: Yetenekler 0-100 arasıysa)
ax.set_ylim(0, 100) 

plt.title('Oyuncu Yetenek Karşılaştırması', y=1.1, size=15)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.show()