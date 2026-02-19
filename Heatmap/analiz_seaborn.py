import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Veriyi yükle
df = pd.read_csv('player_stats.csv', encoding='latin-1', low_memory=False)

# 2. Analiz etmek istediğimiz özellikleri seçelim
# Veri setinde var olduğunu bildiğimiz sütunları kullanıyoruz
cols_to_analyze = ['age', 'ball_control', 'dribbling', 'marking', 'slide_tackle', 'height', 'weight']

# Seçtiğimiz sütunlardaki korelasyonu (ilişkiyi) hesapla
# 1'e yakın değerler güçlü pozitif ilişki, -1'e yakınlar negatif ilişki demektir.
corr_matrix = df[cols_to_analyze].corr()

# 3. Görselleştirme
plt.figure(figsize=(10, 8))

# Seaborn Isı Haritası (Heatmap)
# annot=True: Karelerin içine sayıları yazar
# cmap='coolwarm': Renk paleti (Mavi: düşük, Kırmızı: yüksek ilişki)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

plt.title('Futbolcu Özellikleri Arasındaki İlişki Analizi (Seaborn)')
plt.show()