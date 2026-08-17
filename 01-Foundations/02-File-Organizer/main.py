from pathlib import Path 

folder = Path(r"D:\PythonProjects\AI-Engineering-Projects\01-Foundations\02-File-Organizer")

for item in folder.rglob("*"):
    print(item)