import os
import glob

# Resimlerin bulunduğu klasörün yolu
klasor_yolu = "dataset/"

# Klasördeki tüm resim/txt dosyalarını bul
resimler_txt = glob.glob(os.path.join(klasor_yolu, "*.jpg"))  

# Başlangıç numarası
baslangic_numarasi = 271

# Yeniden adlandırma işlemi
for i, eski_ad in enumerate(resimler_txt, start=baslangic_numarasi):
    yeni_ad = os.path.join(klasor_yolu, f"{i}.jpg")  
    os.rename(eski_ad, yeni_ad)
    print(f"{eski_ad} dosyası {yeni_ad} olarak yeniden adlandırıldı.")