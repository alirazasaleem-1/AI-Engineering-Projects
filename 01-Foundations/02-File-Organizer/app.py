
from pathlib import Path 
import shutil 

categories = {
    "Images": ['.png', '.jpg','.jpeg', '.svg'],
    "Documents": ['.doc', '.docx', '.pdf', '.txt'],
    "Videos": ['.mp4', '.mkv', '.avi'],
    "Music": ['.mp3', '.wav', '.flac']
}


def get_category(file):
    for category, extensions in categories.items():
        if file.suffix in extensions:
            return category 
    return "Others"