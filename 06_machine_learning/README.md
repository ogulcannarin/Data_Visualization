# 🤖 Makine Öğrenmesi (Machine Learning) Algoritmaları

Bu dizin, temel makine öğrenmesi algoritmalarının hem klasik (tablo) hem de yapılandırılmamış (görüntü) veriler üzerinde nasıl uygulanacağını gösteren çalışma proje dosyalarını barındırır. Her algoritma kendi klasöründe izole edilmiş verisetleri ve dosyalarla çalışmaktadır.

---

## 📂 İçindekiler ve Modeller

### 1. Karar Ağaçları (`01_karar_agaclari`)
Karar Ağaçları (Decision Trees), veriyi belirli kurallara ve sorulara göre dallandırarak sınıflandırma yapan popüler bir algoritmadır.

*   **Proje:** X-Ray/Röntgen görüntüleri üzerinden algoritmaya **COVID-19** teşhisi koydurma. (Görüntü İşleme + Makine Öğrenmesi)
*   **Veri Seti:** `COVID/` ve `non-COVID/` klasörlerindeki imaj dosyaları. İşlendikten sonra `tam_veri.csv` olarak saklanır.
*   **İşleyiş (`veri_hazirlama.py`):**
    1.  Görüntüler okunur ve `(28, 28)` boyutlarında renksiz (Grayscale) matrislere dönüştürülür.
    2.  Piksel verileri tek bir satıra (flatten) yayılarak 784 sütunluk özellik (feature) vektörleri elde edilir. Çıkış etiketi (target) listelenerek `DataFrame` oluşturulur.
    3.  Veri %80 eğitim (train) ve %20 test (test) olarak ayrılır.
    4.  Scikit-Learn kütüphanesinden `DecisionTreeClassifier` kullanılarak model eğitilir ve test seti üzerinden bir doğruluk (accuracy) skoru alınır.

### 2. K-En Yakın Komşu (`02_knn`)
K-Nearest Neighbors (KNN), tahmin edilecek verinin eğitim setindeki kendisine en yakın 'k' sayıdaki komşusuna bakılarak sınıfının belirlenmesine dayanan uzaklık tabanlı yapısal bir algoritmadır.

*   **Proje:** Yaprak uzunluklarına ve genişliklerine göre bitki türü (`Species`) tahmini.
*   **Veri Seti:** Bilinen ünlü *Iris* (Süsen çiçeği) tablo veri seti (`Iris.csv`).
*   **İşleyiş (`knn.ipynb`):**
    1.  Tablo `pandas` ile okunur ve özellikler rastgele karıştırılarak (`shuffle`) tahmine hazırlanır.
    2.  Kategorik olan (metin tabanlı tür adları) etiketler `LabelEncoder` vasıtasıyla algoritmaya uygun olarak makinenin anlayabileceği sayılara (`0, 1, 2`) dönüştürülür.
    3.  Tüm özelliklerin (petal length, sepal width vb.) eşit ağırlıkta hesaplamaya girebilmesi için uzaklık temelli algoritmalarda kritik olan özellik ölçekleme (`StandardScaler`) işlemi yapılır.
    4.  En yakın `k=3` komşuya göre `KNeighborsClassifier` kullanılarak model eğitilir.

---

## 🛠️ Kullanılan Teknolojiler:
*   `scikit-learn`: Tüm makine öğrenmesi model mimarileri ve ölçekleyicileri için.
*   `pandas` & `numpy`: Veri çerçeveleri, matris işlemleri ve veri bütünleştirme için.
*   `Pillow (PIL)`: Derin öğrenme / Makine öğrenmesi görüntü önişleme işlemleri için.
