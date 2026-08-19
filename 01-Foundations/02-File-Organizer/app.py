
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

def create_category_folder(category):
    destination = test_folder / category 
    destination.mkdir(exist_ok=True)