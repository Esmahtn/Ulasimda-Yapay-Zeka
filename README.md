# Ulasimda-Yapay-Zeka
📌 Teknofest Görüntü İşleme Scriptleri / Teknofest Image Processing Scripts

📜 Description

This project provides Python scripts for image processing tasks such as renaming, resizing, label verification, and region selection, used in the Teknofest competition.

📂 İçerik / Contents

rename.py → Belirtilen klasördeki .jpg, .jpeg ve .png dosyalarını sıralı bir şekilde yeniden adlandırır.

Renames .jpg, .jpeg, and .png files in the specified folder in sequential order.

resize.py → _images klasöründeki görselleri 640x640 boyutlarına küçültüp yarisma_goruntu klasörüne kaydeder.

Resizes images in the _images folder to 640x640 pixels and saves them in the yarisma_goruntu folder.

roi_selection.py → Video üzerinden kullanıcının seçtiği bölgeyi belirlemek için bir araç sağlar ve işlenen kareyi kaydeder.

Provides a tool for selecting a region of interest (ROI) from a video and saves the processed frame.

delete_unabled_image.py → Etiketlenmemiş (kullanılmayan) resimleri belirleyip siler.

Detects and deletes unlabelled (unused) images.

delete_negative_labels.py → Yanlış veya negatif etiket içeren resimleri tespit edip siler.

Identifies and removes incorrectly labeled or negatively labeled images.

🛠 Kullanılan Teknolojiler / Technologies Used

OpenCV, Pillow (PIL), os, imutils, numpy

🚀 Kullanım / Usage

Resimleri Yeniden Adlandırma / Rename Images → rename.py çalıştırıldığında _images klasöründeki resimler otomatik olarak yeniden adlandırılır.

When rename.py is executed, images in the _images folder are automatically renamed.

Resimleri Boyutlandırma / Resize Images → resize.py çalıştırıldığında _images klasöründeki resimler 640x640 piksele ölçeklenir ve yarisma_goruntu klasörüne kaydedilir.

When resize.py is executed, images in the _images folder are resized to 640x640 pixels and saved in the yarisma_goruntu folder.

ROI Seçme / Select ROI → roi_selection.py çalıştırıldığında kampus.mp4 videosu açılır. Fare ile tıklayarak ROI (Region of Interest) seçimi yapılabilir. ESC tuşuna basıldığında seçili alan roi.png olarak kaydedilir.

When roi_selection.py is executed, kampus.mp4 video opens, allowing users to select a Region of Interest (ROI) by clicking. Pressing the ESC key saves the selected area as roi.png.

Etiketlenmemiş Resimleri Silme / Delete Unused Images → delete_unabled_image.py çalıştırıldığında, etiketsiz resimler silinir.

When delete_unabled_image.py is executed, unlabelled images are deleted.

Negatif Etiketleri Temizleme / Remove Negative Labels → delete_negative_labels.py çalıştırıldığında, negatif etiket içeren resimler temizlenir.

When delete_negative_labels.py is executed, negatively labeled images are removed.
