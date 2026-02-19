# 📊 FIFA 23 Oyuncu Analizi — Matplotlib ile Radar Grafiği

Bu proje, Kaggle'dan alınan gerçek **FIFA 23** verilerini kullanarak futbolcu yeteneklerini analiz eden ve karşılaştıran bir Python uygulamasıdır. Görselleştirme katmanında **Matplotlib** ve **NumPy** ile oluşturulan profesyonel **Radar (Spider) Grafikleri** kullanılmaktadır.

---

## 🚀 Özellikler

- **Veri İşleme** — Pandas ile büyük ölçekli `player_stats.csv` dosyasının temizlenmesi ve filtrelenmesi
- **Hata Yönetimi** — UTF-8 / Latin-1 karakter kodlaması ve eksik `NaN` değerleri için otomatik çözümler
- **Radar Grafikleri** — Matplotlib polar eksen sistemi üzerinde dinamik Spider Chart üretimi
- **Akıllı Sütun Eşleştirme** — Veri setindeki sütun isimlerine göre kendini adapte eden esnek yapı
- **Çoklu Oyuncu Karşılaştırması** — Birden fazla oyuncuyu tek grafik üzerinde kıyaslama

---

## 🛠️ Kullanılan Teknolojiler

| Kütüphane | Versiyon | Kullanım Amacı |
|-----------|----------|----------------|
| Python | 3.10+ | Ana dil |
| Pandas | ≥ 1.5 | Veri okuma, filtreleme, temizleme |
| Matplotlib | ≥ 3.6 | Radar grafiği çizimi (polar eksen) |
| NumPy | ≥ 1.23 | Açısal hesaplamalar ve veri düzenleme |

---

## 📦 Kurulum

```bash
# 1. Repoyu klonlayın
git clone https://github.com/kullaniciadi/fifa23-radar-chart.git
cd fifa23-radar-chart

# 2. Sanal ortam oluşturun (önerilir)
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### `requirements.txt`

```
pandas>=1.5
matplotlib>=3.6
numpy>=1.23
```

---

## 📂 Proje Yapısı

```
fifa23-radar-chart/
│
├── data/
│   └── player_stats.csv        # Kaggle'dan indirilen ham veri seti
│
├── src/
│   ├── data_loader.py          # CSV okuma ve ön işleme
│   ├── radar_chart.py          # Matplotlib radar grafiği modülü
│   └── compare_players.py      # Oyuncu karşılaştırma arayüzü
│
├── outputs/
│   └── radar_output.png        # Üretilen grafik çıktısı
│
├── requirements.txt
└── README.md
```

---

## ▶️ Kullanım

```bash
python src/compare_players.py
```

Kod çalıştırıldığında istenen oyuncular seçilir ve aşağıdaki gibi bir radar grafiği üretilir:

![Radar Grafiği Örneği](image.png)

---

## 🎨 Matplotlib ile Radar Grafiği — Temel Mantık

Radar grafikleri, Matplotlib'in **polar (kutupsal) eksen** sistemi üzerine inşa edilir.

```python
import numpy as np
import matplotlib.pyplot as plt

kategoriler = ['Top Kontrolü', 'Dribbling', 'Savunma', 'Pas', 'Şut', 'Hız']
N = len(kategoriler)

# Açıları eşit aralıklarla dağıt, grafiği kapat
acılar = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
acılar += acılar[:1]   # başlangıç noktasına dön (kapalı çokgen)

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

def radar_ciz(degerler, renk, etiket):
    degerler = degerler + degerler[:1]
    ax.plot(acılar, degerler, color=renk, linewidth=2, label=etiket)
    ax.fill(acılar, degerler, color=renk, alpha=0.2)

# Oyuncu verileri (0–100 ölçeği)
radar_ciz([85, 90, 40, 78, 88, 95], '#1f77b4', 'Oyuncu A')
radar_ciz([70, 65, 80, 85, 72, 60], '#ff7f0e', 'Oyuncu B')

ax.set_thetagrids(np.degrees(acılar[:-1]), kategoriler, fontsize=11)
ax.set_ylim(0, 100)
ax.set_title('Oyuncu Karşılaştırması', size=15, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.savefig('outputs/radar_output.png', dpi=150)
plt.show()
```

### Kritik Noktalar

- `subplot_kw=dict(polar=True)` → eksenin kutupsal olmasını sağlar
- `np.linspace(0, 2π, N, endpoint=False)` → kategorileri daireye eşit dağıtır
- Liste sonuna başlangıç değeri eklenmesi (`values[:1]`) → çokgeni kapatır
- `ax.fill()` + `alpha` → yarı saydam alan dolgusu üretir

---

## 📊 Veri Seti

Veri seti **Kaggle — FIFA 23 Complete Player Dataset** kaynağından alınmıştır.

Kullanılan başlıca sütunlar:

| Sütun Adı | Açıklama |
|-----------|----------|
| `short_name` | Oyuncu kısa adı |
| `pace` | Hız puanı (0–100) |
| `shooting` | Şut puanı |
| `passing` | Pas puanı |
| `dribbling` | Dribbling puanı |
| `defending` | Savunma puanı |
| `physic` | Fiziksel güç puanı |




![alt text](image.png)
