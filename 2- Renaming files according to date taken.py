import os
from datetime import datetime
from PIL import Image

def get_date_taken(file_path):
    try:
        with Image.open(file_path) as img:
            info = img._getexif()
            if info is not None and 36867 in info:
                date_taken_str = info[36867]
                return datetime.strptime(date_taken_str, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Error extracting date taken from {file_path}: {e}")
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

                # Handle duplicate names
                counter = 1
                while os.path.exists(os.path.join(folder_path, new_filename)):
                    new_filename = f"{date_taken_str}_{counter}{os.path.splitext(filename)[1]}"
                    counter += 1

                # Rename the file
                os.rename(file_path, os.path.join(folder_path, new_filename))
                total_renamed += 1

    print(f"Total files renamed: {total_renamed}")

if __name__ == "__main__":
    folder_path = r'E:\Photos'  # Change Path
    rename_files_by_date_taken(folder_path)
