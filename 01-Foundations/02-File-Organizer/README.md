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

## 🚨 Error Handling

File movement is protected using `try/except`.

If a file cannot be moved:

1. The error is caught.
2. The error is written to the log.
3. The program continues processing other files.

Example:

```python
try:
    shutil.move(item, unique_destination)
    logging.info(f"FILE MOVED: {item.name} -> {unique_destination}")
except Exception as e:
    logging.error(f"FAILED TO MOVE: {item.name} -> {unique_destination} | Error: {e}")
```

## 🧪 Testing

The organizer was tested using test files with different extensions and scenarios.

Testing included:

* Image files
* Document files
* Video files
* Music files
* Unknown file types
* Duplicate filenames
* Dry-run mode
* Successful file movement
* Failed file movement
* Error logging
* Test files in a safe testing environment

## ⚠️ Safety Precautions

Before using the organizer on real data:

1. Test on a temporary/test folder first.
2. Use dry-run mode to preview changes.
3. Do not initially test on important personal files.
4. Keep a backup of important data.
5. The program moves files; it does not delete them.
6. Duplicate filenames are renamed instead of overwritten.
7. Check `organizer.log` if something goes wrong.
8. Verify the destination folders after organization.

## 📁 Project Structure

```text
02-File-Organizer/
├── app.py
├── README.md
├── organizer.log
├── Images/
├── Documents/
├── Videos/
├── Music/
└── Others/
```

## 🚀 Future Improvements

Possible future upgrades:

* Command-line arguments
* Proper `--dry-run` CLI option
* Configurable categories using JSON/YAML
* Scheduled execution
* Undo/rollback functionality
* Better logging configuration
* GUI interface
* Streamlit interface
* Cloud storage integration

These features are not part of the current version.

## 💼 What This Project Demonstrates

This project demonstrates practical experience with:

* Python automation
* Filesystem manipulation
* Safe file operations
* Error handling
* Logging
* Defensive programming
* Basic software design

## 📌 Project Status

**Project 2 — File Organizer Automation**

| Feature            | Status |
| ------------------ | ------ |
| Scan directory     | ✅      |
| Classify files     | ✅      |
| Create folders     | ✅      |
| Safe file movement | ✅      |
| Duplicate handling | ✅      |
| Dry-run mode       | ✅      |
| Logging            | ✅      |
| Error handling     | ✅      |
| Testing            | ✅      |
| Documentation      | ✅      |

**Project Complete 🎉**
