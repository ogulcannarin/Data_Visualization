import numpy as np
from PIL import Image
import os
import pandas as pd

covidli = "COVID/"
covid_olmayan = "non-COVID/"

def dosya(yol):
    return [os.path.join(yol, f) for f in os.listdir(yol)]

def veri_donusturme(klasor_adi, sinif_adi):
    goruntuler = dosya(klasor_adi)
    goruntu_sinif = []

    for goruntu in goruntuler:
        goruntu_oku = Image.open(goruntu).convert("L")
        goruntu_boyutlandirma = goruntu_oku.resize((28, 28))
        goruntu_donustur = np.array(goruntu_boyutlandirma).flatten()

        if sinif_adi == "COVID":
            veriler = np.append(goruntu_donustur, [0])
        elif sinif_adi == "non-COVID":
            veriler = np.append(goruntu_donustur, [1])
        else:
            continue

        goruntu_sinif.append(veriler)

    return goruntu_sinif

# verileri oluştur
covidli_veri = veri_donusturme(covidli, "COVID")
covidlidf = pd.DataFrame(covidli_veri)

covid_olmayan_veri = veri_donusturme(covid_olmayan, "non-COVID")
covid_olmayan_df = pd.DataFrame(covid_olmayan_veri)

tum_veri = pd.concat([covidlidf, covid_olmayan_df], ignore_index=True)

print(f"✅ Veri birleştirme tamamlandı! Toplam {len(tum_veri)} adet görüntü işlendi.")
print(tum_veri.head())

# İsteğe bağlı olarak CSV dosyası olarak kaydedebilirsiniz:
tum_veri.to_csv("tam_veri.csv", index=False)
print("Veriler 'tam_veri.csv' olarak kaydedildi.")

# --- Karar Ağacı Modeli Eğitimi ---
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split  # Düzeltildi: sklearn_selection yerine model_selection
from sklearn import metrics

# DataFrame'i Numpy dizisine çeviriyoruz ki dilimleme (slicing) yapabilelim
veri_dizisi = tum_veri.values

# İlk 784 kolon özellikler (pikseller), 784. indeks ise etiket
Giris = veri_dizisi[:, :784]
Cıkıs = veri_dizisi[:, 784]

print("Giriş verisi (X) boyutu:", Giris.shape)
print("Çıkış verisi (y) boyutu:", Cıkıs.shape)

# Veriyi %80 eğitim, %20 test olacak şekilde bölüyoruz
Giris_tr, Giris_ts, Cıkıs_tr, Cıkıs_ts = train_test_split(Giris, Cıkıs, test_size=0.2, random_state=42)

# Modeli oluşturup eğitiyoruz
model = DecisionTreeClassifier()
clf = model.fit(Giris_tr, Cıkıs_tr)

# Test verisi üzerinden tahmin yapıp doğruluk oranını ölçüyoruz
cikis_pred = clf.predict(Giris_ts)
print("Doğruluk Oranı:", metrics.accuracy_score(Cıkıs_ts, cikis_pred))
