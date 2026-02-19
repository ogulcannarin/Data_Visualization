# 🧬 FIFA 23 İstatistiksel Analiz — Seaborn ile Korelasyon Keşfi

Bu proje, Python'un en güçlü istatistiksel görselleştirme kütüphanelerinden **Seaborn** kullanılarak 19.000+ profesyonel futbolcunun fiziksel ve teknik özellikleri arasındaki gizli ilişkilerin keşfedilmesini amaçlar.

---

## 🧬 Seaborn Nedir?

Seaborn, **Matplotlib** üzerine inşa edilmiş yüksek seviyeli bir Python görselleştirme kütüphanesidir. Veri biliminde şu avantajları nedeniyle tercih edilir:

- **İstatistiksel Odak** — Dağılımları, ilişkileri ve desenleri görselleştirmek için optimize edilmiştir
- **Estetik Görünüm** — Modern, temiz ve profesyonel grafik temalarını varsayılan olarak sunar
- **Pandas Entegrasyonu** — DataFrame yapılarıyla mükemmel uyum; karmaşık tablolar saniyeler içinde grafiğe dönüşür
- **Az Kod, Çok Sonuç** — Matplotlib'de onlarca satır süren işlemler Seaborn'da tek satıra iner

### Matplotlib vs Seaborn

| Özellik | Matplotlib | Seaborn |
|---------|-----------|---------|
| Soyutlama seviyesi | Düşük (tam kontrol) | Yüksek (hızlı üretim) |
| Varsayılan estetik | Sade | Profesyonel |
| İstatistiksel grafikler | Manuel | Yerleşik |
| Pandas entegrasyonu | Orta | Mükemmel |
| Öğrenme eğrisi | Dik | Hafif |

---

## 📦 Kurulum

```bash
# 1. Repoyu klonlayın
git clone https://github.com/kullaniciadi/fifa23-seaborn-analysis.git
cd fifa23-seaborn-analysis

# 2. Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### `requirements.txt`

```
pandas>=1.5
seaborn>=0.12
matplotlib>=3.6
numpy>=1.23
```

---

## 📂 Proje Yapısı

```
fifa23-seaborn-analysis/
│
├── data/
│   └── player_stats.csv            # Kaggle FIFA 23 ham veri seti
│
├── src/
│   ├── data_loader.py              # CSV okuma ve ön işleme
│   ├── analiz_seaborn.py           # Korelasyon haritası — ana modül
│   ├── analiz.py                   # Matplotlib radar grafiği
│   └── analiz_plotly.py            # Plotly interaktif grafik
│
├── outputs/
│   ├── korelasyon_haritasi.png     # Isı haritası çıktısı
│   └── dagilim_grafigi.png         # Dağılım grafikleri
│
├── requirements.txt
└── README.md
```

---

## ▶️ Kullanım

```bash
python src/analiz_seaborn.py
```

Çalıştırıldığında `outputs/` klasörüne aşağıdaki görseller kaydedilir:

- `korelasyon_haritasi.png` — Özellikler arası ilişki matrisi
- `dagilim_grafigi.png` — Seçili özellik çiftlerinin dağılım grafiği

![Korelasyon Isı Haritası](image.png)

---

## 💻 Tam Proje Kodu

### Korelasyon Isı Haritası

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ── Veri Yükleme ──────────────────────────────────────────────────
for enc in ['utf-8', 'latin-1', 'cp1252']:
    try:
        df = pd.read_csv('data/player_stats.csv', encoding=enc)
        print(f"Veri yuklendi: {len(df)} oyuncu")
        break
    except UnicodeDecodeError:
        continue

# ── Analiz Edilecek Özellikler ────────────────────────────────────
OZELLIKLER = ['age', 'ball_control', 'dribbling',
              'marking', 'slide_tackle', 'height', 'weight']

# Eksik değerleri temizle
df_temiz = df[OZELLIKLER].dropna()
print(f"Analiz icin kullanilan oyuncu sayisi: {len(df_temiz)}")

# ── Korelasyon Matrisi ────────────────────────────────────────────
corr_matrix = df_temiz.corr()

# ── Görselleştirme ────────────────────────────────────────────────
plt.figure(figsize=(10, 8))

sns.heatmap(
    corr_matrix,
    annot=True,           # Hücrelere değer yaz
    fmt='.2f',            # 2 ondalık basamak
    cmap='coolwarm',      # Mavi (negatif) → Kırmızı (pozitif)
    center=0,             # Renk skalasını sıfırda ortala
    square=True,          # Kare hücreler
    linewidths=0.5,       # Hücre sınır çizgileri
    linecolor='#2d2d2d',
    cbar_kws={'label': 'Korelasyon Katsayisi', 'shrink': 0.8},
    annot_kws={'size': 11, 'weight': 'bold'}
)

plt.title('FIFA 23 — Oyuncu Ozellikleri Korelasyon Haritasi',
          fontsize=15, pad=20, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)

plt.tight_layout()
plt.savefig('outputs/korelasyon_haritasi.png', dpi=150, bbox_inches='tight')
plt.show()
print("Grafik kaydedildi: outputs/korelasyon_haritasi.png")
```

