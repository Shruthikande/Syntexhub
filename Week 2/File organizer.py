import os
import shutil

FILE_CATEGORIES={
    "Images":[".jpg",".jpeg",".png",".gif",".bmp",".tiff"],
    "Videos":[".mp4",".mkv",".flv",".avi",".mov"],
    "Documents":[".pdf",".doc",".docx",".txt",".ppt",".pptx",".xls",".xlsx"],
    "Audio":[".mp3",".wav",".aac",".flac"],
    "Archives":[".zip",".rar",".7z",".tar",".gz"],
    "Data":[".csv",".json",".xml"],
    "Others":[]
}
def organize_files(directory):
    """organizes files in the given dir based on their file type"""
    if not os.path.isdir(directory):
        print(f"Error:{directory} is not a valid directory")
        return

    for category in FILE_CATEGORIES:
        folder_path=os.path.join(directory,category)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(directory):
        file_path=os.path.join(directory,filename)

        if os.path.isdir(file_path):
            continue
        file_moved=False
        for category,extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved=True
                break

        if not file_moved:
            shutil.move(file_path, os.path.join(directory, category, filename))
            print(f"Moved: {filename} → {category}")

directory_to_organize=input("Enter the directory path to organize:")
organize_files(directory_to_organize)
print(" File organization completed successfully!")


