import os
from datetime import datetime
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def get_unique_filename(dest_path):
    base, extension = os.path.splitext(dest_path)
    counter = 1
    new_dest_path = dest_path

    while os.path.exists(new_dest_path):
        new_dest_path = f"{base}_{counter}{extension}"
        counter += 1

    return new_dest_path

def organize_photos_by_filename(src_folder):
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    for filename in files:
        try:
            if len(filename) >= 15 and filename[8] == '_':
                year = filename[:4]
                month = filename[4:6]

                if not (year.isdigit() and month.isdigit()):
                    print(f"Skipping {filename} - invalid date format")
                    continue

                dest_year_folder = os.path.join(src_folder, year)
                month_name = datetime.strptime(month, "%m").strftime('%B')
                dest_month_folder = os.path.join(dest_year_folder, month_name)

                if not os.path.exists(dest_year_folder):
                    os.makedirs(dest_year_folder)
                if not os.path.exists(dest_month_folder):
                    os.makedirs(dest_month_folder)

                file_path = os.path.join(src_folder, filename)
                dest_path = os.path.join(dest_month_folder, filename)
                dest_path = get_unique_filename(dest_path)
                os.rename(file_path, dest_path)
                print(f"Moved {filename} to {dest_month_folder}")
            else:
                print(f"Skipping {filename} - does not match expected format")
        except Exception as e:
            print(f"Error processing {filename} - {e}")

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
                dest_path = get_unique_filename(dest_path)
                os.rename(file_path, dest_path)
                print(f"Moved {filename} to {dest_month_folder}")
        except Exception as e:
            print(f"Skipping {filename} - {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    source_folder = filedialog.askdirectory(title="Select Folder")

    if source_folder:
        choice = simpledialog.askstring("Choose Method", "Enter '1' to organize by filename or '2' to organize by date taken:")

        if choice == '1':
            try:
                organize_photos_by_filename(source_folder)
                messagebox.showinfo("Organizing Complete", "Photos have been organized successfully by filename!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        elif choice == '2':
            try:
                organize_photos_by_date_taken(source_folder)
                messagebox.showinfo("Organizing Complete", "Photos have been organized successfully by date taken!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Invalid Choice", "You must enter '1' or '2'.")
