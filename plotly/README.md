# ⚽ FIFA 23 İnteraktif Veri Analizi ve Görselleştirme Portfolyosu

Bu proje, **FIFA 23** oyuncu verilerini kullanarak **Plotly** kütüphanesi ile modern, interaktif ve profesyonel veri görselleştirme tekniklerini sergilemektedir. Proje, temel grafiklerden başlayarak ileri seviye 3D analizlere ve kapsamlı dashboard tasarımlarına kadar 5 ana bölümden oluşmaktadır.

---

## 📊 Proje İçeriği ve Bölümler

### 01. Temel Analizler (Radar, Line, Scatter)
Bu bölümde oyuncuların teknik yetenekleri karşılaştırılmış ve zaman içindeki gelişim trendleri incelenmiştir.
- **Radar Analizi**: Oyuncuların teknik kapasitelerinin (Ball Control, Dribbling, vb.) örümcek ağ grafiği ile kıyaslanması.
- **Trend Analizi**: Yetenek puanlarının oyuncu bazlı değişimleri.

| Örnek Görseller |
| :---: |
| ![Radar Analizi](01_Temel_Analizler/Ekran%20görüntüsü%202026-02-20%20155714.png) |
| ![Line Analizi](01_Temel_Analizler/Ekran%20görüntüsü%202026-02-20%20155740.png) |
| ![Scatter Analizi](01_Temel_Analizler/Ekran%20görüntüsü%202026-02-20%20155805.png) |

---

### 02. Doğrulama ve Dağılım (Bubble, Histogram)
İstatistiksel dağılımların ve değişkenler arası ilişkilerin daha derinlemesine incelendiği bölümdür.
- **Bubble Chart**: Boy, kilo ve yetenek arasındaki üç boyutlu ilişkinin 2D düzlemde gösterimi.
- **Histogram**: Oyuncu yaş dağılımı ve frekans analizi.

| Örnek Görseller |
| :---: |
| ![Bubble Chart](02_Dogrulama_ve_Dagilim/Ekran%20görüntüsü%202026-02-20%20160053.png) |
| ![Histogram](02_Dogrulama_ve_Dagilim/Ekran%20görüntüsü%202026-02-20%20160116.png) |

---

### 03. İstatistiksel Görselleştirme (Box Plot & Word Cloud)
Veri setindeki aykırı değerlerin (outliers) tespiti ve metin tabanlı verilerin görselleştirilmesi sağlanmıştır.
- **Box Plot**: Yaş gruplarına göre yetenek puanlarının standart sapma ve kartil analizi.
- **Word Cloud**: Veri setindeki ülke popülasyonlarının görsel frekans haritası.

| Örnek Görseller |
| :---: |
| ![Box Plot](03_Istatistiksel_Gorsellestirme/Ekran%20görüntüsü%202026-02-20%20160410.png) |
| ![Word Cloud](03_Istatistiksel_Gorsellestirme/Ekran%20görüntüsü%202026-02-20%20160428.png) |

---

### 04. İleri Seviye Analizler (3D & Harita)
Mekansal ve üç boyutlu verilerin analiz edildiği, projenin en etkileyici bölümlerinden biridir.
- **3D Scatter**: Boy, Kilo ve Yetenek parametrelerinin 3 boyutlu uzayda interaktif analizi.
- **Choropleth Harita**: Dünya üzerindeki oyuncu dağılım yoğunluğunun coğrafi gösterimi.

| Örnek Görseller |
| :---: |
| ![3D Analiz](04_Ileri_Seviye_Analizler/Ekran%20görüntüsü%202026-02-20%20160753.png) |
| ![Dünya Haritası](04_Ileri_Seviye_Analizler/Ekran%20görüntüsü%202026-02-20%20160919.png) |

---

### 05. Master Dashboard
Tüm analizlerin bir araya getirildiği, yönetici özeti niteliğindeki final raporu tasarımıdır.
- **Subplots**: Tek ekranda Bar, Pie, Harita ve 3D grafiklerin senkronize sunumu.

| Final Dashboard Çıktısı |
| :---: |
| ![Master Dashboard](05_Master_Dashboard/Ekran%20görüntüsü%202026-02-20%20161130.png) |

---

## 🛠️ Teknik Altyapı ve Kurulum

Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

### 📦 Gerekli Kütüphaneler
- `pandas`: Veri manipülasyonu
- `plotly`: İnteraktif grafikler
- `wordcloud`: Kelime bulutu oluşturma
- `matplotlib`: Statik görselleştirme destekçisi

### 🚀 Çalıştırma
```bash
# Bağımlılıkları yükleyin
pip install pandas plotly wordcloud matplotlib

# İlgili bölümlerdeki Python dosyalarını çalıştırın (Örn: Bölüm 5)
python 05_Master_Dashboard/final_football_dashboard.py
```

---

## 💎 Neden Bu Proje?
Bu çalışma, sadece veri görselleştirme değil, aynı zamanda ham veriden anlamlı hikayeler çıkarma yeteneğini temsil eder. **Plotly** sayesinde statik görsellerin aksine:
- **Etkileşim**: Kullanıcı grafiklerle konuşabilir, zoom yapabilir ve odak noktasını seçebilir.
- **Profesyonellik**: HTML tabanlı çıktılar sayesinde herhangi bir yazılım kurulumuna gerek kalmadan sunumlar yapılabilir.
- **Derinlik**: 3D ve Harita analizleri ile standart grafiklerin ötesine geçilir.

---
*Hazırlayan: Hilmi Kılavuz / KARAYERİN OLSUN*
