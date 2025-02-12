import os

def delete_unlabeled_images(folder_path):
    
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    for image_file in image_files:
        label_file = os.path.splitext(image_file)[0] + '.txt'
        if not os.path.exists(os.path.join(folder_path, label_file)):
            # Etiket dosyası yoksa resmi sil
            os.remove(os.path.join(folder_path, image_file))
            print(f"{image_file} silindi.")

data_folder = "dataset"
delete_unlabeled_images(data_folder)
