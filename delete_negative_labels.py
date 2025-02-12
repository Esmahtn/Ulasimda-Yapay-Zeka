import os

def delete_negative_indices(folder_path):
    
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()

        
        modified_content = ''
        for line in lines:
            parts = line.split()
            has_negative_index = False
            for part in parts[1:]:  # İlk parça sınıf indeksi olduğu için onu kontrol etmiyoruz
                if float(part) < 0:
                    has_negative_index = True
                    break
            
            
            if not has_negative_index:
                modified_content += line
        
        
        with open(file_path, 'w') as file:
            file.write(modified_content)

# Örnek kullanım
dataset_folder = "dataset"
delete_negative_indices(dataset_folder)
