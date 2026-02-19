# 📊 Veri Görselleştirme Rehberi

> Ham veriyi; yaşayan, nefes alan ve stratejik karar destek mekanizmalarına dönüştüren dört katmanlı veri bilimi çalışması.

---

## 🗂️ İçindekiler

- [Storytelling with Data](#-1-storytelling-with-data)
- [İnteraktif Dashboard](#-2-i̇nteraktif-dashboard)
- [Gerçek Zamanlı Görselleştirme](#-3-gerçek-zamanlı-görselleştirme)
- [Büyük Veri Görselleştirme](#-4-büyük-veri-görselleştirme)

---

## 📖 1. Storytelling with Data

Veri hikaye anlatımı, rakamları insanların anlayabileceği ve harekete geçebileceği anlamlı bir anlatıya dönüştürme sanatıdır. Sadece "doğru grafik çizmek" değil, **"doğru mesajı iletmek"** üzerine kuruludur.

> 💡 **Temel İlke:** İzleyici verinizi görmez — hikayenizi duyar. Bu yüzden her görselleştirmenin bir sorusu, bir çatışması ve bir sonucu olmalıdır.

### Zayıf vs Güçlü Yaklaşım

| Yaklaşım | ❌ Zayıf | ✅ Güçlü |
|----------|---------|---------|
| **Başlık** | "Yaş Dağılımı" | "25 Yaş Altı Oyuncular Golün %67'sini Atıyor" |
| **Grafik Notu** | "Pas başarı oranları gösteriliyor" | "60. dakikadan sonra pas başarısı %78'den %61'e düşüyor" |
| **Renk Kullanımı** | Tüm çubuklar aynı renk | Kritik çubuk kırmızı, diğerleri gri |

### 4 Temel İlke

**1. Veri-Mürekkep Oranı**
Her piksel bir bilgi taşımalıdır. Gereksiz ızgara çizgilerini, süs öğelerini ve fazladan rengi kaldırın. Grafiğin hiçbir öğesi bilgi iletmiyorsa, o öğe gürültüdür.

**2. Tek Vurgu Noktası**
Dikkat çekilmek istenen tek öğeyi kırmızıyla işaretle, geri kalanı griyle bırak. İzleyicinin gözü doğrudan o noktaya gider. İki şeyi vurgulamak, hiçbirini vurgulamamaktır.

**3. Sonucu Başlığa Taşı**
"Yaş Dağılımı" başlık değildir, etiket seviyesindedir. İzleyicinin sonucu kendisi bulmasını bekleme. Başlık zaten sonucu söylemeli, grafik onu kanıtlamalıdır.

**4. Hikaye Yapısı: Soru → Çatışma → Çözüm**
"Takım bu sezon neden kazanamadı?" → "60. dakikadan sonra pas başarısı dramatik düşüyor" → "Kondisyon yatırımı gerekli." Her grafik bu üç aşamayı taşımalıdır.

### Grafik Türü Seçim Rehberi

| Grafik Türü | Ne Zaman Kullan | Kaçınma Kriteri |
|-------------|----------------|-----------------|
| **Pasta Grafik** | Parçanın bütüne oranı | 6+ dilim → bar grafiğe geç |
| **Çizgi Grafik** | Zaman serisi, trend | Kategorik veriler için kullanma |
| **Scatter Plot** | İki değişken arası ilişki | 1000+ nokta → alpha blending ekle |
| **Heatmap** | Matris ilişkileri, korelasyon | Renk körü erişimi için dikkatli palet seç |
| **3D Grafik** | Neredeyse hiçbir zaman | Perspektif değerleri bozar, 2D kullan |

---

## 🎛️ 2. İnteraktif Dashboard

Statik raporun evrimidir. Kullanıcı artık sadece okuyucu değil, **araştırmacıdır.** Bir filtre değiştirdiğinde veri ona anında cevap verir.

> ⚠️ **Kritik Tasarım Hatası:** Tek ekrana 15 grafik sıkıştırmak. Bir dashboard'un tek soruyu mükemmel yanıtlaması, on soruyu yarım yanıtlamasından çok daha değerlidir.

### Üç Katmanlı Tasarım

```
┌──────────────────────────────────────────────┐
│  [KPI]  Toplam Oyuncu │ Ort. Overall │ Ort. Hız │  ← Tek bakışta durum
├──────────────────────────────────────────────┤
│                                              │
│          [Ana Grafik — Scatter / Bar]        │  ← Trend ve örüntü
│                                              │
├──────────────────────────────────────────────┤
│      [Drill-Down Tablo — Filtrelenmiş]       │  ← Ham veriye erişim
└──────────────────────────────────────────────┘
```

### Araç Karşılaştırması

| Araç | Kullanım Amacı | Güçlü Yön | Sınır |
|------|---------------|-----------|-------|
| **Streamlit** | Hızlı prototip | Birkaç satır Python = çalışan app | Üretim ölçeğinde kısıtlı |
| **Plotly Dash** | Kurumsal üretim | React tabanlı, tam callback kontrolü | Öğrenme eğrisi dik |
| **Power BI** | İş analitiği | Kod yazmadan görsel arayüz | Özelleştirme sınırlı, ücretli |
| **Tableau** | Veri keşfi | Drag & drop, hızlı görsel | Pahalı, Python entegrasyonu zor |

### Streamlit — Temel Yapı

```python
import streamlit as st
import plotly.express as px

# Sidebar filtreleri
yas     = st.slider("Yaş Aralığı", 16, 45, (20, 28))
overall = st.slider("Min. Overall", 60, 99, 75)

# KPI kartları
c1, c2, c3 = st.columns(3)
c1.metric("Toplam Oyuncu", len(filtreli))
c2.metric("Ort. Overall",  f"{filtreli['overall'].mean():.1f}")
c3.metric("Ort. Hız",      f"{filtreli['pace'].mean():.1f}")

# Ana grafik + drill-down tablo
st.plotly_chart(px.scatter(filtreli, x='pace', y='shooting'))
st.dataframe(filtreli.sort_values('overall', ascending=False))
```

---

## ⚡ 3. Gerçek Zamanlı Görselleştirme

Geleneksel görselleştirme **"ne oldu?"** sorusunu yanıtlarken, gerçek zamanlı sistemler **"şu an ne oluyor?"** sorusunu yanıtlar. Teknik ekip kararını maç bitmeden verebilir.

### Sistem Mimarisi

```
YOLOv8  →  JSON Stream  →  WebSocket  →  st.empty()  →  Canlı Grafik
(Kaynak)   (Koordinat)    (Transport)    (Render)       (Çıktı)
```

### Üç Temel Bileşen

**Veri Kaynağı**
Sensörler, kameralar, API'lar, IoT cihazları. YOLOv8 ile video karelerinden oyuncu koordinatları milisaniyeler içinde çıkarılır.

**Transport Katmanı — WebSocket**
Kalıcı bağlantı, çift yönlü, düşük gecikme. HTTP'nin aksine her mesaj için yeni bağlantı açmaz; kanal sürekli açık kalır.

**Render Katmanı — `st.empty()`**
Streamlit'te bir placeholder tanımlanır ve gelen her veri paketiyle grafik yerinde yeniden çizilir. Sayfa yenilenmez.

### WebSocket Sunucu — ~30 FPS

```python
import asyncio, websockets, json

async def canli_gonder(websocket):
    for satir in koordinat_df.itertuples():
        await websocket.send(json.dumps({
            'track_id': satir.track_id,
            'x': satir.x,
            'y': satir.y
        }))
        await asyncio.sleep(0.033)   # 30 FPS

async def main():
    async with websockets.serve(canli_gonder, 'localhost', 8765):
        await asyncio.Future()

asyncio.run(main())
```

> ⚠️ **Gecikme Yönetimi:** Veri 100ms'de geliyorsa grafik 100ms'de güncellenmeli. Aksi halde **backpressure** birikir ve sistem çöker. Her kare yerine belirli aralıklarla güncelleme (throttling) üretim standardıdır.

> ⚠️ **Bellek Sızıntısı:** Pozisyon geçmişi sürekli büyümemeli. Yalnızca son N kare tutulmalıdır. Sınırsız büyüyen listeler kaçınılmaz çökmelere yol açar.

---

## 🌐 4. Büyük Veri Görselleştirme

Milyonlarca nokta aynı grafikte çizildiğinde tüm noktalar üst üste biner, tek renkli bir lekeye dönüşür ve hiçbir bilgi iletilemez. Bu soruna **overplotting** denir.

### Kademeli Çözüm Rehberi

| Veri Boyutu | Yöntem | Araç | Nasıl Çalışır? |
|-------------|--------|------|----------------|
| < 100K | Doğrudan Çizim | Matplotlib / Plotly | Tüm noktalar çizilir, sorun yok |
| 100K – 500K | Alpha Blending | Matplotlib | Saydamlık ile yoğunluk görünür hale gelir |
| 500K – 2M | Hexbinning | Matplotlib | Altıgen hücre → nokta sayısı → renk yoğunluğu |
| 2M – 1B | Datashader | Datashader | GPU destekli piksel düzeyinde render |
| 1B+ | Lazy Evaluation | Vaex | RAM'e hiç yüklemeden işler |
| Tüm Ölçekler | Parquet Formatı | Pandas / Vaex | CSV'den 5–10x daha hızlı okuma |

### Alpha Blending

```python
# 100K – 500K nokta için
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(df['x'], df['y'],
           alpha=0.03,   # Çakışan bölgeler doğal olarak koyulaşır
           s=1,
           color='#00BFFF')
ax.set_facecolor('#0a0a2e')
plt.savefig('outputs/alpha_blend.png', dpi=150)
```

### Hexbinning

```python
# 500K – 2M nokta için
fig, ax = plt.subplots(figsize=(12, 8))
hb = ax.hexbin(df['x'], df['y'],
               gridsize=40,       # Hücre sıklığı
               cmap='YlOrRd',     # Sarı (az) → Kırmızı (çok)
               mincnt=1)
plt.colorbar(hb, label='Yoğunluk')
plt.savefig('outputs/hexbin.png', dpi=150)
```

### Datashader — GPU Destekli

```python
# 2M – 1B nokta için
import datashader as ds
import datashader.transfer_functions as tf
from colorcet import fire

cvs     = ds.Canvas(plot_width=1200, plot_height=800,
                    x_range=(0, 105), y_range=(0, 68))
agregat = cvs.points(df, 'x', 'y', ds.count())
gorsel  = tf.shade(agregat, cmap=fire, how='log')
tf.set_background(gorsel, 'black').to_pil().save('outputs/density.png')
```

### Vaex — RAM Olmadan 4 Milyon Satır

```python
# 1B+ kayıt için
import vaex

df = vaex.open('data/match_events.parquet')  # RAM'e yüklemez
print(f"Toplam kayıt: {len(df):,}")          # → 4.200.000

# Lazy evaluation — sonuç istenene kadar hesaplanmaz
ozet = df[df.event_type == 'pass'].groupby('team_id', agg={
    'pas_sayisi': vaex.agg.count(),
    'basari':     vaex.agg.mean('pass_success')
})
print(ozet.to_pandas_df())
```

### Format Karşılaştırması

| Format | Okuma Hızı | Disk Boyutu | İnsan Okunabilir |
|--------|-----------|-------------|------------------|
| **CSV** | ~12 sn / 100MB | Büyük | ✅ Evet |
| **Parquet** | ~1.2 sn / 100MB | %60–80 küçük | ❌ Hayır |
| **Feather** | ~0.8 sn / 100MB | Orta | ❌ Hayır |

> 💡 **Altın Kural:** Büyük veri projesine CSV ile başlamak, yarış yarım kala pit stop yapmak gibidir. İlk adımda CSV'yi Parquet'e dönüştür — geri kalan her adım 10x daha hızlı çalışır.

---

## 🛠️ Teknoloji Yığını

| Katman | Araçlar |
|--------|---------|
| Veri İşleme | Pandas, NumPy, Vaex |
| Statik Görsel | Matplotlib, Seaborn |
| İnteraktif | Plotly, Streamlit, Dash |
| Gerçek Zamanlı | YOLOv8, WebSocket, OpenCV |
| Büyük Veri | Datashader, Parquet |

