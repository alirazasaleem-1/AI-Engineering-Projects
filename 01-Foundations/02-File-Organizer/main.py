from pathlib import Path 
import shutil 

test_folder = Path(r"D:\PythonProjects\AI-Engineering-Projects\01-Foundations\02-File-Organizer")

for item in test_folder.iterdir():
    if item.is_file():
        print(f"File Name: {item.name}")
        print(f"Extension: {item.suffix}")
        if item.suffix in ['.jpg', '.png']:
            print("It's an image")
            category = "image"
            destination = test_folder / "Images"
            destination.mkdir(exist_ok=True)
            destination_file = destination / item.name 
            counter = 1

            while destination_file.exists():
                new_name = f"{item.stem}_{counter}{item.suffix}"
                destination_file = destination / new_name
                shutil.move(item, destination_file)
                counter += 1

            if not destination_file.exists():
                shutil.move(item, destination)

        elif item.suffix in ['.pdf', '.doc', '.docx']:
            print("It's a document.")
            category = "document"
            destination = test_folder / "Documents"
            destination.mkdir(exist_ok=True)
            destination_file = destination / item.name
            counter = 1

            while destination_file.exists():
                new_name = f"{item.stem}_{counter}{item.suffix}"
                destination_file = destination / new_name
                counter += 1

            if not destination_file.exists():
                shutil.move(item, destination)

        elif item.suffix in ['.mp4']:
            print("It's a video.")
            category = "video"
            destination = test_folder / "Videos"
            destination.mkdir(exist_ok=True)
            destination_file = destination / item.name 
            counter = 1 

            while destination_file.exists():
                new_name = f"{item.stem}_{counter}{item.suffix}"
                destination_file = destination / new_name
                counter += 1 

            if not destination_file.exists():
                shutil.move(item, destination)
              