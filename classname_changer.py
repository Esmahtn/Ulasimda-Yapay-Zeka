import os

#değiştirilmek istenen index numaralarını belirtiyoruz.Hem 0'ları 1 yapıyor hem de tersini
search_text = "0"
replace_text = "1"


folder_path = "dataset"
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]


for file_name in txt_files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        file_content = file.readlines()
    

    for i, line in enumerate(file_content):
        parts = line.split()
        for j, part in enumerate(parts):
            if part == search_text:
                parts[j] = replace_text
            elif part == replace_text:
                parts[j] = search_text
        file_content[i] = " ".join(parts) + "\n"
 
    with open(file_path, 'w') as file:
        file.writelines(file_content)
