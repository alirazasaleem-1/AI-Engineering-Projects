
from pathlib import Path 
import shutil 

categories = {
    "Images": ['.png', '.jpg','.jpeg', '.svg'],
    "Documents": ['.doc', '.docx', '.pdf', '.txt'],
    "Videos": ['.mp4', '.mkv', '.avi'],
    "Music": ['.mp3', '.wav', '.flac']
}

test_folder = Path(r"D:\PythonProjects\AI-Engineering-Projects\01-Foundations\02-File-Organizer")

def get_category(file):
    for category, extensions in categories.items():
        if file.suffix in extensions:
            return category 
    return "Others"

def create_category_folder(folder, category):
    destination = folder / category 
    destination.mkdir(exist_ok=True)
    return destination 

def get_unique_destination(destination_file):
    counter = 1
    original_stem = destination_file.stem 
    while destination_file.exists():
        new_name = f"{original_stem}_{counter}{destination_file.suffix}" 
        destination_file = destination_file.parent / new_name
        counter += 1 
    return destination_file 

def organize_folder(test_folder):
    for item in test_folder.iterdir():
        if item.is_file():
            category = get_category(item)
            destination = create_category_folder(test_folder, category)
            destination_file = destination / item.name 
            unique_destination = get_unique_destination(destination_file)
            shutil.move(item, unique_destination)

organize_folder(test_folder)
print("Folder is organizedn now.")