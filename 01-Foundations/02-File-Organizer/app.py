from pathlib import Path
import shutil 
import logging 

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

def organize_folder(test_folder, dry_run = False):
    for item in test_folder.iterdir():
        if item.is_file():
            
            if item.name == "app.py":
                continue 

            category = get_category(item)
            destination = create_category_folder(test_folder, category)
            destination_file = destination / item.name 
            unique_destination = get_unique_destination(destination_file)
            if dry_run:
                print(f"DRY RUN: {item.name} -> {unique_destination}")
            else: 
                shutil.move(item, unique_destination)

    if dry_run:
        print("Dry run completed. No files were moved.")
    else:
        print("Folder organized successfully.")

organize_folder(test_folder)