import os
from datetime import datetime
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files_by_creation_datetime(folder_path):
    total_renamed = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the item is a file
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            creation_datetime = datetime.fromtimestamp(creation_time).strftime('%Y%m%d_%H%M%S')

            # Form the new filename using the creation date and time
            new_filename = f"{creation_datetime}{os.path.splitext(filename)[1]}"

            # Handle duplicate names
            counter = 1
            while os.path.exists(os.path.join(folder_path, new_filename)):
                new_filename = f"{creation_datetime}_{counter}{os.path.splitext(filename)[1]}"
                counter += 1

            # Rename the file
            os.rename(file_path, os.path.join(folder_path, new_filename))
            total_renamed += 1

    messagebox.showinfo("Renaming Complete", f"Total files renamed: {total_renamed}")

def get_date_taken(file_path):
    try:
        with Image.open(file_path) as img:
            info = img._getexif()
            if info is not None and 36867 in info:
                date_taken_str = info[36867]
                return datetime.strptime(date_taken_str, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Error extracting date taken from {file_path}: {e}")
        messagebox.showinfo("Date Taken Error", f"Error extracting date taken from {file_path}: {e}")
    return None

def rename_files_by_date_taken(folder_path):
    total_renamed = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            date_taken = get_date_taken(file_path)

            if date_taken:
                # Format the date and time for the new filename
                date_taken_str = date_taken.strftime('%Y%m%d_%H%M%S')

                # Form the new filename using the date taken and existing file extension
                new_filename = f"{date_taken_str}{os.path.splitext(filename)[1]}"
            else:
                # If no date taken information, use creation datetime
                creation_time = os.path.getctime(file_path)
                creation_datetime = datetime.fromtimestamp(creation_time).strftime('%Y%m%d_%H%M%S')
                new_filename = f"{creation_datetime}{os.path.splitext(filename)[1]}"

            # Handle duplicate names
            counter = 1
            while os.path.exists(os.path.join(folder_path, new_filename)):
                new_filename = f"{date_taken_str}_{counter}{os.path.splitext(filename)[1]}"
                counter += 1

            # Rename the file
            os.rename(file_path, os.path.join(folder_path, new_filename))
            total_renamed += 1

    messagebox.showinfo("Renaming Complete", f"Total files renamed: {total_renamed}")

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory(title="Select Folder")
    return folder_path

def show_rename_option_window():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    choice = tk.messagebox.askquestion("Choose Renaming Option", "Select renaming option:\nRename files by creation datetime?\n(Yes) or Rename files by date taken from metadata?\n(No)")

    return choice == 'yes'

if __name__ == "__main__":
    folder_path = select_folder()

    if folder_path:
        if show_rename_option_window():
            rename_files_by_creation_datetime(folder_path)
        else:
            rename_files_by_date_taken(folder_path)
