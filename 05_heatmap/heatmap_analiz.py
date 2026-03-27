import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    # 'latin-1' özel karakterleri (é, ñ, ş gibi) okumak için en sağlam yoldur
    df = pd.read_csv('player_stats.csv', encoding='latin-1')

    # Sadece sayısal sütunları seç
    sayisal_df = df.select_dtypes(include=['float64', 'int64'])

    # Korelasyonu hesapla
    corr = sayisal_df.corr()

    # Heatmap çizdir
    plt.figure(figsize=(15, 10))
    sns.heatmap(corr, annot=False, cmap='coolwarm', linewidths=0.2)
    plt.title("FIFA 24: Ozellikler Arasi Baglanti Haritasi")
    plt.show()

except Exception as e:
    print(f"Bir hata olustu: {e}")