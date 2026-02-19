Bu depo, modern veri bilimi araçlarını kullanarak futbol dünyasından anlamlı içgörüler çıkarma yolculuğumu içermektedir. Proje, statik istatistiksel analizlerden interaktif kullanıcı deneyimine kadar geniş bir yelpazeyi kapsar.

🚀 Proje Genel Bakış
Kaggle üzerinden alınan FIFA 23 veri seti üzerinde çalışılarak, oyuncu yetenekleri ve fiziksel parametreler arasındaki ilişkiler üç farklı boyutta incelenmiştir:

Teknik Kıyaslama (Matplotlib)

İstatistiksel İlişkiler (Seaborn)

İnteraktif Deneyim (Plotly)

Teknik Araç Çantası (Toolkit)
Pandas: Veri manipülasyonu ve büyük veri setlerinin yönetimi.

Matplotlib: Özelleştirilmiş radar grafikleri ile detaylı yetenek analizi.

Seaborn: Korelasyon ısı haritaları ile veri madenciliği.

Plotly: Tarayıcı tabanlı, interaktif "Point & Hover" grafikler.

📊 Analiz Detayları
1. Yetenek Karşılaştırma (Radar Chart)
analiz.py dosyası ile oluşturulan bu grafik, iki oyuncuyu (Örn: Messi vs Ronaldo) kafa kafaya getirir. Oyuncuların savunma, hücum ve fiziksel kapasitelerini poligonlar üzerinde üst üste bindirerek farkları net bir şekilde ortaya koyar.

2. İstatistiksel Derinlik (Seaborn Heatmap)
analiz_seaborn.py ile verideki 19.000+ oyuncunun özellikleri taranmıştır.

Bulgu: ball_control ve dribbling arasındaki 0.95 korelasyon, teknik gelişimin ayrılmaz bir bütün olduğunu kanıtlar.

3. İnteraktif Karşılaştırma (Plotly Radar)
analiz_plotly.py ile oluşturulan interaktif grafik, kullanıcının veri noktalarıyla etkileşime girmesini sağlar.
  Özellik: Oluşturulan oyuncu_kiyaslama.html dosyası herhangi bir tarayıcıda açılabilir ve noktaların üzerine gelindiğinde anlık veriler görüntülenebilir.

  ![alt text](image.png)