import os
import shutil

# Folder to organize (change this path to something on your system when running)
folder_path = "Downloads"

# File type categories
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3', '.wav'],
    'Code': ['.py', '.ipynb', '.java', '.cpp'],
    'Archives': ['.zip', '.rar']
}

def organize_folder(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            for category, extensions in file_types.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(path, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    print(f"Moved: {file} → {category}")
                    break

# Run
organize_folder(folder_path)
