import os
from datetime import datetime

def organize_photos_by_year_month(src_folder):
    # Create a list of files in the source folder
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    # Iterate through each file
    for filename in files:
        file_path = os.path.join(src_folder, filename)

        # Check if the item is a file
        if os.path.isfile(file_path):
            modification_time = os.path.getmtime(file_path)
            modification_date = datetime.fromtimestamp(modification_time)

            # Create destination folder based on the year and month
            dest_folder = os.path.join(src_folder, modification_date.strftime('%Y'), modification_date.strftime('%B'))

            # If the destination folder doesn't exist, create it
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            # Move the file to the destination folder
            dest_path = os.path.join(dest_folder, filename)
            os.rename(file_path, dest_path)
            print(f"Moved {filename} to {dest_folder}")

if __name__ == "__main__":
    source_folder = r'E:\files' #Change path
    organize_photos_by_year_month(source_folder)