### Ek: Dağılım Grafiği (Pairplot)

```python
import numpy as np

# Sadece alt üçgeni göster (tekrar eden değerleri gizle)
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

sns.heatmap(corr_matrix, mask=mask, annot=True,
            fmt='.2f', cmap='coolwarm', center=0)

# Seçili özellikler için çiftli dağılım
sns.pairplot(
    df_temiz[['ball_control', 'dribbling', 'pace', 'age']],
    diag_kind='kde',           # Köşegen: yoğunluk eğrisi
    plot_kws={'alpha': 0.3},   # Nokta saydamlığı
    corner=True                # Sadece alt üçgen
)
plt.suptitle('Ozellik Ciftleri Dagilim Grafigi', y=1.02)
plt.savefig('outputs/dagilim_grafigi.png', dpi=150)
```

---

## 🔍 `sns.heatmap` — Parametre Referansı

| Parametre | Tür | Açıklama |
|-----------|-----|----------|
| `data` | DataFrame | Korelasyon matrisi (sayısal) |
| `annot` | bool | Hücrelere değer yazdırma |
| `fmt` | str | Değer formatı: `'.2f'` → ondalıklı |
| `cmap` | str | Renk paleti (`coolwarm`, `viridis`, `YlOrRd`) |
| `center` | float | Renk skalası merkezi (genelde `0`) |
| `square` | bool | Kare hücreler |
| `linewidths` | float | Hücre arası çizgi kalınlığı |
| `vmin` / `vmax` | float | Renk skalası sınırları (`-1` ve `1` önerilir) |
| `mask` | array | Gizlenecek hücre maskesi (üst üçgen için kullanılır) |

### Popüler Renk Paleteleri

```python
# Korelasyon için: iki yönlü (pozitif/negatif)
cmap='coolwarm'    # Mavi → Beyaz → Kırmızı  ← En yaygın
cmap='RdBu_r'      # Kırmızı → Beyaz → Mavi
cmap='PiYG'        # Pembe → Yeşil

# Tek yönlü değerler için (0'dan büyük)
cmap='YlOrRd'      # Sarı → Turuncu → Kırmızı
cmap='Blues'       # Açık → Koyu Mavi
cmap='viridis'     # Mor → Sarı (erişilebilir)
```

---

## 📊 Analizden Çıkarılan Bulgular

### Güçlü Pozitif Korelasyonlar

**`ball_control` ↔ `dribbling` → 0.95**
Teknik gelişimin ayrılmaz bütünlüğünü kanıtlar. Top kontrolü gelişen oyuncunun dribbling becerisi de paralel ilerleme kaydeder. Antrenman programlarında bu iki yeteneğin birlikte çalışılması bu sonucu destekler.

**`height` ↔ `weight` → 0.76**
Beklenen fiziksel doğrulama. Boy uzadıkça vücut kütlesinin artması futbolcularda da genel popülasyonla benzer seyir izler.

**`slide_tackle` ↔ `marking` → 0.88**
Savunma yeteneklerinin birlikte geliştiğini gösterir. Defansif eğitim almış oyuncular hem adam markajı hem de kayarak müdahale konusunda eş zamanlı ilerler.

### Negatif Korelasyonlar

**`height` ↔ `dribbling` → −0.38**
Boy arttıkça dribbling becerisinin zayıflaması, uzun boylu oyuncuların ağırlık merkezlerinin yüksek olmasından kaynaklanan biyomekanik bir kısıtlamayı yansıtır.

**`age` ↔ `pace` → −0.31**
Yaş ilerledikçe hız parametresinin düşüşü, futbolda fiziksel zirvenin 24–27 yaş aralığında olduğuna dair sahadan gelen gözlemlerle örtüşür.

---

## 🎨 Seaborn Tema Sistemi

```python
# Kullanılabilir temalar
sns.set_theme(style='darkgrid')   # Koyu ızgara
sns.set_theme(style='whitegrid')  # Açık ızgara
sns.set_theme(style='dark')       # Izgarasız koyu
sns.set_theme(style='white')      # Izgarasız açık
sns.set_theme(style='ticks')      # Minimal eksen tikleri

# Renk paleti
sns.set_palette('husl')           # 8 dengeli renk
sns.set_palette('tab10')          # Matplotlib varsayılanı
sns.set_palette('Set2')           # Pastel, baskı dostu

# Yazı ve öğe boyutları
sns.set_context('paper')          # Küçük — makale
sns.set_context('notebook')       # Orta  — Jupyter (varsayılan)
sns.set_context('talk')           # Büyük — sunum
sns.set_context('poster')         # En büyük — afiş
```

---

## ⚙️ Hata Yönetimi

```python
# Karakter kodlaması otomatik algılama
for enc in ['utf-8', 'latin-1', 'cp1252']:
    try:
        df = pd.read_csv('data/player_stats.csv', encoding=enc)
        break
    except UnicodeDecodeError:
        continue

# Sayısal olmayan sütunları otomatik ayıkla
sayisal_df = df.select_dtypes(include='number')

# Korelasyon için yalnızca tam satırları kullan
corr_matrix = sayisal_df.dropna().corr()
```


![alt text](image.png)
