import os
import shutil
import tkinter as tk
from tkinter import filedialog

def move_files_to_destination(src_folder, dest_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Iterate through all files in the source folder and its subfolders
    for root, dirs, files in os.walk(src_folder):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Move the file to the destination folder
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} to {dest_folder}")

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(title="Select Folder")
    return folder_path

if __name__ == "__main__":
    print("Select the source folder:")
    source_folder = select_folder()
    print("Select the destination folder:")
    destination_folder = select_folder()

    if source_folder and destination_folder:
        move_files_to_destination(source_folder, destination_folder)
