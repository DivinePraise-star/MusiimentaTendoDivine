# File Organization Assignment
#File to organize files in my downmloads folder into subfolders based on file type

import pathlib

downloads_folder = pathlib.Path.home() / "Downloads"

def organize_files_by_type(folder_path):
    for file in folder_path.iterdir():
        if file.is_file():
            file_extension = file.suffix[1:]  # Get the file extension without the dot
            if file_extension:  # Check if the file has an extension
                subfolder_path = folder_path / file_extension
                subfolder_path.mkdir(exist_ok=True)  # Create subfolder if it doesn't exist
                new_file_path = subfolder_path / file.name
                file.rename(new_file_path)  # Move the file to the new subfolder

organize_files_by_type(downloads_folder)
