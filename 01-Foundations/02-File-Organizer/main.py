from pathlib import Path 

test_folder = Path(r"D:\PythonProjects\AI-Engineering-Projects\01-Foundations\02-File-Organizer")

for item in test_folder.iterdir():
    if item.is_file():
        print(f"File Name: {item.name}")
        print(f"Extension: {item.suffix}")
        if item.suffix in ['.jpg', '.png']:
            print("It's an image")
            category = "image"
        if item.suffix in ['.pdf', '.doc', '.docx']:
            print("It's a document.")
            category = "document"
        if item.suffix in ['.mp4']:
            print("It's a video.")
            category = "video"