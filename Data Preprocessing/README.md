# 🧹 Veri Önişleme ve Veri Temizleme Uygulamaları (Data Preprocessing & Data Cleaning) 

Bu klasör, Veri Bilimi (Data Science) ve Makine Öğrenimi (Machine Learning) projelerinin en temel ve kritik adımı olan **Veri Önişleme (Data Preprocessing)** ve **Veri Temizleme (Data Cleaning)** süreçlerini adım adım anlatan Jupyter Notebook uygulamalarını içermektedir.

Sıfırdan başlayarak veri setlerindeki eksikliklerin nasıl giderileceği, aykırı değerlerin nasıl analiz edilip işleneceği gibi konular örneklerle ve popüler veri setleriyle uygulamalı olarak işlenmiştir. 

## 🧠 Temel Veri Önişleme Adımları Nelerdir?

Gerçek dünya verileri genellikle eksik, gürültülü veya tutarsızdır. Makine öğrenmesi modelleri algoritmalarla çalıştıkları için, verilen verinin kalitesi doğrudan modelin de kalitesini belirler ("Garbage In, Garbage Out"). Verinin işlenebilir ve kaliteli hale getirilmesi için başlıca 4 temel veri önişleme adımı uygulanır:

### 1. Veri Temizleme (Data Cleaning)
Verideki ölçüm hatalarını ve eksiklikleri gidermek için yapılan ilk müdahaledir.
- **Eksik Değerlerin Doldurulması:** Özellikle `diabetes.csv` gibi sağlık verilerinde $0$ olarak yanlış işaretlenmiş veya null bırakılan tıbbi verilerin (örneğin glikoz, kan basıncı) medyan, ortalama veya KNN gibi daha anlamlı uzaklık tabanlı yöntemlerle doldurulması işlemidir.
- **Gürültülü Veri (Noise) Giderme:** Doğru sanılan ama aslında bariz istatistiksel hatalar barındıran uç değerlerin (outliers) hatalı ölçüm olup olmadığına karar verilip ayıklanması veya baskılanmasıdır.
- **Tutarsızlıkların Giderilmesi:** Veri setinde aynı ifadeye karşılık gelen ama büyük/küçük harf, harf hatası vb. farklı yazılan girdilerin ("Diyabet", "diyabet", "Diabet") tek ve standart bir forma çevrilmesidir.

### 2. Veri Bütünleştirme (Data Integration)
Farklı ve dağınık veri kaynaklarından (veritabanları, Excel dosyaları) gelen verilerin ortak bir çatı altında bütünleştirilmesidir.
- **Veri Kaynağı Birleştirme:** Eğer hastanın kan tahlilleri laboratuvar tablosunda, kişisel demografik bilgileri hasta kayıt tablosunda duruyorsa, bu iki devasa tablo ortak bir anahtar/ID (`Hasta_ID`) üzerinden birbirine eklemlenir ve birleştirilir.
- **Varlık Çakışmalarını Çözme:** Çoğu zaman farklı kaynaktan gelen tablolarda aynı şeyi ifade eden sütunların adları farklıdır. Sistemlerin birinde "BP" (Blood Pressure) iken diğerinde "Kan_Basinci" yazıyor olabilir. Bu tür isimlendirme çakışmaları eşitlenerek harmanlanır.

### 3. Veri İndirgeme (Data Reduction)
Elde edilen büyük hacimli verinin kalitesini, yapısal desenini ve barındırdığı asıl bilgi özünü kaybetmeden boyut olarak çok daha kullanışlı bir küçüklüğe çekilmesidir.
- **Özellik Seçimi (Feature Selection):** Diyabeti veya ilgili hedefi tahmin etmede zerre kadar matematiksel katkısı / korelasyonu bulunmayan özellikleri (örneğin bir hastanın ID numarası veya sisteme kayıt sırası gibi) modelden çıkarma, temizleme işlemidir.
- **Örneklem Azaltma (Instance Reduction):** Milyonlarca satırdan oluşan verilerde birbirinin tamamen kopyası olan verileri çıkararak veya geniş evrenden sadece karakteristiği ifade eden dengeli bir örneklem (sampling) seçerek daha küçük boyutlu, hızlı bir sonuç alınmasını sağlar.
- **Boyut Küçültme (Dimensionality Reduction):** Değişken sayısının çok olduğu veri setlerinde PCA (Temel Bileşenler Analizi) gibi matematiksel metotlarla birçok sütunun, çok daha az sayıda ama daha fazla varyansı anlatan yeni bileşen matrislerine sıkıştırılmasıdır.

