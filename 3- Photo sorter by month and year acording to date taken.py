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

def organize_photos_by_date_taken(src_folder):
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    for filename in files:
        file_path = os.path.join(src_folder, filename)

        if os.path.isfile(file_path):
            date_taken = get_date_taken(file_path)

            if date_taken:
                dest_folder = os.path.join(src_folder, date_taken.strftime('%Y'), date_taken.strftime('%B'))

                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                dest_path = os.path.join(dest_folder, filename)
                os.rename(file_path, dest_path)
                print(f"Moved {filename} to {dest_folder}")
            else:
                print(f"Skipping {filename} - could not extract date taken")

if __name__ == "__main__":
    source_folder = r'E:\Photos'  # Change path
    organize_photos_by_date_taken(source_folder)
