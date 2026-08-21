# 📁 File Organizer Automation

A Python automation script that organizes files in a folder into category-based directories based on their file extensions.

## 🎯 Project Goal

Messy folders can contain images, documents, videos, music, and unknown file types mixed together.

This project automates the organization process:

```text
Messy Folder
     ↓
Scan Files
     ↓
Detect File Type
     ↓
Choose Category
     ↓
Create Category Folder
     ↓
Find Safe Destination
     ↓
Move File
```

Example:

```text
Before:

File-Organizer/
├── cat.jpg
├── report.pdf
├── movie.mp4
├── song.mp3
└── unknown.xyz


After:

File-Organizer/
├── Images/
│   └── cat.jpg
├── Documents/
│   └── report.pdf
├── Videos/
│   └── movie.mp4
├── Music/
│   └── song.mp3
└── Others/
    └── unknown.xyz
```

## 🛠️ Technologies Used

* Python
* pathlib
* shutil
* logging

Only Python's standard library is used.

## 🧠 Concepts Practiced

* Python functions
* Dictionaries
* Lists
* Loops and conditions
* pathlib
* Filesystem traversal
* File extensions
* Directory creation
* File movement
* Duplicate filename handling
* Boolean parameters
* `continue`
* `try/except`
* Logging
* Dry-run mode
* Basic Git workflow

## 📂 File Categories

| Category  | Extensions                      |
| --------- | ------------------------------- |
| Images    | `.png`, `.jpg`, `.jpeg`, `.svg` |
| Documents | `.doc`, `.docx`, `.pdf`, `.txt` |
| Videos    | `.mp4`, `.mkv`, `.avi`          |
| Music     | `.mp3`, `.wav`, `.flac`         |
| Others    | Any unsupported extension       |

Unknown file types are placed in the `Others` folder.

## ⚙️ How It Works

### 1. Scan the Folder

The program uses `pathlib` to scan the target directory:

```python
for item in test_folder.iterdir():
```

Only files are processed.

### 2. Detect File Category

The `get_category()` function checks the file extension against the category dictionary.

Example:

```text
cat.jpg
   ↓
.jpg
   ↓
Images
```

If the extension is not recognized:

```text
unknown.xyz
   ↓
Others
```

### 3. Create Category Folder

The `create_category_folder()` function creates the required destination folder if it does not already exist.

```python
destination.mkdir(exist_ok=True)
```

### 4. Handle Duplicate Filenames

The `get_unique_destination()` function prevents existing files from being overwritten.

If `Images/cat.jpg` already exists, the new file becomes:

```text
Images/cat_1.jpg
```

If that also exists:

```text
Images/cat_2.jpg
```

The program continues until it finds an available filename.

### 5. Move Files Safely

Files are moved using:

```python
shutil.move()
```

Before moving, the program calculates a unique destination so an existing file is not overwritten.

## 👀 Dry-Run Mode

The organizer supports a dry-run mode.

Dry-run previews what the program would do without actually moving files.

Example:

```text
DRY RUN: cat.jpg -> Images/cat.jpg
DRY RUN: report.pdf -> Documents/report.pdf
```

No files are moved during a dry run.

This allows changes to be reviewed before running the organizer normally.

## 📝 Logging

The project uses Python's built-in `logging` module.

Logs are stored in:

```text
organizer.log
```

Successful file movements are recorded:

```text
INFO:root:FILE MOVED: test2.jpg -> ...\Images\test2.jpg
```

Errors are also recorded:

```text
ERROR:root:FAILED TO MOVE: test3.jpg -> ...\Images\test3.jpg | Error: ...
```

This provides a record of what happened during execution.