### 4. Veri Dönüştürme (Data Transformation)
Verinin algoritmanın ağırlık olarak daha iyi sindirebileceği, denge gözetilmiş kesin sınırlar içeren sayısal formatlara sokulması sürecidir.
- **Normalizasyon ve Ölçeklendirme (Scaling):** Makine öğrenimi farklı ölçeklerdeki sayılarda yanılgıya düşer. Bir özelliği 'yıllar' ile ifade edip 10-80 arasında sunarken, diğerini 'gelirler' ile ifade edip 10.000 - 100.000 arasında verirseniz; algoritma büyük sayıların çok daha önemli olduğu hatasına kapılır. Tüm sayısal verilerin 0-1 gibi belirli bir aralığa (Standart veya Min-Max kullanarak) sıkıştırılarak eşitlemektir.
- **Ayrıklaştırma (Discretization):** Sürekli uzayan sayısız detaydaki rakamsal / lineer veriyi anlamlı bölümlere ayırarak kategorik bir hal almasını sağlamaktır. (Örn: Hastanın tam olarak 48, 55, 62 yaşlarında olmasını tek tek hesaplamak yerine onları bir sınırla ayırarak "Genç", "Orta Yaş", "Yaşlı" sepetlerine koymaktır).
- **Özellik Oluşturma (Feature Engineering):** Hastalık ve hedef tahminleri açısından var olan değişkenlerden daha zengin ipuçları çıkarmayı sağlayan bir çeşit altın madenciliğidir. Örnek olarak bir diyabet tahmininde sadece kişinin glikozu ile değerlendirmek veya sadece Vücut Kitle Endeksine (BMI) bakmak yerine; bu iki risk faktörünü birbirleriyle doğrudan çarptığımız `Glucose * BMI` adında yeni çok bariz etki yaratan güçlü bir sütun üretmek gibi yaratıcı matematiksel dönüşümleri içerir.

## 📂 Klasör İçeriği ve Notebook'lar

### 1. `VeriTemizleme.ipynb` 
Veri temizleme teorisine ve temel uygulamalarına odaklanır:
- **Aykırı Değer (Outlier) Tespiti:** Çeyrekler Açıklığı (IQR) ve Z-Skor (Z-Score) yöntemleri ile aykırı değerlerin matematiksel olarak bulunması. Matplotlib ile Kutu Grafiği (Boxplot) görselleştirmesi.
- **Eksik Veri (Missing Data) Analizi:** Eksik verilerin mekanizmaları teorik ve pratik olarak incelenir. 
  - `MCAR` (Missing Completely At Random - Tamamen Rastgele Eksik Veri)
  - `MAR` (Missing At Random - Başka Değişkene Bağlı Rastgele Eksik Veri)
  - `MNAR` (Missing Not At Random - Kendi Değerine Bağlı Eksik Veri)
- **Eksik Veri Doldurma Yöntemleri (Imputation):** Geleneksel basit yöntemler (Ortalama (mean) ve Medyan atama), listwise/pairwise silme (dropna) ile Makine öğrenimi destekli uzaklık tabanlı doldurma (`KNNImputer`) ile eksik veriler doldurulur.
- **Gürültülü Veri:** Yanlış veya anormallik barındıran noisy verileri okuma.
- Kaggle'ın ünlü `Titanic` veri seti ve manuel simüle edilen öğrenci sınav tablosu ile uygulamalar.

### 2. `verionisleme01.ipynb`
Gerçek verilerle önişleme pratiği:
- **Diamonds Veri Seti:** Seaborn kütüphanesi üzerinden çekilen "diamonds" veri setinde Pandas kullanılarak veri analizi yapılır.
- Belirli özellikler (carat, table vb.) üzerindeki aykırı değerlerin matematiksel sınırlarının (Alt ve Üst Sınır) belirlenip tablo üzerinden filtrelenmesi, tespit edilmesi ve görsel olarak incelenmesi.

### 3. `veriönişleme02.ipynb`
Eksik veri analizinde ileri düzey yöntemler ve baskılama metodolojisi:
- **Planets Veri Seti:** Seaborn'daki "planets" astrofizik veri seti üzerinde DataFrame metodları ile boş (NaN/null) değer kontrolleri (`isnull().sum()`, `any()`).
- **Missingno Kütüphanesi:** Eksik verilerin büyük resimde görülmesi ve analizi için `missingno` kütüphanesi (Missing Data Visualization) ile grafiklileştirilmesi.
- **Baskılama Yöntemi (Clipping):** Ortaya çıkarılan aykırı değerleri silmek yerine, veriyi kaybetmemek adına sınır değerlere (alt_sinir/üst_sinir) çekerek veriyi optimize etme (`df.clip`) işlemi.

### 4. `veriönişleme03.ipynb`
Temizlenmiş verilerin makine öğrenmesi modellerinin anlayacağı sayısal veya algoritmik düzeye taşınması için gereken tamamlayıcı veri önişleme aşamalarını barındırır.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

Bu çalışmaları kendi ortamınızda doğru bir şekilde yürütebilmek için bilgisayarınızda şu Python kütüphanelerinin yüklü olması gerekmektedir:
- `pandas` - Veri manipülasyonu, tablo (DataFrame) işlemleri
- `numpy` - Matematiksel array ve matris operasyonları
- `matplotlib` & `seaborn` - İstatistiksel veri görselleştirme (Boxplot vb.)
- `scikit-learn` (`sklearn`) - Tahminsel eksik veri doldurma (`KNNImputer`)
- `missingno` - Eksik veri matrislerini grafikleştirme aracı

> **Not:** Kütüphaneleri kurmak için komut satırınıza aşağıdaki betiği yapıştırabilirsiniz:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn missingno jupyter
```

## 🚀 Çalıştırma

1. Python kurulu bir ortamda yukarıdaki bağımlılıkların makinenizde yüklü olduğundan emin olun.
2. Terminal yardımıyla bu README dosyasının bulunduğu ana dizine gidin.
3. Komut ekranından `jupyter notebook` veya `jupyter lab` yazıp editörünüzü başlatın.
4. Sırasıyla ilgili notebook'ları açarak hücreleri (Shift + Enter) çalıştırabilirsiniz. İyi çalışmalar!
