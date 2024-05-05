import os
from datetime import datetime
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def get_date_taken(file_path):
    try:
        with Image.open(file_path) as img:
            info = img._getexif()
            if info is not None and 36867 in info:
                date_taken_str = info[36867]
                return datetime.strptime(date_taken_str, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        raise RuntimeError(f"Error extracting date taken from {file_path}: {e}")

def organize_photos_by_date_taken(src_folder):
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    for filename in files:
        file_path = os.path.join(src_folder, filename)

        try:
            date_taken = get_date_taken(file_path)
            if date_taken:
                dest_year_folder = os.path.join(src_folder, date_taken.strftime('%Y'))
                dest_month_folder = os.path.join(dest_year_folder, date_taken.strftime('%B'))

                if not os.path.exists(dest_year_folder):
                    os.makedirs(dest_year_folder)
                if not os.path.exists(dest_month_folder):
                    os.makedirs(dest_month_folder)

                dest_path = os.path.join(dest_month_folder, filename)
                os.rename(file_path, dest_path)
                print(f"Moved {filename} to {dest_month_folder}")
        except Exception as e:
            print(f"Skipping {filename} - {e}")

if __name__ == "__main__":
    # GUI-based folder selection
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    source_folder = filedialog.askdirectory(title="Select Folder")

    if source_folder:
        try:
            organize_photos_by_date_taken(source_folder)
            messagebox.showinfo("Organizing Complete", "Photos have been organized successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
